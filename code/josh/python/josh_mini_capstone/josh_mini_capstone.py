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

# Welcome message
print('''\n\t\t\t\tWelcome to the State Ranker!\n
We will be reviewing states for potential relocation based upon the following categories:
Overall tax burden; political affiliation; median home value, and crime rate (violent/property).
You will be prompted to save states in each category.  Once finished, you will have a file that 
ranks your choices based upon the number of saves from all categories.  States must be saved in 
multiple categories to be considered.\n''')

from csv import DictReader
from bs4 import BeautifulSoup
from urllib.request import urlopen
# import json

# Opens Tax Foundation website to webscrape effective tax burdens
with urlopen('https://taxfoundation.org/tax-burden-by-state-2022/#results') as response:
    soup_tax = BeautifulSoup(response, 'html.parser')

# Opens politics.csv to access state political affiliation data
politics_csv = r'C:\Users\joshg\pdx_code\class_opal\code\josh\python\josh_mini_capstone\politics.csv'
with open(politics_csv, 'r') as file:
    politics = DictReader(file)
    politics_list = list(politics)

# Opens homes.csv to access state median home value data
homes_csv = r'C:\Users\joshg\pdx_code\class_opal\code\josh\python\josh_mini_capstone\homes.csv'
with open(homes_csv, 'r') as file:
    homes = DictReader(file)
    homes_list = list(homes)

# Opens crime.csv to access state violent/property crime rate data
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
        state = dict['ï»¿state']
        median_value = dict['MedianValue']
        if user_input == state:
            return f'State: {user_input}, Median Home Price: ${median_value}'
        elif user_input != state:
            try:
                int(user_input)
                if int(user_input) >= int(median_value):
                    print(f'State: {state}, Median Home Price: ${median_value}')
            except ValueError:
                continue


# Returns state (individual or list) and crime rate (violent/property) based upon user input for either state or crime rate per 100k people
def crime(user_input):
    for dict in crime_list:
        state = dict['ï»¿state']
        rate = dict['rate']
        if user_input == state:
            return f'State: {user_input}, Crime Rate per 100,000 people: {int(float(rate))}'
        elif user_input != state:
            try:
                int(user_input)
                if int(user_input) >= int(float(rate)):
                    print(f'State: {state}, Crime Rate per 100,000 people: {int(float(rate))}')                    
            except ValueError:
                continue

tax_favs_list = []
politics_favs_list = []
homes_favs_list = []
crime_favs_list = []

# REPL for Tax Burden
while True:
    state_choice = input('Enter a state name or rank to view the state\'s effective tax burden or \'q\' to continue to the next section: ')
    if state_choice == 'q':
        break
    elif tax_burden(state_choice) == None:
        print('You have entered an invalid response.')
    else:
        print(tax_burden(state_choice))
        add_state = input('Would you like to save this state to favorites?  Enter \'y\' for yes or \'n\' to continue: ')
        if add_state == 'y':
            try:
                int(state_choice)
                print('Unable to add state by rank.  Please re-enter choice by state name to save.')
            except ValueError:
                tax_favs_list.append(state_choice)
                print(f'{state_choice} saved to favorites.')
                print(tax_favs_list)    # for testing
        else:
            continue
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
    elif politics(state_choice) != None:
        print(politics(state_choice))
    add_state = input('Would you like to save this state to favorites?  Enter \'y\' for yes or \'n\' to continue: ')
    if add_state == 'y':
        try:
            if state_choice == 'Democrat' or state_choice == 'Republican' or state_choice == 'Split':
                print('Unable to add state by political affiliation.  Please re-enter choice by state name to save.')
            else:
                politics_favs_list.append(state_choice)
                print(f'{state_choice} saved to favorites.')
                print(politics_favs_list)   # for testing
        except:
            continue
    another_state = input('Would you like to view another state? Enter \'y\' for yes or \'n\' for no: ')
    # another_state = input('End of search or invalid input.  Would you like to view another state? Enter \'y\' for yes or \'n\' for no: ')
    if another_state == 'y':
        continue
    elif another_state == 'n':
        break
    else:
        print('You have entered an invalid response.')
        continue

# REPL for Median Home Values
while True:
    state_choice = input('Enter a state name for median home values, a max price to view states below that value, or \'q\' to continue to the next section: ')
    if state_choice == 'q':
        break
    elif homes(state_choice) == None:
        print('End of search or invalid entry.')
        continue
    elif homes(state_choice) != None:
        print(homes(state_choice))
    add_state = input('Would you like to save this state to favorites?  Enter \'y\' for yes or \'n\' to continue: ')
    if add_state == 'y':
        try:
            if int(state_choice):
                print('Unable to add state by price.  Please re-enter choice by state name to save.')
            else:
                continue
        except ValueError:
            homes_favs_list.append(state_choice)
            print(f'{state_choice} saved to favorites.')
            print(homes_favs_list)
    else:
        continue
    another_state = input('Would you like to view another state? Enter \'y\' for yes or \'n\' for no: ')
    # another_state = input('End of search or invalid input.  Would you like to view another state? Enter \'y\' for yes or \'n\' for no: ')
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
    elif crime(state_choice) != None:
        print(crime(state_choice))
    add_state = input('Would you like to save this state to favorites?  Enter \'y\' for yes or \'n\' to continue: ')
    if add_state == 'y':
        try:
            if int(state_choice):
                print('Unable to add state by crime rate.  Please re-enter choice by state name to save.')
            else:
                continue
        except ValueError:
            crime_favs_list.append(state_choice)
            print(f'{state_choice} saved to favorites.')
            print(crime_favs_list)
    else:
        continue
    
    another_state = input('Would you like to view another state? Enter \'y\' for yes or \'n\' for no: ')
    if another_state == 'y':
        continue
    elif another_state == 'n':
        break
    else:
        print('You have entered an invalid response.')
        continue


all_lists = tax_favs_list + politics_favs_list + homes_favs_list + crime_favs_list
state_count = {}
four_matches = []
three_matches = []
two_matches = []
one_match = []

for state in set(all_lists):
    state_count[state] = all_lists.count(state)

for state, occurrence in state_count.items():
    if occurrence == 4:
        four_matches.append(state)
    elif occurrence == 3:
        three_matches.append(state)
    elif occurrence == 2:
        two_matches.append(state)
    elif occurrence == 1:
        one_match.append(state)

# for i, value in enumerate(four_matches, 1)(three_matches, 1)(two_matches, 1):
#             ''.join(four_matches)

# print(state_count)
# print(f'States that have matched all lists: {four_matches}')
# print(f'States that have matched 3 out of 4 lists: {three_matches}')
# print(f'States that have matched half of the lists: {two_matches}')
# print(f'States that have matched 1 list: {one_match}')


# Need to check lab 11 to create file based upon 'state_count'
# print (list(enumerate(list name, starting number)))
four_matches = ['Oregon', 'Washington', 'Idaho']    # testing
three_matches = ['Virginia', 'Tennessee', 'New Hampshire', 'South Dakota']  # testing
two_matches = ['California', 'New York']    # testing


final_results = f'''
Your saved states that match all categories:\n{list(enumerate(four_matches, 1))}\n
Your saved states that match 3 categories:\n{list(enumerate(three_matches, 1))}\n
Your saved states that match half of the categories:\n{list(enumerate(two_matches, 1))}
'''

print(final_results)

# Overwrites original file with information from 'contacts_ouput' list above 
output_path = 'class_opal\code\josh\python\josh_mini_capstone\state_ranker.txt'
output_content = '\n'.join(four_matches), '\n'.join(three_matches), '\n'.join(two_matches)

with open(output_path, 'w') as file:
    file.write(output_content)