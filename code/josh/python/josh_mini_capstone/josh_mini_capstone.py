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
import requests
import pandas as pd
from pprint import pprint
from bs4 import BeautifulSoup, SoupStrainer
from urllib.request import urlopen

# Opens 1st website to webscrape effective tax burdens
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


# Returns state and political party control of that state based upon user input for either state or political party
def politics(user_input):
    # Iterates through the remaining list of strings and converts each string to a dictionary value 
    pol_rel_path = 'C:/Users/joshg/pdx_code/class_opal/code/josh/python/josh_mini_capstone/politics.csv'
    # Opens file at relative path and converts lines into a list of strings
    with open(pol_rel_path, 'r') as file:
        lines:list = file.read().split('\n')
    states_list = []
    # Creates a list of strings, where each string will be used as a dictionary key from the first line in the file above
    keys: list[str] = lines[0].split(',')    
    for line in lines[1:]:
        state_dict = {}
        values: list[str] = line.split(',')
        for i, key in enumerate(keys):
            state_dict[key] = values[i]
        states_list.append(state_dict)
    for d in states_list:
        state = d['ï»¿state']
        control = d['control']
        if user_input == state:
            print(f'State: {user_input}, Political Affiliation: {control}')
        elif user_input == control:
            print(f'State: {state}, Political Affiliation: {user_input}')
            

# Returns state and median home price based upon user input for either state or price
def homes(user_input):
    # Iterates through the remaining list of strings and converts each string to a dictionary value 
    homes_rel_path = r'C:\Users\joshg\pdx_code\class_opal\code\josh\python\josh_mini_capstone\homes.csv'
    # Opens file at relative path and converts lines into a list of strings
    with open(homes_rel_path, 'r') as file:
        lines:list = file.read().split('\n')
    states_list = []
    # Creates a list of strings, where each string will be used as a dictionary key from the first line in the file above
    keys: list[str] = lines[0].split(',')    
    for line in lines[1:]:
        state_dict = {}
        values: list[str] = line.split(',')
        for i, key in enumerate(keys):
            state_dict[key] = values[i]
        states_list.append(state_dict)
    for d in states_list:
        state = d['ï»¿state']
        median_value = d['MedianValue']
        if user_input == state:
            print(f'State: {user_input}, Median Home Price: ${median_value}')
        elif user_input >= median_value:
            print(f'State: {state}, Median Home Price: ${median_value}')


# Returns state (individual or list) and crime rate (violent/property) based upon user input for either state or crime rate per 100k people
def crime(user_input):
    # Iterates through the remaining list of strings and converts each string to a dictionary value 
    crime_rel_path = r'C:\Users\joshg\pdx_code\class_opal\code\josh\python\josh_mini_capstone\crimes.csv'
    # Opens file at relative path and converts lines into a list of strings
    with open(crime_rel_path, 'r') as file:
        lines:list = file.read().split('\n')
    states_list = []
    # Creates a list of strings, where each string will be used as a dictionary key from the first line in the file above
    keys: list[str] = lines[0].split(',')    
    for line in lines[1:]:
        state_dict = {}
        values: list[str] = line.split(',')
        for i, key in enumerate(keys):
            state_dict[key] = values[i]
        states_list.append(state_dict)
    for d in states_list:
        state = d['ï»¿state']
        rate = d['rate']
        if user_input == state:
            print(f'State: {user_input}, Crime Rate per 100,000 people: {int(float(rate))}')
        elif int(user_input) <= int(float(rate)):
            print(f'State: {state}, Crime Rate per 100,000 people: {int(float(rate))}')
    # for d in states_list:
    #     return_list = []
    #     state = d['ï»¿state']
    #     rate = d['rate']
    #     if user_input == state:
    #         return_list.append(f'State: {user_input}, Crime Rate per 100,000 people: {int(float(rate))}')
    #     elif int(user_input) <= int(float(rate)):
    #         return_list.append(f'State: {state}, Crime Rate per 100,000 people: {int(float(rate))}')
    # return return_list


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