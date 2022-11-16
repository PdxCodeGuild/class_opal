# Lab 14: Test ATM
from ATM import ATM


balance = 0
deposit = 10.0
interest_rate = 0.1
amount = 100


def test_check_balance():
    assert balance is 0
    assert balance + deposit == 10.0


def test_deposit():
    pass


def test_check_withdrawal():
    assert check_withdrawal(amount) is False
    pass


def test_withdraw():
    pass


def test_calc_interest():
    pass