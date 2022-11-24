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
# pol_rel_path = 'class_opal\code\josh\python\josh_mini_capstone\politics.csv'

# # state, control
# # Opens file at relative path and converts lines into a list of strings
# with open(pol_rel_path, 'r') as file:
#     lines:list = file.read().split('\n')

# states_list = []
# # Creates a list of strings, where each string will be used as a dictionary key from the first line in the file above
# keys: list[str] = lines[0].split(',')  

# # Iterates through the remaining list of strings and converts each string to a dictionary value 
# for line in lines[1:]:
#     state_dict = {}
#     values: list[str] = line.split(',')
#     for i, key in enumerate(keys):
#         state_dict[key] = values[i]
#     states_list.append(state_dict)

# print(states_list)


import requests
import pandas as pd
# import json
from pprint import pprint
from bs4 import BeautifulSoup, SoupStrainer
from urllib.request import urlopen

# state, control
politics= pd.read_csv(r'C:\Users\joshg\pdx_code\class_opal\code\josh\python\josh_mini_capstone\politics.csv')
# state, MedianValue
homes= pd.read_csv(r'C:\Users\joshg\pdx_code\class_opal\code\josh\python\josh_mini_capstone\homes.csv')
# state, rate
crimes= pd.read_csv(r'C:\Users\joshg\pdx_code\class_opal\code\josh\python\josh_mini_capstone\crimes.csv')

print(homes)

# for state in politics:
#     print(state)

def csv(user_input, csv):
    for state in csv:
        if user_input == state:
            return f'State: {state}, Political Affiliation: {csv[user_input]}'
        elif user_input == politics:
            return f'State: {state}, Political Affiliation: {csv[user_input]}'

# print(csv('control', homes))

# response = requests.get('https://taxfoundation.org/tax-burden-by-state-2022/#results')
# response = requests.get('https://files.taxfoundation.org/20220407173521/State-and-Local-Tax-Burdens-2022..pdf')
# response_text = response.json()
# pprint(response_text)
# author  = response_text['quote']['author']
# quote = response_text['quote']['body']


# Opens 1st website to webscrape effective tax burdens
with urlopen('https://taxfoundation.org/tax-burden-by-state-2022/#results') as response:
    soup_tax = BeautifulSoup(response, 'html.parser')

# Opens 2nd website (data from Pew Research Center, Kaiser Family Foundation, et al.) to webscrape political leanings by state
with urlopen('https://worldpopulationreview.com/state-rankings/states-by-political-party') as response:
    soup_politics = BeautifulSoup(response, 'html.parser')

# Opens 3rd website (data from FBI Crime Data Explorer) to webscrape crime rates by state
with urlopen('https://worldpopulationreview.com/state-rankings/crime-rate-by-state') as response:
    soup_crime = BeautifulSoup(response, 'html.parser')

# Opens 4th website (data from Zillow, et al.) to webscrape median housing values by state
with urlopen('https://worldpopulationreview.com/state-rankings/median-home-price-by-state') as response:
    soup_house = BeautifulSoup(response, 'html.parser')


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


# # Returns political affiliation by state based upon user input
# def politics(user_input):
# pprint(soup_politics.contents[2])
# pprint(ts(dictionary.get('fips'))

# pprint(soup_politics.contents(dictionary.get('fips'))
    # print(child)
# print(soup_politics.find_all('tr'))

# print(soup_crime.find("div", {"class": "datatable-container"}))

    
    # soup_politics.contents[1].find_all('class'):
    # print(i)



# # Returns crime rates (violent/property crime) by state based upon user input
# def crime(user_input):
#     for


# # Returns median home values by stae based upon user input
# def home_pricing(user_input):
#     for



# ##### Will likely remove later, if not used #####
# state_rank = {
#     '20': 'Alabama 9.8%', 
#     '1': 'Alaska 4.6%',
#     '15': 'Arizona 9.5%',
#     '26': 'Arkansas 10.2%',
#     '46': 'California 13.5%',
#     '19': 'Colorado 9.7%',
#     '49': 'Connecticut 15.4%',
#     '42': 'Delaware 12.4%',
#     '11': 'Florida 9.1%',
#     '8': 'Georgia 8.9%',
#     '48': 'Hawaii 14.1%',
#     '29': 'Idaho 10.7%',
#     '44': 'Illinois 12.9%',
#     '14': 'Indiana 9.3%',
#     '34': 'Iowa 11.2%',
#     '33': 'Kansas 11.2%',
#     '17': 'Kentucky 9.6%',
#     '12': 'Louisiana 9.1%',
#     '41': 'Maine 12.4%',
#     '35': 'Maryland 11.3%',
#     '37': 'Massachusetts 11.5%',
#     '5': 'Michigan 8.6%',
#     '39': 'Minnesota 12.1%',
#     '21': 'Mississippi 9.8%',
#     '13': 'Missouri 9.3%',
#     '27': 'Montana 10.5%',
#     '38': 'Nebraska 11.5%',
#     '18': 'Nevada 9.6%',
#     '16': 'New Hampshire 9.6%',
#     '45': 'New Jersey 13.2%',
#     '25': 'New Mexico 10.2%',
#     '50': 'New York 15.9%',
#     '23': 'North Carolina 9.9%',
#     '7': 'North Dakota 8.8%',
#     '24': 'Ohio 10.0%',
#     '10': 'Oklahoma 9.0%',
#     '31': 'Oregon 10.8%',
#     '28': 'Pennsylvania 10.6%',
#     '36': 'Rhode Island 11.4%',
#     '9': 'South Carolina 8.9%',
#     '4': 'South Dakota 8.4%',
#     '3': 'Tennessee 7.6%',
#     '6': 'Texas 8.6%',
#     '40': 'Utah 12.1%',
#     '47': 'Vermont 13.6%',
#     '43': 'Virginia 12.5%',
#     '30': 'Washington 10.7%',
#     '22': 'West Virginia 9.8%',
#     '32': 'Wisconsin 10.9%',
#     '2': 'Wyoming 7.5%'
# }

# while True:
#     state_choice = input('Enter a state name or rank to view the state\'s effective tax burden or \'q\' to continue to the next section: ')
#     if state_choice == 'q':
#         break
#     elif tax_burden(state_choice) == None:
#         print('You have entered an invalid response.')
#     else:
#         print(tax_burden(state_choice))
#     another_state = input('Would you like to view another state? Enter \'y\' for yes or \'n\' for no: ')
#     if another_state == 'y':
#         pass
#     elif another_state == 'n':
#         break
#     else:
#         print('You have entered an invalid response.')
#         continue