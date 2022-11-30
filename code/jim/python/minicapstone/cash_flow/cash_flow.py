"""
PDX Code Guild Python Minicapstone - James Brennan - 2022.11.28 
This module returns a cash flow forecast for retirement planning
purposes based on user attribute data.
"""
import time
import numpy as np
from matplotlib import pyplot as plt

from household import Household
from economy import Economy
from user import User

if __name__ == '__main__':
    start_time = time.time()

    # Instantiate economy, household, and user.
    econ = Economy(
        # TODO rewrite model for user.target_age instead of economy.max_age
        max_age=150,
        social_security_age=62,
        inflation_rate=0.02,
        retirement_expense_modifiers={
            'Simpler': 0.9, 'About the same': 1, 'More expensive': 1.1},
        annual_long_term_care_cost=100_000,
        # TODO: generalize user class methods for ltc calcs; currently ltc fixed at 3 years.
        long_term_care_years=3
    )

    household = Household(
        investable_assets=1_500_000,
        portfolio_income=15_000,
        other_income=50_000,
        transitionary_phase='Yes',
        transitionary_length=4,
        transitionary_income=200_000,
        retirement_income=100_000,
        assets_sell='Yes',
        assets_sell_value=1_250_000,
        assets_buy='Yes',
        assets_buy_value=850_000,
        annual_expenses=200_000,
        retirement_lifestyle='More expensive',
        # TODO make portfolio calcs depend on this variable.
        long_term_care_include='Yes',
        potential_returns=0.04
    )

    user = User(
        first_name='Emma',
        last_name='Shelton',
        dob='19661231',
        earned_income=180_000,
        age_stop=65,
        has_spouse='Yes',
        spouse_first_name='Ron',
        spouse_last_name='Shelton',
        spouse_dob='19681231',
        spouse_earned_income=110_000,
        spouse_age_stop=67
    )

    # TODO add features to chart including legend and callout for zero hh funds ages
    # Plot portfolio value, inflows and outflows series over time.
    x = np.arange(user.get_age(user.dob), econ.max_age)
    plt.title("Cash Flow Forecast")
    plt.xlabel("Time")
    plt.ylabel("$")
    plt.plot(x, user.portfolio_value_series_ltc(econ, household),
             label=user.portfolio_value_series_ltc(econ, household), color="blue")
    plt.plot(x, user.primary_earned_income_stream(econ, household),
             label=user.primary_earned_income_stream(econ, household))
    plt.plot(x, user.spouse_earned_income_stream(econ, household),
             label=user.spouse_earned_income_stream(econ, household))
    plt.plot(x, user.other_income_stream(econ, household),
             label=user.other_income_stream(econ, household))
    plt.plot(x, user.retirement_income_stream(econ, household),
             label=user.retirement_income_stream(econ, household))
    plt.plot(x, user.asset_sales_series(econ, household),
             label=user.asset_sales_series(econ, household))
    plt.plot(x, user.asset_buy_series(econ, household),
             label=user.asset_buy_series(econ, household))
    plt.show()

    print("My program took", time.time() - start_time, "to run")
