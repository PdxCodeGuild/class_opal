import sys
sys.path.insert(0, 'code/nick/python/')
from lab12 import ATM  # nopep8


def test_atm_creation():
    '''
    test instantiation of ATM class
    attributes are balance and transaction history
    balance is dictated, transactions start as empty list
    account cannot be created as or withrawn to negative, will default to 0 if attempted
    '''
    atm_0 = ATM(0)
    assert atm_0.balance == 0
    assert atm_0.transactions == []
    atm_0 = ATM(123.98)
    assert atm_0.balance == 123.98
    assert atm_0.transactions == []
    atm_0 = ATM(-5476.98)
    assert atm_0.balance == 0
    assert atm_0.transactions == []


def test_check_balance():
    '''
    test that check_balance() returns correct balance
    account cannot be created as or withrawn to negative, will default to 0 if attempted
    '''
    atm_1 = ATM(0)
    assert atm_1.check_balance() == 0
    atm_1 = ATM(1234)
    assert atm_1.check_balance() == 1234
    atm_1 = ATM(-145.98)
    assert atm_1.check_balance() == 0


def test_deposit():
    '''
    test that deposit() changes balance and transactions accordingly
    takes absolute value of amount entered in case of mistake
    '''
    atm_2 = ATM(0)
    atm_2.deposit(1000)
    assert atm_2.balance == 1000
    atm_2.deposit(2500)
    assert atm_2.balance == 3500
    atm_2.deposit(-500.79)
    assert atm_2.balance == 4000.79


def test_check_withdrawal():
    '''
    test that check_withdrawal() returns True if amount is <= balance, False if not
    takes absolute value of amount entered in case of mistake
    '''
    atm_3 = ATM(100)
    assert atm_3.check_withdrawal(99.98)
    assert atm_3.check_withdrawal(100)
    assert not atm_3.check_withdrawal(-101.87)


def test_withdraw():
    '''
    test that withdraw() changes balance and transactions accordingly
    takes absolute value of amount entered in case of mistake
    '''
    atm_4 = ATM(5000)
    atm_4.withdraw(1000)
    assert atm_4.balance == 4000
    atm_4.withdraw(2500)
    assert atm_4.balance == 1500
    atm_4.withdraw(-987.36)
    assert atm_4.balance == 512.64


def test_calc_interest():
    '''
    test that interest returns .1% interest of balance
    account cannot be created as or withrawn to negative, so no negative interest
    '''
    atm_5 = ATM(1000)
    assert atm_5.calc_interest() == 1
    atm_5 = ATM(500)
    assert atm_5.calc_interest() == .5
    atm_5 = ATM(-500)
    assert atm_5.calc_interest() == 0
