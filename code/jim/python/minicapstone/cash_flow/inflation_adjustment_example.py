"""
PDX Code Guild Python Minicapstone - James Brennan - 2022.11.28 
This module demonstrates an alternative method for handling
inflation in the model, where the income and expense series are
first calculated ignoring inflation, and then the 
inflation-adjusted versions are produced.
"""

# scenario for testing
MAX_AGE = 150
SOCIAL_SECURITY_AGE = 62
dob = '19661231'
spouse = 'Yes'
spouse_dob = '19681231'
age_stop = 65
earned_income = 180_000
spouse_age_stop = 67
spouse_earned_income = 110_000
investable_assets = 1_500_000
portfolio_income = 15_000
other_income = 50_000
transitionary_phase = 'Yes'
transitionary_length = 4
transitionary_income = 200_000
retirement_income = 100_000
assets_sell = 'Yes'
asset_sell_value = 1_250_000
assets_buy = 'Yes'
asset_buy_value = 850_000
annual_expenses = 200_000
retirement_lifestyle = 'More expensive'
long_term_care_include = 'Yes'
age = 55

# define model parameters like inflation and portfolio returns
inflation_rate = 0.02
potential_returns = 0.04

accumulation_phase_length = age_stop - age
full_retirment_age = age_stop + transitionary_length


primary_earned_income_stream = []
for t in range(MAX_AGE - age):
    income = 0
    if age + t < age_stop:
        income = (1 + inflation_rate) ** t * earned_income
    elif age + t < full_retirment_age:
        income = (1 + inflation_rate) ** t * transitionary_income
    primary_earned_income_stream.append(income)


print(primary_earned_income_stream)

primary_earned_income_stream = []
for t in range(MAX_AGE - age):
    income = 0
    if age + t < age_stop:
        income = earned_income
    elif age + t < full_retirment_age:
        income = transitionary_income
    primary_earned_income_stream.append(income)

print(primary_earned_income_stream)


def inflation_adjustment(income_stream: list, inflation_rate: float) -> list:
    inflation_adjusted_income_stream = []
    for t in range(len(income_stream)):
        inflation_adjustment = (1 + inflation_rate) ** t * income_stream[t]
        inflation_adjusted_income_stream.append(inflation_adjustment)
    return inflation_adjusted_income_stream


print(inflation_adjustment(primary_earned_income_stream, inflation_rate))
