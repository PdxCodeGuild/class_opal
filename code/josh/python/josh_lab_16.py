# Lab 16: Dad Joke API, Part 1 - Use the API to get and display a dad joke to the user

import requests
from pprint import pprint
import json

header = {'accept': 'application/json'}
response = requests.get('https://icanhazdadjoke.com/', headers=header)
response_text = response.json()

# Part 2 - Create a REPL that allows user to enter a search term and go through jokes one at a time

while True:
    user_input = input('Enter a search term to locate a related dad joke: ')    # user enters string to become search term to find joke
    parameter = {'term': user_input}    # term - search term (default: all)
    search_response = requests.get('https://icanhazdadjoke.com/search', params=parameter, headers=header)   # gets jokes
    search_response_text = search_response.json()   # jokes returned changed to json
    if search_response_text['results'] == []:   # skips empty results
        print(f'{user_input} did not return any jokes.')    # displays to user if search term doesn't exist
    else:
        for dict in (search_response_text['results']):  # searches 'results' list of dictionaries
            print(dict['joke']) #displays first
            next = input(f'Another {user_input} joke? Enter \'y\' for yes or \'n\' for no: ')
            if next == 'y': # continues displaying next joke for search term
                continue
            else:   # stops showing jokes from search term
                break
    again = input('Would you like a new joke search? (\'y\' for yes or \'n\' to exit) ') # asks user to continue or not
    if again == 'n':    # exits program
        break
    elif again == 'y':  # continues program
        continue
    else:   # informs user of invalid response and exits program
        print('You did not enter a valid response.  Goodbye.')
        break