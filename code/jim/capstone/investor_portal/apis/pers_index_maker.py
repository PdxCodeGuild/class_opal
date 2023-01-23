"""
PDX Code Guild Python Minicapstone - James Brennan - 2022.11.28 
This module reads a stock metadata csv and uses pandas to
manipulate the data and produce a list of stock orders for
a personalized index based on a set of input parameters.
"""

import time
from math import ceil
import pandas as pd
import numpy as np
from pathlib import Path
from pandas_datareader import get_quote_yahoo
from .index_parameters import index_filter_parameters, rank_order, sector_target_parameters, position_weight_parameters, user_parameters, columns_of_interest


# TODO (if needed) write function to clean yf data; check data quality
def import_data(filename: str) -> pd.DataFrame:
    """import yf data from csv and return as pandas dataframe"""
    filepath = Path(__file__).parent / filename
    df = pd.read_csv(filepath)
    return df[columns_of_interest]
    # Note: could filter out excluded sectors here


# TODO write test to check that these filters are working correctly
def filter_universe(df: pd.DataFrame, market_cap_min, dividend_yield_min, pe_ratio_max) -> pd.DataFrame:
    """Filters the universe of stock data by conditions on attributes."""
    df = df[(df['dividendYield'] >= dividend_yield_min) &
            (df['marketCap'] >= market_cap_min) &
            (df['forwardPE'] <= pe_ratio_max) &
            (df['forwardPE'] >= index_filter_parameters['pe_ratio_min'])]
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
    stock_selection = stock_selection.sort_values('marketCap', ascending=False)
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


def get_personalized_index(index_name, index_allocation, market_cap_min=5_000_000_000, dividend_yield_min=0, pe_ratio_max="", sector_exclude_1="", sector_exclude_2=""):
    # start_time = time.time()

    # Import stock data
    filename = "universe.csv"
    df = import_data(filename)

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

    # Save index metadata (and print), and save stock orders to csv
    orders_to_csv(personalized_index, index_name)

    # Print summary portfolio metrics. Should have sum(potion_weight) near 1.
    # print(personalized_index.head(30))
    # print(personalized_index['position_weight'].sum())
    # print(personalized_index['target_allocation'].sum())

    # print(f"My program took {time.time() - start_time} seconds to run.")


# TODO special handling for dual tickers like GOOG and GOOGL
# TODO stock exclude capabilities
# TODO add portfolio summary report including total rounding loss
# TODO add reconciliation with existing portfolio
# TODO add rebalancing and tax-loss harvesting
if __name__ == '__main__':
    get_personalized_index("test_index", 105_000,
                           5_000_000_000, 0.01, 100, "Real Estate", "Energy")
