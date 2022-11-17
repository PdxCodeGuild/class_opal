# Lab 16: Dad Joke API, Part 1 - Use the API to get and display a dad joke to the user

import requests
from pprint import pprint
import json

header = {'accept': 'application/json'}
response = requests.get('https://icanhazdadjoke.com/', headers=header)
response_text = response.json()

# pprint(response_text)


# Part 2 - Add the ability to "search" for jokes using another endpoint:
parameters = {'page': int, 'limit': int, 'term': str} #page-location(def:1), limit-# of results(def:20,max:30), term-search term(default:all)

search_response = requests.get('https://icanhazdadjoke.com/search/', params=parameters, headers=header, )
search_response_text = search_response.json()

pprint(search_response_text)

# Create a REPL that allows one to enter a search term and go through jokes one at a time:

while True:
    user_input = input('Enter a search term to locate a related dad joke: ')    # user enters string to become search term to find joke
    for element in parameters:  # loop through 'parameters' var to update 'term' in search
        if element == 'term':   # stops on element 'term' in loop of 'parameters' var
            user_input == :
            print(search_response_text['joke'])
        else:
            print(f'{user_input} did not return any jokes.')    # displays to user if search term doesn't exist
            pass

    again = input('Would you like another joke? (\'y\' for yes or \'n\' to exit) ') # asks user to continue or not
    if again == 'n':    # exits loop
        break
    elif again == 'y':  # continues loop
        continue
    else:   # informs user of invalid response and exits loop 
        print('You did not enter a valid response.  Goodbye.')
        break