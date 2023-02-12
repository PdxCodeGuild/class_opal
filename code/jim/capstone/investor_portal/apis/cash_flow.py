from pathlib import Path
import numpy as np
from matplotlib import pyplot as plt
import seaborn

from .household import Household
from .economy import Economy
from .user import User


def get_cash_flow(dob, earned_income, age_stop, has_spouse, spouse_dob, spouse_earned_income, spouse_age_stop, investable_assets, portfolio_income, other_income, transitionary_phase, transitionary_length, transitionary_income, retirement_income, assets_sell, assets_sell_value, assets_buy, assets_buy_value, annual_expenses, retirement_lifestyle, long_term_care_include, potential_returns):
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
        investable_assets=investable_assets,
        portfolio_income=portfolio_income,
        other_income=other_income,
        transitionary_phase=transitionary_phase,
        transitionary_length=transitionary_length,
        transitionary_income=transitionary_income,
        retirement_income=retirement_income,
        assets_sell=assets_sell,
        assets_sell_value=assets_sell_value,
        assets_buy=assets_buy,
        assets_buy_value=assets_buy_value,
        annual_expenses=annual_expenses,
        retirement_lifestyle=retirement_lifestyle,
        long_term_care_include=long_term_care_include,
        potential_returns=potential_returns
    )

    user = User(
        first_name='Emma',
        last_name='Shelton',
        dob=dob,
        earned_income=earned_income,
        age_stop=age_stop,
        has_spouse=has_spouse,
        spouse_first_name='Ron',
        spouse_last_name='Shelton',
        spouse_dob=spouse_dob,
        spouse_earned_income=spouse_earned_income,
        spouse_age_stop=spouse_age_stop
    )

    # TODO add features to chart including legend and callout for zero hh funds ages
    # Plot portfolio value, inflows and outflows series over time.

    dpi = 72
    width = 1000
    height = 500
    plt.figure(figsize=(width/dpi, height/dpi), dpi=dpi)
    x = np.arange(user.get_age(user.dob), econ.max_age)
    plt.style.use("seaborn")
    plt.title("Cash Flow Forecast")
    plt.xlabel("Your Age")
    plt.ylabel("Total Cash (in Millions $)")
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

    filepath = Path(__file__).parent / "data"
    plt.savefig(filepath / "cash_flow_chart.svg")


if __name__ == '__main__':
    pass
