"""
PDX Code Guild Python Minicapstone - James Brennan - 2022.11.28 
This module returns uses pandas_datareader to determine
which S&P 500 tickers from Wikipedia are not recognized by the
Yahoo finance API due to formatting differences.
"""

import time
import bs4 as bs
import requests
import yfinance as yf
import pandas as pd
from pandas_datareader import data
from index_parameters import invalid_tickers

start_time = time.time()

# get the list of SP500 tickers from Wikipedia
resp = requests.get('http://en.wikipedia.org/wiki/List_of_S%26P_500_companies')
soup = bs.BeautifulSoup(resp.text, 'lxml')
table = soup.find('table', {'class': 'wikitable sortable'})
tickers = []
for row in table.findAll('tr')[1:]:
    ticker = row.findAll('td')[0].text
    tickers.append(ticker)

# remove invalid tickers
tickers = [t for t in tickers if t not in invalid_tickers]

# reformat tickers list
ticker_list = [s.replace('\n', '') for s in tickers][:70]

# define list of attributes of interest
# attribute_list = ['shortName', 'marketCap',
#                   'forwardPE', 'trailingAnnualDividendRate']


def get_tickers_info(ticker_list, attribute):
    universe = {}
    invalid_tickers = []
    for ticker in ticker_list:
        try:
            universe[ticker] = data.get_quote_yahoo(ticker)[attribute][ticker]
        except KeyError:
            universe[ticker] = 'NA'
            invalid_tickers.append(ticker)
    return universe, invalid_tickers


universe = get_tickers_info(ticker_list, 'price')[0]
invalid_tickers = get_tickers_info(ticker_list, 'price')[1]

print(universe)
print(invalid_tickers)

print(f"My program took {time.time() - start_time} seconds to run.")
