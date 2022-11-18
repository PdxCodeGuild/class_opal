# Lab 14: Automated Tests - Peaks and Valleys, ARI, ATM

# Each function's tests should have multiple assertions. Test all of the edge cases you can think of, keeping assertions small.

########## PEAKS AND VALLEYS ##########
from josh_lab_8 import peaks_and_valleys
# Do I have to import unittest.mock, patch, and pytest?
# Do I have to copy and paste 'data_dict' to test function with program code that is outside of the function?


def test_peaks_and_valleys():
# def test_peaks_and_valleys(data_dict):    # Use if I copy/paste 'data_dict'
    peaks = [6, 14]
    valleys = [9, 17]
    assert peaks[0] != valleys[0]
    assert peaks[1] != valleys[1]
    for peak, valley in peaks, valleys:
        assert peak, valley == int
        assert peak, valley == list
        assert peak != valley
        assert valley != peak
        # assert data[key] == data[key + 2]   # Use if I copy/paste 'data_dict'
 
   
# # Creates a function to return a list of the peaks and valleys in order of appearance in the original data
# def peaks_and_valleys(data):
#     peaks_and_valleys_list = []
#     for key in data:
#         try:
#             if data[key] == data[key + 2]:
#                 peaks_and_valleys_list.append(key + 1)   
#         except:
#             break    
#     print(peaks_and_valleys_list)


# peaks_and_valleys(data_dict)


########## AUTOMATED READABILITY INDEX ##########
# from josh_lab_9 import ???


########## AUTOMATED TELLER MACHINE ##########
from josh_lab_12 import ATM

atm = ATM()


def test_check_balance():
    assert atm.check_balance() == 0
    atm.deposit(1000)
    assert atm.check_balance() == 1000
    atm.withdraw(900)
    assert atm.check_balance() == 100
    atm.calc_interest()
    assert atm.check_balance == 100.1


def test_deposit():
    assert atm.check_balance() == 0
    atm.deposit(1000)
    assert atm.check_balance() == atm.deposit() + atm.check_balance()


def test_check_withdrawal():
    assert atm.check_balance() == 100
    atm.withdraw(99)
    assert atm.check_withdrawal() == True
    assert atm.check_balance() == 1
    atm.withdraw(2)
    assert atm.check_withdrawal() == False


def test_withdraw():
    assert atm.check_balance() == 1000
    atm.withdraw(500)
    assert atm.check_balance() == 500
    atm.deposit(100)
    atm.withdraw(500)
    assert atm.check_balance() == 100


def test_calc_interest():
    assert atm.check_balance() == 100
    atm.calc_interest()
    assert atm.check_balance() == 100.1
    atm.calc_interest()
    assert round(atm.check_balance(), 1) == 100.2


# def test_print_transactions():

# If you need to refactor your code to make it more testable, include the refactored code in your pull request.
# To run pytest enter the following: 'python -m pytest josh_lab_14.py'