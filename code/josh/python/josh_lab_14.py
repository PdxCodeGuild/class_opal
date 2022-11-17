# Lab 14: Automated Tests - Peaks and Valleys, ARI, ATM

# Each functions tests should have multiple assertions. Test all of the edge cases you can think of, keeping assertions small.
# For example, in peaks_and_valleys you might test [1, 2, 3, 2] and [3, 2, 3, 2] instead of long lists.

########## PEAKS AND VALLEYS ##########
from josh_lab_8 import peaks_and_valleys


def test_peaks_and_valleys():
    peaks = [6, 14]
    valleys = [9, 17]
    assert peaks[0] != valleys[0]
    assert peaks[1] != valleys[1]

   
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
# from josh_lab_12 import ATM

# def test_check_balance:
# def test_deposit:
# def test_check_withdrawal:
# def test_withdraw:
# def test_calc_interest:
# def test_print_transactions:


# If you need to refactor your code to make it more testable, include the refactored code in your pull request.
# To run pytest enter the following: 'python -m pytest josh_lab_14.py'