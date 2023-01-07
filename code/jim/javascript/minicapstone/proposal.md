# PDX Code Guild Fullstack Developer Capstone
### *James Brennan - 2023.01.01*

## Summary of Python Minicapstone Features

### `personlized_index.py` 
Reads a stock metadata csv and uses pandas to manipulate the data and produce a list of stock orders for a personalized index based on a set of input parameters.
* `import_data` reads data from csv and returns it in a pandas dataframe. Uses a filter based on yfinance library and the Yahoo! Finance API and columns_of_interest defined in index_parameters.py.
* Methods to construct a "sector table" with summary sector statistics that are used to help filter the list of stocks selected for the personalized index.
* Methods to manipulate the dataframe to filter for the personalized index based on criteria defined in index_parameters.py.
* `get_current_price` pulls current stock price in real time for all symbols on personalized index list.
* `orders_to_csv` produces a csv with columns for stock symbol and quantity to be ordered.

### `universe_construction.py`
This module returns a csv metadata for all S&P 500 tickers using the Wikipedia and Yahoo Finance APIs.
* `get_wikipedia_tickers` Gets the list of n S&P 500 tickers from Wikipedia.
* `get_yfinance_tickers_data` and `get_yfinance_tickers_info` pulls info from the Yahoo! Finance API using the yfinance library. Note this process takes over 10 minutes to complete; would like to find a way to speed this up.
* `tickers_info_to_csv` Converts universe of tickers info to pandas dataframe and writes to csv.

### `invalid_tickers.py`
This module returns uses pandas_datareader to determine which S&P 500 tickers from Wikipedia are not recognized by the Yahoo finance API due to formatting differences.

### `index_parameters.py`
Set of input parameters for the personalized_index.py module. (Could be integrated as a cash flow planning class.) The parameter data is stored in python dictionaries. Could store these in a database and provide an interface to allow a user to modify the parameters for a particular personalized index.

## Javascript Minicapstone Plan



