# Python Mini-Capstone

# Your program needs to utilize an external library.  The functionality of the program is up to you.

# 0930 and 1330 Stand Ups to answer 3 questions:
    # What did you do in your last session?
    # What will you do in this session?
    # What roadblock do you have, if any?

# 5-minute (roughly) Presentations:
    # A demo of your project
    # A look at the code
    # Time for questions
    # There is more info on presentations in the README

######################################################################################################################################################
######################################################################################################################################################

import requests
import pandas as pd
# import json
from pprint import pprint
from bs4 import BeautifulSoup
from urllib.request import urlopen

# response = requests.get('https://taxfoundation.org/tax-burden-by-state-2022/#results')
# response = requests.get('https://files.taxfoundation.org/20220407173521/State-and-Local-Tax-Burdens-2022..pdf')
# response_text = response.json()
# pprint(response_text)
# author  = response_text['quote']['author']
# quote = response_text['quote']['body']


# Opens first website 'Tax Foundation' to webscrape effective tax burdens
with urlopen('https://taxfoundation.org/tax-burden-by-state-2022/#results') as response:
    soup_tax = BeautifulSoup(response, 'html.parser')

# Opens second website '???' to webscrape political leanings
with urlopen('https://taxfoundation.org/tax-burden-by-state-2022/#results') as response:
    soup_tax = BeautifulSoup(response, 'html.parser')

# Opens third website '???' to webscrape crime rates
with urlopen('https://taxfoundation.org/tax-burden-by-state-2022/#results') as response:
    soup_tax = BeautifulSoup(response, 'html.parser')

# Opens fourth website '???' to webscrape median housing values
with urlopen('https://taxfoundation.org/tax-burden-by-state-2022/#results') as response:
    soup_tax = BeautifulSoup(response, 'html.parser')


# Returns state, tax_rate, and data based upon user input for either state or rank
def tax_burden(user_input):
    for row in soup_tax.table.contents[5].find_all('tr'):
        state = row.contents[1].string
        tax_rate = row.contents[3].string
        rank = row.contents[5].string
        if user_input == state:
            return f'State: {state}, Effective Tax Burden: {tax_rate}, Rank: {rank}'
        elif user_input == rank:
            return f'State: {state}, Effective Tax Burden: {tax_rate}, Rank: {rank}'


##### Will likely remove later, if not used #####
state_rank = {
    '20': 'Alabama 9.8%', 
    '1': 'Alaska 4.6%',
    '15': 'Arizona 9.5%',
    '26': 'Arkansas 10.2%',
    '46': 'California 13.5%',
    '19': 'Colorado 9.7%',
    '49': 'Connecticut 15.4%',
    '42': 'Delaware 12.4%',
    '11': 'Florida 9.1%',
    '8': 'Georgia 8.9%',
    '48': 'Hawaii 14.1%',
    '29': 'Idaho 10.7%',
    '44': 'Illinois 12.9%',
    '14': 'Indiana 9.3%',
    '34': 'Iowa 11.2%',
    '33': 'Kansas 11.2%',
    '17': 'Kentucky 9.6%',
    '12': 'Louisiana 9.1%',
    '41': 'Maine 12.4%',
    '35': 'Maryland 11.3%',
    '37': 'Massachusetts 11.5%',
    '5': 'Michigan 8.6%',
    '39': 'Minnesota 12.1%',
    '21': 'Mississippi 9.8%',
    '13': 'Missouri 9.3%',
    '27': 'Montana 10.5%',
    '38': 'Nebraska 11.5%',
    '18': 'Nevada 9.6%',
    '16': 'New Hampshire 9.6%',
    '45': 'New Jersey 13.2%',
    '25': 'New Mexico 10.2%',
    '50': 'New York 15.9%',
    '23': 'North Carolina 9.9%',
    '7': 'North Dakota 8.8%',
    '24': 'Ohio 10.0%',
    '10': 'Oklahoma 9.0%',
    '31': 'Oregon 10.8%',
    '28': 'Pennsylvania 10.6%',
    '36': 'Rhode Island 11.4%',
    '9': 'South Carolina 8.9%',
    '4': 'South Dakota 8.4%',
    '3': 'Tennessee 7.6%',
    '6': 'Texas 8.6%',
    '40': 'Utah 12.1%',
    '47': 'Vermont 13.6%',
    '43': 'Virginia 12.5%',
    '30': 'Washington 10.7%',
    '22': 'West Virginia 9.8%',
    '32': 'Wisconsin 10.9%',
    '2': 'Wyoming 7.5%'
}

while True:
    state_choice = input('Enter a state name or rank to view the state\'s effective tax burden or \'q\' to continue to the next section: ')
    if state_choice == 'q':
        break
    elif tax_burden(state_choice) == None:
        print('You have entered an invalid response.')
    else:
        print(tax_burden(state_choice))
    another_state = input('Would you like to view another state? Enter \'y\' for yes or \'n\' for no: ')
    if another_state == 'y':
        pass
    elif another_state == 'n':
        break
    else:
        print('You have entered an invalid response.')
        continue