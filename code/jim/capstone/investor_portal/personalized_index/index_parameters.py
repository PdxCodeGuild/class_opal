"""
PDX Code Guild Python Minicapstone - James Brennan - 2022.11.29 
Set of input parameters for the personalized_index.py module.
Could be integrated as a cash flow planning classs.
"""

columns_of_interest = ['sector', 'longBusinessSummary',
                       'country', 'shortName', 'symbol',
                       'trailingEps', 'forwardPE', 'marketCap', 'dividendYield', 'trailingPE']

index_filter_parameters = {
    'market_cap_min': 5_000_000_000,
    'dividend_yield_min': 0.01,
    'pe_ratio_max': 100,
    'pe_ratio_min': 0
}

sector_target_parameters = {
    'sector_max_number': 7,
    'sector_equalization': 0.8,
    'sector_exclude_1': 'Real Estate',
    'sector_exclude_2': 'Energy',
}

rank_order = ['dividendYield', 'marketCap', 'trailingPE']

position_weight_parameters = {
    'position_weight_max': 0.03,
    'position_weight_min': 0.003,
    'sector_weight_dev_max': 0.2,
    'sector_weight_dev_min': 0.2,
    'final_weight_choice': 'top_n_tranched',
    'top_tranche_num': 25,
    'top_tranche_weight': 0.02,
    'top_tranche_min_market_cap': 5_000_000_000
}

user_parameters = {
    'pers_index_allocation': 105_000
}

invalid_tickers = ['BRK.B', 'BF.B']

# N.B.: Sector_equalization=0 implies full equal weight, =1 implies full mkt cap weight
# TODO write portfolio class with attributes like parameters in PI spreadsheet
# TODO handle negative and missing PE ratios
# TODO add alternative weighting scheme
