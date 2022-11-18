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
    # search_response = requests.get('https://icanhazdadjoke.com/search/', params=parameter, headers=header)
    search_response = requests.get(f'https://icanhazdadjoke.com/search?term={user_input}', headers=header)  # temp fix for line 16 'params' not working
    search_response_text = search_response.json()
    if search_response_text['status'] == 404:
        print(f'{user_input} did not return any jokes.')    # displays to user if search term doesn't exist
    else:
        print(search_response_text)
        pass
    again = input('Would you like another joke? (\'y\' for yes or \'n\' to exit) ') # asks user to continue or not
    if again == 'n':    # exits loop
        break
    elif again == 'y':  # continues loop
        continue
    else:   # informs user of invalid response and exits loop 
        print('You did not enter a valid response.  Goodbye.')
        break