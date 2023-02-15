from math import ceil
import sqlite3
import pandas as pd
import numpy as np
from pathlib import Path
from pandas_datareader import get_quote_yahoo
from django.db import transaction

from .index_parameters import index_filter_parameters, rank_order, sector_target_parameters, position_weight_parameters, user_parameters, columns_of_interest
from personalized_index.models import PersonalizedIndex, PersonalizedIndexStock, Stock


# TODO (if needed) write function to clean yf data; check data quality
def import_data(db_file: str) -> pd.DataFrame:
    """import yf data from database and return as pandas dataframe"""
    conn = sqlite3.connect(db_file)
    query = "SELECT * FROM personalized_index_stock"
    df = pd.read_sql_query(query, conn)
    conn.close()
    return df
    # Note: could filter out excluded sectors here


# TODO write test to check that these filters are working correctly
def filter_universe(df: pd.DataFrame, market_cap_min, dividend_yield_min, pe_ratio_max) -> pd.DataFrame:
    """Filters the universe of stock data by conditions on attributes."""
    df = df[(df['dividend_yield'] >= dividend_yield_min) &
            (df['market_cap'] >= market_cap_min) &
            (df['forward_pe'] <= pe_ratio_max) &
            (df['forward_pe'] >= index_filter_parameters['pe_ratio_min'])]
    return df


# TODO robust testing of the sorting algorithm
def sort_universe(df: pd.DataFrame, rank_order: list) -> pd.DataFrame:
    """Sorts the universe of stock data by conditions on attributes."""
    return df.sort_values(by=[rank_order[0], rank_order[1], rank_order[2]], ascending=[False, False, True], na_position='last')


def get_sector_table(df: pd.DataFrame, filtered_df: pd.DataFrame, sector_exclude_1, sector_exclude_2) -> pd.DataFrame:
    """Construct table with pct of stocks in sector and target num per sector within a given universe."""
    # TODO generalize to n excluded sectors
    df = df[(df['sector'] != sector_exclude_1) &
            (df['sector'] != sector_exclude_2)]
    sector_table = df['sector'].value_counts()
    sector_table = pd.DataFrame(sector_table)
    sector_table.columns = ['sector_count']
    sector_table = sector_table.assign(
        sector_freq=df['sector'].value_counts(normalize=True))
    sector_table = sector_table.assign(sector_prop=sector_table['sector_freq'] *
                                       sector_target_parameters['sector_max_number'] * len(sector_table.index))
    sector_table = sector_table.assign(sector_target=(
        (1-sector_target_parameters['sector_equalization']) * sector_target_parameters['sector_max_number'] + sector_target_parameters['sector_equalization'] * sector_table['sector_prop']))
    sector_table = sector_table.assign(
        filtered_freq=filtered_df['sector'].value_counts())
    return sector_table


def get_stock_selection(sorted_df: pd.DataFrame, sector_table: pd.DataFrame) -> pd.DataFrame:
    """Get stocks for personalized index based on sector targets and filtered/sorted universe"""
    stock_selection = pd.DataFrame(columns=sorted_df.columns)
    for sector in sector_table.index:
        sector_list = sorted_df[sorted_df['sector'] == sector].head(ceil(min(
            sector_table.loc[sector]['sector_count'], sector_table.loc[sector]['sector_target'])))
        stock_selection = pd.concat([stock_selection, sector_list])
    stock_selection = stock_selection.sort_values(
        'market_cap', ascending=False)
    return stock_selection


# TODO generalize for a low-market cap tranche
def get_stock_weights(df: pd.DataFrame) -> pd.DataFrame:
    """Calculate portfolio weights of stocks in personalized index."""
    df = df.reset_index()
    df.loc[df.index < position_weight_parameters['top_tranche_num'],
           'position_weight'] = position_weight_parameters['top_tranche_weight']
    df.loc[df.index >= position_weight_parameters['top_tranche_num'], 'position_weight'] = (
        1 - position_weight_parameters['top_tranche_num']*position_weight_parameters['top_tranche_weight'])/(len(df.index) - position_weight_parameters['top_tranche_num'])
    return df


def get_target_allocation(df: pd.DataFrame, index_allocation) -> pd.DataFrame:
    df = df.assign(
        target_allocation=df['position_weight'] * index_allocation)
    return df


def get_current_price(df: pd.DataFrame) -> pd.DataFrame:
    """Gets current price for all stocks in data frame."""
    data = get_quote_yahoo(df['symbol'].astype('str').to_list())[
        'price'].to_list()
    df['current_price'] = data
    return df


def get_order_quantity(df: pd.DataFrame) -> pd.DataFrame:
    """Calculates order quantities given price and target allocation in dollars."""
    df = df.assign(quantity=df['target_allocation']/df['current_price'])
    df = df.assign(order_quantity=df['quantity'].apply(np.floor))
    df = df.assign(rounding_loss=df['current_price']
                   * (df['quantity'] - df['order_quantity']))
    return df


def orders_to_csv(df: pd.DataFrame, index_name) -> None:
    index_name = index_name.replace(" ", "_")
    filepath = Path(__file__).parent / "data"
    df.to_csv(
        filepath / f"personalized_index_{index_name}.csv", mode='w', index=False)
    df = df[['symbol', 'order_quantity']]
    df['order_quantity'] = df['order_quantity'].apply(np.int64)
    df.to_csv(filepath / f"orders_{index_name}.csv", mode='w', index=False)
    return None


def store_personalized_index(df: pd.DataFrame, index_id) -> None:
    df = df.drop(columns=['index', 'sector', 'country', 'dividend_yield', 'forward_pe', 'long_business_summary',
                 'market_cap', 'short_name', 'trailing_eps', 'trailing_pe'], inplace=False)
    df = df.assign(personalized_index_id=index_id)
    df.rename(columns={'symbol': 'symbol_id'}, inplace=True)
    with transaction.atomic():
        PersonalizedIndexStock.objects.filter(
            personalized_index_id=index_id).delete()
        PersonalizedIndexStock.objects.bulk_create(
            [PersonalizedIndexStock(**row) for row in df.to_dict("records")])


def get_personalized_index(index_id):
    # Import stock data
    db_file = (Path(__file__).parent.parent / "db.sqlite3").resolve()
    df = import_data(db_file)

    index = PersonalizedIndex.objects.get(id=index_id)
    index_name = index.index_name
    index_allocation = index.index_allocation
    market_cap_min = index.market_cap_min
    dividend_yield_min = index.dividend_yield_min
    pe_ratio_max = index.pe_ratio_max
    sector_exclude_1 = index.sector_exclude_1
    sector_exclude_2 = index.sector_exclude_2

    # Create index selection based on personalized parameters
    filtered_df = filter_universe(
        df, market_cap_min, dividend_yield_min, pe_ratio_max)
    sorted_df = sort_universe(filtered_df, rank_order)
    sector_table = get_sector_table(
        df, filtered_df, sector_exclude_1, sector_exclude_2)
    stock_selection = get_stock_selection(sorted_df, sector_table)
    personalized_index = get_stock_weights(stock_selection)
    personalized_index = get_target_allocation(
        personalized_index, index_allocation)
    personalized_index = get_current_price(personalized_index)
    personalized_index = get_order_quantity(personalized_index)

    # Save real-time index values to personalizedindexstock table
    store_personalized_index(personalized_index, index_id)

    # Save index metadata (and print), and save stock orders to csv
    orders_to_csv(personalized_index, index_name)


# TODO special handling for dual tickers like GOOG and GOOGL
# TODO stock exclude capabilities
# TODO add portfolio summary report including total rounding loss
# TODO add reconciliation with existing portfolio
# TODO add rebalancing and tax-loss harvesting
if __name__ == '__main__':
    get_personalized_index(1)