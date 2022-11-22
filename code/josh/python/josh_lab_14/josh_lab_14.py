# Lab 14: Automated Tests - Peaks and Valleys, ARI, ATM

# Each function's tests should have multiple assertions. Test all of the edge cases you can think of, keeping assertions small.

########## PEAKS AND VALLEYS ##########
from refactor_josh_lab_8 import peaks_and_valleys


def test_peaks_and_valleys():
    data = [3, 4, 3, 2]
    assert peaks_and_valleys(data) == [1]
    data = [6, 5, 6, 7]
    assert peaks_and_valleys(data) == [1]
    data = [1, 2, 3, 4, 3, 2, 3, 4, 5, 6, 7, 6, 5]
    assert peaks_and_valleys(data) == [3, 5, 10]


########## AUTOMATED READABILITY INDEX ##########
from refactor_josh_lab_9 import sentences


def test_sentences():
    statements = 'This is a statement.'
    questions = 'Is this a question?'
    exclamations = 'What an exclamation!'
    assert sentences() == 3
    statements = 'This is statement 1. This is statement 2.'
    assert sentences() == 4
    questions = 'What is a test?  How do I test?'
    exclamations = 'How happy I am to finish the tests!!!'
    assert sentences() == 7


########## AUTOMATED TELLER MACHINE ##########
from refactor_josh_lab12 import ATM

atm = ATM()


def test_check_balance():
    assert atm.check_balance() == 0
    atm.deposit(1000)
    assert atm.check_balance() == 1000
    atm.withdraw(900)
    assert atm.check_balance() == 100
 

def test_deposit():
    atm.deposit(1000)
    assert atm.check_balance() == 1100
    atm.deposit(400)
    assert atm.check_balance() == 1500


def test_check_withdrawal():
    atm.withdraw(1499)
    assert atm.check_withdrawal(1) == True
    assert atm.check_balance() == 1
    atm.withdraw(2)
    assert atm.check_withdrawal(-1) >= 0


def test_withdraw():
    atm.deposit(1001)
    atm.withdraw(500)
    assert atm.check_balance() == 500
    atm.deposit(100)
    atm.withdraw(500)
    assert atm.check_balance() == 100


def test_calc_interest():
    assert atm.calc_interest() == 100.1
    atm.deposit(100)
    assert atm.calc_interest() == 200.2
    

def test_print_transactions():
    assert atm.print_transactions('') == ''
    assert atm.print_transactions('Transactions') != ''
    assert atm.print_transactions('Transactions') == 'Transactions'