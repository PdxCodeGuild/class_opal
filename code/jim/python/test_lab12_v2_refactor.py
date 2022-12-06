from unittest.mock import patch

from lab12_v2_refactor import ATM

atm = ATM()


@patch('builtins.input')
def test_operate_atm(mock_input):
    mock_input.return_value = 'exit'
    assert atm.check_balance() == 0


def test_check_balance():
    atm = ATM()
    assert atm.check_balance() == 0
    atm.deposit(100)
    assert atm.check_balance() == 100


def test_deposit():
    atm = ATM()
    atm.deposit(50)
    assert atm.check_balance() == 50

    atm = ATM()
    atm.deposit(-100)
    assert atm.check_balance() == -100


def test_check_withdrawal():
    atm = ATM()
    assert atm.check_withdrawal(-100) == True

    amount = 50
    assert atm.check_withdrawal(amount) == None
    atm.deposit(amount)
    assert atm.check_withdrawal(amount) == True


def test_withdraw():
    atm = ATM()
    atm.withdraw(-100)
    assert atm.balance == 100

    atm = ATM()
    atm.withdraw(50)
    assert atm.balance == -50

    atm = ATM(balance=100)
    atm.withdraw(50)
    assert atm.balance == 50


def test_calc_interest():
    atm = ATM(balance=100, interest_rate=0.07)
    assert round(atm.calc_interest()) == 7

    atm = ATM(balance=-100)
    assert atm.calc_interest() == -100 * 0.001


def test_print_transactions():
    atm = ATM(transactions=[], balance=0.0)
    atm.deposit(100)
    assert type(atm.transactions) == list
    atm.withdraw(50)
    assert atm.transactions == [
        "user deposited $100", "user withdrew $50"]

    atm.deposit(12)
    assert len(atm.print_transactions()) == 3
