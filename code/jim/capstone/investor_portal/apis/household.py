from .economy import Economy


class Household:
    def __init__(self, investable_assets, portfolio_income, other_income, transitionary_phase, transitionary_length, transitionary_income, retirement_income, assets_sell, assets_sell_value, assets_buy, assets_buy_value, annual_expenses, retirement_lifestyle, long_term_care_include, potential_returns) -> None:
        self.investable_assets = investable_assets
        self.portfolio_income = portfolio_income
        self.other_income = other_income
        self.transitionary_phase = transitionary_phase
        self.transitionary_length = transitionary_length
        self.transitionary_income = transitionary_income
        self.retirement_income = retirement_income
        self.assets_sell = assets_sell
        self.assets_sell_value = assets_sell_value
        self.assets_buy = assets_buy
        self.assets_buy_value = assets_buy_value
        self.annual_expenses = annual_expenses
        self.retirement_lifestyle = retirement_lifestyle
        self.long_term_care_include = long_term_care_include
        self.potential_returns = potential_returns
        pass

    def total_other_income(self):
        return self.portfolio_income + self.other_income

    def real_rate(self, econ: Economy):
        return (1 + self.potential_returns) / (1 + econ.inflation_rate) - 1


if __name__ == '__main__':
    pass
