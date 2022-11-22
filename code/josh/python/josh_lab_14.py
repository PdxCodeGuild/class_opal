# Lab 14: Automated Tests - Peaks and Valleys, ARI, ATM

# Each function's tests should have multiple assertions. Test all of the edge cases you can think of, keeping assertions small.

########## PEAKS AND VALLEYS ##########
from josh_lab_8 import peaks_and_valleys, data
# from unittest.mock import patch

# Do I have to import unittest.mock, patch, and pytest?

# data = [1, 2, 3, 4, 5, 6, 7, 6, 5, 4, 5, 6, 7, 8, 9, 8, 7, 6, 7, 8, 9]

def test_peaks_and_valleys():
    peaks_and_valleys(data) == [6, 9, 14, 17]
    # assert peaks_and_valleys(data) == [6, 9, 14, 17]    
   
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


########## STILL WORKING ON IT ##########
# def test_calc_interest():
#     atm.calc_interest()
#     assert atm.check_balance() == 100.1
#     atm.calc_interest()
#     assert round(atm.check_balance(), 1) == 100.2


# def test_print_transactions():

# If you need to refactor your code to make it more testable, include the refactored code in your pull request.
# To run pytest enter the following: 'python -m pytest josh_lab_14.py'