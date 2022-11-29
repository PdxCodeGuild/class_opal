# Python Mini-Capstone: State Ranker

# Welcome message
print('''\n\t\t\t\tWelcome to the State Ranker!\n
We will be reviewing states for potential relocation based upon the following categories:
Overall tax burden; political affiliation; median home value; and crime rate (violent/property).
You will be prompted to save states in each category.  Once finished, you will have a file that 
ranks your choices based upon the number of saves from all categories.  States must be saved in 
multiple categories to be considered.\n''')

from csv import DictReader
from bs4 import BeautifulSoup
from urllib.request import urlopen

# Opens Tax Foundation website to webscrape effective tax burdens
with urlopen('https://taxfoundation.org/tax-burden-by-state-2022/#results') as response:
    soup_tax = BeautifulSoup(response, 'html.parser')   # parses HTML data webpage listed above

# Opens CSV files to access state data
politics_csv = r'C:\Users\joshg\pdx_code\class_opal\code\josh\python\josh_mini_capstone\politics.csv'
with open(politics_csv, 'r') as file:
    politics_dict = DictReader(file) # stores CSV data as dictionaries
    politics_list = list(politics_dict)  # stores dictionaries from CSV data in a list

homes_csv = r'C:\Users\joshg\pdx_code\class_opal\code\josh\python\josh_mini_capstone\homes.csv'
with open(homes_csv, 'r') as file:
    homes_dict = DictReader(file)
    homes_list = list(homes_dict)

crime_csv = r'C:\Users\joshg\pdx_code\class_opal\code\josh\python\josh_mini_capstone\crime.csv'
with open(crime_csv, 'r') as file:
    crime_dict = DictReader(file)
    crime_list = list(crime_dict)


def tax_burden(user_input): # Returns state, tax_rate, and data based upon user input for either state or rank
    for row in soup_tax.table.contents[5].find_all('tr'):   # loops selected table data in parse tree
        state = row.contents[1].string  # stores string of state names from table
        tax_rate = row.contents[3].string   # stores string of effective tax rate from table
        rank = row.contents[5].string   # stores string of state rank (1 is lowest tax rate) from table
        if user_input == state: # returns single value of either user choice of state or rank
            return f'State: {state}, Effective Tax Burden: {tax_rate}, Rank: {rank}'
        elif user_input == rank:
            return f'State: {state}, Effective Tax Burden: {tax_rate}, Rank: {rank}'


def politics(user_input):   # Returns state and political party control of that state based upon user input for either state or political party
    for dict in politics_list:  # loops data from selected CSV list of dictionaries 
        state = dict['ï»¿state']    # stores key from CSV file (file returns 'state' as 'ï»¿state')
        control = dict['control']
        if user_input == state: # returns single value of state or multiple values (if applicable) of political affiliation (control)
            print(f'State: {user_input}, Political Affiliation: {control}')
        elif user_input == control:
            print(f'State: {state}, Political Affiliation: {user_input}')
    

def homes(user_input):  # Returns state and median home price based upon user input for either state or price
    for dict in homes_list:
        state = dict['ï»¿state']
        median_value = dict['MedianValue']
        if user_input == state:
            return f'State: {user_input}, Median Home Price: ${median_value}'
        elif user_input != state:   # converts user input to an integer to create list of values matching try statement
            try:
                int(user_input)
                if int(user_input) >= int(median_value):
                    print(f'State: {state}, Median Home Price: ${median_value}')
            except ValueError:  # if user input is not an integer, stops ValueError from breaking code
                continue


def crime(user_input):  # Returns state(s) and crime rate (violent/property) based upon user input for either state or crime rate per 100k people
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


# Lists to save user choices by category
tax_favs_list = []
politics_favs_list = []
homes_favs_list = []
crime_favs_list = []

while True: # REPL for Tax Burden
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

while True: # REPL for Politics
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
        except:
            continue
    another_state = input('Would you like to view another state? Enter \'y\' for yes or \'n\' for no: ')
    if another_state == 'y':
        continue
    elif another_state == 'n':
        break
    else:
        print('You have entered an invalid response.')
        continue

while True: # REPL for Median Home Values
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

while True: # REPL for Crime
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

for state in set(all_lists):    # loops 'all_lists' and assigns state names: frequency to state_count dictionary 
    state_count[state] = all_lists.count(state)

# Lists for storing states by number of matches
four_matches = []
three_matches = []
two_matches = []
one_match = []

for state, occurrence in state_count.items():   # loops keys, values in state_count dictionary and appends lists above by number of matches
    if occurrence == 4:
        four_matches.append(state)
    elif occurrence == 3:
        three_matches.append(state)
    elif occurrence == 2:
        two_matches.append(state)
    elif occurrence == 1:
        one_match.append(state)


def results(lists): # Returns items from parameter as an enumerated list
    matches = ''
    for i, state in enumerate(lists, 1):
        matches += '{}. {}'.format(i, state) + '\n'
    return matches
        

final_results = f'''\n\t\t\tSTATE RANKER\n
Your saved states that match all categories:\n{results(four_matches)}\n
Your saved states that match 3 categories:\n{results(three_matches)}\n
Your saved states that match half of the categories:\n{results(two_matches)}
'''

print(final_results)
print('*These results have been saved to file \'state_ranker.txt\'')

output_path = r'C:\Users\joshg\pdx_code\class_opal\code\josh\python\josh_mini_capstone\state_ranker.txt'

# Overwrites original file with information from 'final_results' list above 
with open(output_path, 'w') as file:
    file.write(final_results)