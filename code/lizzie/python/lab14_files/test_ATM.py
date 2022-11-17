# Lab 14: Test ATM
from ATM import ATM

def test_check_balance():
    atm = ATM()
    #instantiating instance of class
    assert atm.balance == 0
    assert atm.check_balance() == 0
    assert type(atm.balance) is float


def test_deposit():
    atm = ATM()
    atm.deposit(10)
    assert atm.balance == 10
    
    atm = ATM()
    atm.deposit(0)
    assert atm.balance == 0


def test_check_withdrawal():
    atm = ATM()
    amount = 0
    assert atm.check_withdrawal(amount) is True

    amount = -10
    assert atm.check_withdrawal(amount) is True

    amount = 100_000
    assert atm.check_withdrawal(amount) is None
    atm.deposit(100_001)
    assert atm.check_withdrawal(amount) is True


def test_withdraw():
    atm = ATM()
    atm.withdraw(10)
    assert atm.balance == -10
    
    atm = ATM()
    atm.withdraw(0)
    assert atm.balance == 0

    atm.deposit(100_001)
    atm.withdraw(1)
    assert atm.balance == 100_000


def test_calc_interest():
    atm = ATM()
    assert atm.interest_rate == 0.1
    assert atm.balance + atm.interest_rate *1 == 0.1


def test_print_transactions():
    #refactored code in ATM.py so the atm_list is in the class ATM,
    #thus making it possible to access for the print_transactions function.
    atm = ATM()
    assert type(atm.print_transactions()) is list
    atm.withdraw(1)
    assert atm.atm_list == [f"User withdrew $1"]
