"""
PDX Code Guild Python Minicapstone - James Brennan - 2022.11.28 
A simple model of a user for cash flow and retirement planning
including methods for calculation income and expense flows for
the entire work and retirement horizon.
"""
import numpy as np
import numpy_financial as npf

from .economy import Economy
from .household import Household


class User:
    """A simple model of a user with a cash flow plan for work and retirement."""

    def __init__(self, first_name, last_name, dob: str, earned_income: int, age_stop: int, has_spouse: bool, spouse_first_name, spouse_last_name, spouse_dob, spouse_earned_income, spouse_age_stop) -> None:
        """Initialize user attributes."""
        self.first_name = first_name
        self.last_name = last_name
        self.dob = dob
        self.earned_income = earned_income
        self.age_stop = age_stop
        self.has_spouse = has_spouse
        self.spouse_first_name = spouse_first_name
        self.spouse_last_name = spouse_last_name
        self.spouse_dob = spouse_dob
        self.spouse_earned_income = spouse_earned_income
        self.spouse_age_stop = spouse_age_stop

    def get_age(self, dob):
        """Gets age today (in years) from a given date of birth"""
        from datetime import datetime, date
        today = date.today()
        birth_date = datetime.strptime(dob, '%Y%m%d').date()
        age = today.year - birth_date.year -\
            ((today.month, today.day) <
             (birth_date.month, birth_date.day))
        return age

    def accumulation_phase_length(self):
        """Length of time in years from current age until the user stops working full-time."""
        return self.age_stop - self.get_age(self.dob)

    def full_retirement_age(self, household: Household):
        return self.age_stop + household.transitionary_length

    def primary_earned_income_stream(self, econ: Economy, household: Household):
        """Series of earned income by year for primary user"""
        age = self.get_age(self.dob)
        primary_earned_income_stream = []
        for t in range(econ.max_age - age):
            income = 0
            if age + t < self.age_stop:
                income = (1 + econ.inflation_rate) ** t * self.earned_income
            elif age + t < self.full_retirement_age(household):
                income = (1 + econ.inflation_rate) ** t * \
                    household.transitionary_income
            primary_earned_income_stream.append(income)
        return np.array(primary_earned_income_stream)

    def spouse_earned_income_stream(self, econ: Economy, household: Household):
        """Series of earned income by year for spouse"""
        spouse_earned_income_stream = []
        age = self.get_age(self.dob)
        for t in range(econ.max_age - age):
            income = 0
            if household.transitionary_phase == 'No':
                if age + t < self.full_retirement_age(household):
                    income = (1 + econ.inflation_rate) ** t * \
                        self.spouse_earned_income
            elif t < self.accumulation_phase_length():
                income = (1 + econ.inflation_rate) ** t * \
                    self.spouse_earned_income
            spouse_earned_income_stream.append(income)
        return np.array(spouse_earned_income_stream)

    def other_income_stream(self, econ: Economy, household: Household):
        """Series of other household income such as rental income and portfolio dividends"""
        other_income_stream = []
        age = self.get_age(self.dob)
        for t in range(econ.max_age - age):
            income = (1 + econ.inflation_rate) ** t * \
                household.total_other_income()
            other_income_stream.append(income)
        return np.array(other_income_stream)

    def retirement_income_stream(self, econ: Economy, household: Household):
        """Series of household retirement income from pensions, social security, etc."""
        retirement_income_stream = []
        age = self.get_age(self.dob)
        for t in range(econ.max_age - age):
            income = 0
            if age + t >= econ.social_security_age and t >= self.accumulation_phase_length() + household.transitionary_length:
                income = (1 + econ.inflation_rate) ** t * \
                    household.retirement_income
            retirement_income_stream.append(income)
        return np.array(retirement_income_stream)

    def asset_sales_series(self, econ: Economy, household: Household):
        """Series of sales of major household assets, for simplicity assumed to occur at retirement."""
        asset_sales_series = []
        age = self.get_age(self.dob)
        for t in range(econ.max_age - age):
            income = 0
            if household.assets_sell == 'Yes' and t == self.accumulation_phase_length() + household.transitionary_length:
                income = (1 + econ.inflation_rate) ** t * \
                    household.assets_sell_value
            asset_sales_series.append(income)
        return np.array(asset_sales_series)

    def asset_buy_series(self, econ: Economy, household: Household):
        """Series of purchases of major household assets, for simplicity assumed to occur at retirement."""
        asset_buy_series = []
        age = self.get_age(self.dob)
        for t in range(econ.max_age - age):
            asset_expense = 0
            if household.assets_buy == 'Yes' and t == self.accumulation_phase_length() + household.transitionary_length:
                asset_expense = (1 + econ.inflation_rate) ** t * \
                    household.assets_buy_value
            asset_buy_series.append(asset_expense)
        return np.array(asset_buy_series)

    def annual_expense_stream(self, econ: Economy, household: Household):
        """Household expenses by year, with adjustment for retirement, not including long term care costs."""
        annual_expenses_stream = []
        age = self.get_age(self.dob)
        for t in range(econ.max_age - age):
            expense = 0
            if t < self.accumulation_phase_length():
                expense = (1 + econ.inflation_rate) ** t * \
                    household.annual_expenses
            else:
                expense = (1 + econ.inflation_rate) ** t * \
                    econ.retirement_expense_modifiers[household.retirement_lifestyle] * \
                    household.annual_expenses
            annual_expenses_stream.append(expense)
        return np.array(annual_expenses_stream)

    def get_inflows_stream(self, econ: Economy, household: Household):
        """sum of all streams of income for the household"""
        return self.primary_earned_income_stream(econ, household) + \
            self.spouse_earned_income_stream(econ, household) + \
            self.other_income_stream(econ, household) + \
            self.retirement_income_stream(econ, household) + \
            self.asset_sales_series(econ, household)

    def get_outflows_stream(self, econ: Economy, household: Household):
        """sum of all expense streams for the household"""
        return self.annual_expense_stream(econ, household) + \
            self.asset_buy_series(econ, household)

    def net_contribution_stream(self, econ: Economy, household: Household):
        """difference between household inflow and outflow streams"""
        return self.get_inflows_stream(econ, household) - \
            self.get_outflows_stream(econ, household)

    def portfolio_value_series(self, econ: Economy, household: Household):
        """Series of time t portfolio values with no long term care costs"""
        real_rate = household.real_rate(econ)
        net_contribution_stream = self.net_contribution_stream(econ, household)

        portfolio_value_series = [household.investable_assets]
        age = self.get_age(self.dob)
        for t in range(1, econ.max_age - age):
            portfolio_value = max(-npf.fv(real_rate, 1,
                                  net_contribution_stream[t-1], portfolio_value_series[t - 1], 1), 0)
            portfolio_value_series.append(portfolio_value)
        return np.array(portfolio_value_series)

    def long_term_care_cost_series(self, econ: Economy, household: Household):
        """series of time t inflation adjusted long term care costs"""
        long_term_care_cost_series = []
        age = self.get_age(self.dob)
        for t in range(econ.max_age - age):
            if household.long_term_care_include == 'Yes':
                long_term_care_cost = (1 + econ.inflation_rate) ** t * \
                    econ.annual_long_term_care_costs
            else:
                long_term_care_cost = 0
            long_term_care_cost_series.append(long_term_care_cost)
        return np.array(long_term_care_cost_series)

    def portfolio_value_series_ltc1(self, econ: Economy, household: Household):
        """An intermediate adjustment to portfolio value for one period of ltc costs."""
        portfolio_value_series = self.portfolio_value_series(econ, household)
        real_rate = household.real_rate(econ)
        net_contribution_stream = self.net_contribution_stream(econ, household)
        long_term_care_cost_series = self.long_term_care_cost_series(
            econ, household)

        portfolio_value_series_ltc1 = [portfolio_value_series[0]]
        age = self.get_age(self.dob)
        for t in range(1, econ.max_age - age):
            portfolio_value = max(-npf.fv(real_rate, 1,
                                          net_contribution_stream[t - 1] -
                                          long_term_care_cost_series[t - 1], portfolio_value_series[t - 1], 1), 0)
            portfolio_value_series_ltc1.append(portfolio_value)

        # Two other calculcation methods below.
        # portfolio_value_series_ltc1 = max(-npf.fv(real_rate, 1, net_contribution_stream -
        #                                   long_term_care_cost_series, portfolio_value_series, 1), 0)
        # portfolio_value_series_ltc1 = np.where(portfolio_value_series_ltc1 < 0, 0, portfolio_value_series_ltc1)
        # portfolio_value_series_ltc1 = np.insert(portfolio_value_series_ltc1, 0, household.investable_assets)
        # portfolio_value_series_ltc1 = portfolio_value_series_ltc1[:len(portfolio_value_series_ltc1)-1]

        # portfolio_value_series_ltc1 = [
        #     self.portfolio_value_series(econ, household)[0]]
        # age = self.get_age(self.dob)
        # for t in range(1, econ.max_age - age):
        #     portfolio_value = max(-npf.fv(household.real_rate(econ), 1,
        #                                   self.net_contribution_stream(econ, household)[t - 1] -
        #                                   self.long_term_care_cost_series(
        #                                       econ, household)[t - 1],
        #                                   self.portfolio_value_series(econ, household)[t - 1], 1), 0)
        #     portfolio_value_series_ltc1.append(portfolio_value)
        return portfolio_value_series_ltc1

    def portfolio_value_series_ltc2(self, econ: Economy, household: Household):
        """An intermediate adjustment to portfolio value for two periods of ltc costs."""
        portfolio_value_series = self.portfolio_value_series(econ, household)
        real_rate = household.real_rate(econ)
        net_contribution_stream = self.net_contribution_stream(econ, household)
        long_term_care_cost_series = self.long_term_care_cost_series(
            econ, household)
        portfolio_value_series_ltc1 = self.portfolio_value_series_ltc1(
            econ, household)

        portfolio_value_series_ltc2 = list(portfolio_value_series[0:2])
        age = self.get_age(self.dob)
        for t in range(2, econ.max_age - age):
            portfolio_value = max(-npf.fv(real_rate, 1,
                                          net_contribution_stream[t - 1] -
                                          long_term_care_cost_series[t - 1], portfolio_value_series_ltc1[t - 1], 1), 0)
            portfolio_value_series_ltc2.append(portfolio_value)
        return portfolio_value_series_ltc2

    def portfolio_value_series_ltc3(self, econ: Economy, household: Household):
        """An intermediate adjustment to portfolio value for three periods of ltc costs."""
        portfolio_value_series = self.portfolio_value_series(econ, household)
        real_rate = household.real_rate(econ)
        net_contribution_stream = self.net_contribution_stream(econ, household)
        long_term_care_cost_series = self.long_term_care_cost_series(
            econ, household)
        portfolio_value_series_ltc2 = self.portfolio_value_series_ltc2(
            econ, household)

        portfolio_value_series_ltc3 = list(portfolio_value_series[0:3])
        age = self.get_age(self.dob)
        for t in range(3, econ.max_age - age):
            portfolio_value = max(-npf.fv(real_rate, 1,
                                          net_contribution_stream[t - 1] -
                                          long_term_care_cost_series[t - 1], portfolio_value_series_ltc2[t - 1], 1), 0)
            portfolio_value_series_ltc3.append(portfolio_value)
        return portfolio_value_series_ltc3

    def portfolio_value_series_ltc(self, econ: Economy, household: Household):
        """Series of portfolio values with long term care costs assessed in final three years of portfolio value."""
        portfolio_value_series_ltc = []
        age = self.get_age(self.dob)
        portfolio_value_series = self.portfolio_value_series(econ, household)
        portfolio_value_series_ltc1 = self.portfolio_value_series_ltc1(
            econ, household)
        portfolio_value_series_ltc2 = self.portfolio_value_series_ltc2(
            econ, household)
        portfolio_value_series_ltc3 = self.portfolio_value_series_ltc3(
            econ, household)

        for t in range(econ.max_age - age):
            if portfolio_value_series_ltc3[t] == 0:
                portfolio_value = 0
            elif portfolio_value_series_ltc3[t + 1] == 0:
                portfolio_value = portfolio_value_series_ltc2[t]
            elif portfolio_value_series_ltc3[t + 2] == 0:
                portfolio_value = portfolio_value_series_ltc1[t]
            else:
                portfolio_value = portfolio_value_series[t]
            portfolio_value_series_ltc.append(portfolio_value)
        return np.array(portfolio_value_series_ltc)

    def zero_hh_funds_age(self, econ: Economy, household: Household):
        """Calculates user and spouse ages in period where portfolio value equals zero"""
        try:
            years_until_zero_funds = list(self.portfolio_value_series_ltc(
                econ, household)).index(0)
            primary_age_zero_funds = self.get_age(
                self.dob) + years_until_zero_funds
            spouse_age_zero_funds = self.get_age(
                self.spouse_dob) + years_until_zero_funds
        except ValueError:
            primary_age_zero_funds = f"> {econ.max_age}"
            spouse_age_zero_funds = f"> {econ.max_age}"

        return primary_age_zero_funds, spouse_age_zero_funds


if __name__ == '__main__':
    pass
