"""
PDX Code Guild Python Minicapstone - James Brennan - 2022.11.28 
This module returns a csv metadata for all S&P 500 tickers using the 
Wikipedia and Yahoo Finance APIs.
"""

import time
import bs4 as bs
import requests
import yfinance as yf
import pandas as pd
from index_parameters import invalid_tickers


# TODO rewrite to pull sector info and reformat instead of remove invalid tickers.
def get_wikipedia_tickers(n=None):
    """Gets the list of n S&P 500 tickers from Wikipedia"""
    resp = requests.get(
        'http://en.wikipedia.org/wiki/List_of_S%26P_500_companies')
    soup = bs.BeautifulSoup(resp.text, 'lxml')
    table = soup.find('table', {'class': 'wikitable sortable'})
    tickers = []
    for row in table.findAll('tr')[1:]:
        ticker = row.findAll('td')[0].text
        tickers.append(ticker)

    # reformat ticker list
    tickers = [s.replace('\n', '') for s in tickers][:n]

    # remove invalid tickers
    return [t for t in tickers if t not in invalid_tickers]


# TODO Rewrite these functions to use the pandas datareader API for yahoo finance.
def get_yfinance_tickers_data(ticker_list: list) -> yf.Tickers:
    """pull data from yfinance for a list of tickers"""
    return yf.Tickers(ticker_list)


def get_yfinance_tickers_info(ticker_list: list, tickers: yf.Tickers) -> list:
    """list of dicts of metadata for each ticker"""
    return [tickers.tickers[ticker].info for ticker in ticker_list]


def tickers_info_to_csv(universe: list):
    """convert universe of tickers info to pandas dataframe and write to csv"""
    df = pd.DataFrame.from_dict(universe)
    df = df[['sector', 'longBusinessSummary', 'country', 'shortName', 'symbol',
             'trailingEps', 'forwardPE', 'marketCap', 'dividendYield', 'trailingPE']]
    timestr = time.strftime("%Y%m%d-%H%M%S")
    df.to_csv(f"{universe=}".split('=')[0] + f"_{timestr}.csv")


if __name__ == '__main__':
    start_time = time.time()

    n = 3  # number of tickers to download - set to None for full S&P list

    ticker_list = get_wikipedia_tickers(n)
    tickers = get_yfinance_tickers_data(ticker_list)
    universe = get_yfinance_tickers_info(ticker_list, tickers)
    tickers_info_to_csv(universe)

    print(f"My program took {time.time() - start_time} seconds to run.")
