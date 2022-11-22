import lab12
import pytest
from lab12 import ATM


test_atm = ATM()


def test_atm_creation():
    assert test_atm.balance == 0
    assert test_atm.interest_rate == 0.001


def test_check_balance():
    balance = test_atm.check_balance()
    assert balance == 0
    test_atm2 = ATM(balance=250)
    balance = test_atm2.check_balance()
    assert balance == 250
    test_atm3 = ATM(balance=500)
    balance = test_atm3.check_balance()
    assert balance == 500


def test_deposit():
    test_atm = ATM()
    test_atm.deposit(20)
    assert test_atm.balance == 20
    test_atm.deposit(10)
    assert test_atm.balance == 30
    test_atm.deposit(250)
    assert test_atm.balance == 280


def test_withdraw():
    test_atm = ATM(balance=100)
    test_atm.withdraw(10)
    assert test_atm.balance == 90
    test_atm.withdraw(20)
    assert test_atm.balance == 70
    test_atm.withdraw(50)
    assert test_atm.balance == 20


def test_check_withdrawal():
    test_atm = ATM(balance=100)
    assert test_atm.check_withdrawal(250) == False
    test_atm = ATM(balance=100)
    assert test_atm.check_withdrawal(80) == True
    test_atm = ATM(balance=100)
    assert test_atm.check_withdrawal(1000) == False


def test_calc_interest():
    test_atm = ATM(balance=250)
    assert test_atm.calc_interest() == 0.25
    test_atm = ATM(balance=100)
    assert test_atm.calc_interest() == 0.1
    test_atm = ATM(balance=0)
    assert test_atm.calc_interest() == 0
