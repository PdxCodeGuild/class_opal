import sys
sys.path.insert(0, 'code/nick/python/')
from lab12 import ATM  # nopep8

atm = ATM(0)


def test_atm_creation():
    assert atm.balance == 0
    assert atm.transactions == []


def test_check_balance():
    '''
    test that check_balance() returns correct balance
    '''
    assert atm.check_balance() == 0
    atm_1 = ATM(1234)
    assert atm_1.check_balance() == 1234


def test_deposit():
    '''
    test that deposit() changes balance and transactions accordingly
    '''
    atm_2 = ATM(0)
    atm_2.deposit(1000)
    assert atm_2.balance == 1000
    atm_2.deposit(2500)
    assert atm_2.balance == 3500


def test_check_withdrawal():
    '''
    test that check_withdrawal() returns True if amount is <= balance, False if not
    '''
    atm_3 = ATM(100)
    assert atm_3.check_withdrawal(99)
    assert atm_3.check_withdrawal(100)
    assert not atm_3.check_withdrawal(101)


def test_withdraw():
    '''
    test that withdraw() changes balance and transactions accordingly
    '''
    atm_4 = ATM(5000)
    atm_4.withdraw(1000)
    assert atm_4.balance == 4000
    atm_4.withdraw(2500)
    assert atm_4.balance == 1500


def test_calc_interest():
    '''
    test that interest returns .1% interest of balance
    '''
    atm_5 = ATM(1000)
    assert atm_5.calc_interest() == 1
    atm_5 = ATM(500)
    assert atm_5.calc_interest() == .5
