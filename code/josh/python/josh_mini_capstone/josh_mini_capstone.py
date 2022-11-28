# Python Mini-Capstone

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
# import requests
# import pandas as pd
# from pprint import pprint
from csv import DictReader
from bs4 import BeautifulSoup #, SoupStrainer
from urllib.request import urlopen
# import json

# Opens 1st website to webscrape effective tax burdens
with urlopen('https://taxfoundation.org/tax-burden-by-state-2022/#results') as response:
    soup_tax = BeautifulSoup(response, 'html.parser')

politics_csv = r'C:\Users\joshg\pdx_code\class_opal\code\josh\python\josh_mini_capstone\politics.csv'
with open(politics_csv, 'r') as file:
    politics = DictReader(file)
    politics_list = list(politics)

homes_csv = r'C:\Users\joshg\pdx_code\class_opal\code\josh\python\josh_mini_capstone\homes.csv'
with open(homes_csv, 'r') as file:
    homes = DictReader(file)
    homes_list = list(homes)

crime_csv = r'C:\Users\joshg\pdx_code\class_opal\code\josh\python\josh_mini_capstone\crime.csv'
with open(crime_csv, 'r') as file:
    crime = DictReader(file)
    crime_list = list(crime)


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


# Returns state and political party control of that state based upon user input for either state or political party
def politics(user_input):
    for dict in politics_list:
        state = dict['ï»¿state']
        control = dict['control']
        if user_input == state:
            print(f'State: {user_input}, Political Affiliation: {control}')
        elif user_input == control:
            print(f'State: {state}, Political Affiliation: {user_input}')


# Returns state and median home price based upon user input for either state or price
def homes(user_input):
    for dict in homes_list:
        state = dict['state']
        median_value = dict['MedianValue']
        if user_input == state:
            print(f'State: {user_input}, Median Home Price: ${median_value}')
        elif user_input >= median_value:
            print(f'State: {state}, Median Home Price: ${median_value}')


# Returns state (individual or list) and crime rate (violent/property) based upon user input for either state or crime rate per 100k people
def crime(user_input):
    for dict in crime_list:
        state = dict['state']
        rate = dict['rate']
        if user_input == state:
            print(f'State: {user_input}, Crime Rate per 100,000 people: {int(float(rate))}')
        elif int(user_input) <= int(float(rate)):
            print(f'State: {state}, Crime Rate per 100,000 people: {int(float(rate))}')


# REPL for Tax Burden
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
        continue
    elif another_state == 'n':
        break
    else:
        print('You have entered an invalid response.')
        continue


# REPL for Politics
while True:
    state_choice = input('Enter a state name, \'Democrat\', \'Republican\', or \'Split\' to view state politics.  Enter \'q\' to continue to the next section: ')
    if state_choice == 'q':
        break
    elif politics(state_choice) == None:
        print('You have entered an invalid response.')
        print('111111111111111111111111111111111111111111111111111')
    else:
        print(politics(state_choice))
    another_state = input('Would you like to view another state? Enter \'y\' for yes or \'n\' for no: ')
    if another_state == 'y':
        continue
    elif another_state == 'n':
        break
    else:
        print('You have entered an invalid response.')
        print('22222222222222222222222222222222222222222222222222')
        continue



# while True:
#     state_choice = input('Enter a state name, \'Democrat\', \'Republican\', or \'Split\' to view state politics.  Enter \'q\' to continue to the next section: ')
#     if state_choice == 'q':
#         break
#     elif state_choice != politics_list['state']:
#         print('You have entered an invalid response.')
#     else:
#         print(politics_list[0::1][state_choice])
#     another_state = input('Would you like to view another state? Enter \'y\' for yes or \'n\' for no: ')
#     if another_state == 'y':
#         continue
#     elif another_state == 'n':
#         break
#     else:
#         print('You have entered an invalid response.')
#         print('22222222222222222222222222222222222222222222222222')
#         continue






# REPL for Median Home Values
while True:
    state_choice = input('Enter a state name for median home values, a max price to view states below that value, or \'q\' to continue to the next section: ')
    if state_choice == 'q':
        break
    elif homes(state_choice) == None:
        print('You have entered an invalid response.')
    else:
        print(homes(state_choice))
    another_state = input('Would you like to view another state? Enter \'y\' for yes or \'n\' for no: ')
    if another_state == 'y':
        continue
    elif another_state == 'n':
        break
    else:
        print('You have entered an invalid response.')
        continue

# REPL for Crime
while True:
    state_choice = input('Enter a state name for crime rate, a rate max for states below that value, or \'q\' to continue to the next section: ')
    if state_choice == 'q':
        break
    elif crime(state_choice) == None:
        print('You have entered an invalid response.')
    else:
        print(crime(state_choice))
        continue
    another_state = input('Would you like to view another state? Enter \'y\' for yes or \'n\' for no: ')
    if another_state == 'y':
        continue
    elif another_state == 'n':
        break
    else:
        print('You have entered an invalid response.')
        continue




# Need to create lists to add user choices of states from REPLs for CRUD