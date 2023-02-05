class Economy:
    def __init__(self, max_age, social_security_age, inflation_rate, retirement_expense_modifiers, annual_long_term_care_cost, long_term_care_years) -> None:
        self.max_age = max_age
        self.social_security_age = social_security_age
        self.inflation_rate = inflation_rate
        self.retirement_expense_modifiers = retirement_expense_modifiers
        self.annual_long_term_care_costs = annual_long_term_care_cost
        self.long_term_care_years = long_term_care_years
        pass

    def period_t_inflation(self, t):
        return (1 + self.inflation_rate) ** t


if __name__ == '__main__':
    pass
