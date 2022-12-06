# Lab 17 - Quotes API, Version 1: Get a Random Quote
import requests
from pprint import pprint
import json

response = requests.get('https://favqs.com/api/qotd')
response_text = response.json()
author  = response_text['quote']['author']
quote = response_text['quote']['body']

# print(f'Author: {author}\nQuote: \"{quote}\"')


# Version 2: List Quotes by Keyword
keyword = input('Enter a keyword to search for quotes or \'q\' to exit: ')  # stores user input in var 'keyword' outside loop to allow next page results to load
page = 1    # 'page' counter outside the loop to allow counter to increase with each loop

while True:
    header = {'Authorization': 'Token token="855df50978dc9afd6bf86579913c9f8b"'}
    parameters = {'filter': keyword, 'page': page}  # stores user input and page number to allow search terms and next page functionality in URL
    search_response = requests.get('https://favqs.com/api/quotes', params=parameters, headers=header)
    search_response_text = search_response.json()
    quotes: list = search_response_text['quotes']   # sorts returned list index 'quotes'
    if keyword == 'q':  # user input ends search/program
        break
    else:
        print(f'25 quotes associated with {keyword} - page {page}')
        for i in quotes:    # loops through list indices (list of dictionaries)
            for key in i:   # loops through dictionary keys
                if key == 'author':
                    author = (i[key])   # stores value of key 'author' as 'author'
                elif key == 'body':
                    quote = (i[key])    # stores value of key 'body' as 'quote'
            print(f'\"{quote}\"\n\t - {author}')    # prints loop values of authors and quotes
    next = input('Enter \'next page\' or \'done\': ')   # stores user input to allow exiting search/program or to check results of next page returned
    if next == 'done':
        print('Thank you for searching for quotes.  We hope you were inspired.  Good day.  I said good day!')
        break
    elif next == 'next page':
        page += 1   # increases page number to return next page of results for search based upon user input
        continue
    else:
        print('You did not enter a valid response.  Goodbye.')  # exits program
        break