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

header = {'Authorization': 'Token token="855df50978dc9afd6bf86579913c9f8b"'}
keyword = input('Enter a keyword to search for quotes or \'q\' to exit: ')
parameters = {'filter': keyword, 'page': }
page = 'page'
search_response = requests.get('https://favqs.com/api/quotes?page=' + page + '&filter=' + keyword + '&type=tag', headers=header)
search_response_text = search_response.json()
# author = search_response_text['quotes'][1]['author']
quotes: list = search_response_text['quotes']
# quote = search_response_text['quotes'][1]['body']
page = search_response_text['page']
next_page = int(search_response_text['page'] + 1)

if keyword == 'q':
    exit
else:
    print(f'25 quotes associated with {keyword} - page {page}')
    for i in quotes:
        for key in i:
            if key == 'author':
                author = (i[key])
            elif key == 'body':
                quote = (i[key])
        print(f'\"{quote}\"\n\t - {author}')

next = input('Enter \'next page\' or \'done\': ')
if next == 'done':
    exit
elif next == 'next page':
    print(next_page)    # I'm going to change this.
else:
    print('You did not enter a valid response.  Goodbye.')
# else:
#     continue

# pprint(quotes)
# pprint(search_response_text)
# print(f'\"{quote}\" - {author}')

# Prompt the user for a keyword, list the quotes you get in response, and prompt the user to either show the next page or enter a new keyword. 
# You can use string concatenation to build the URL.

# Optional URL Parameters:

# Parameter	Description
# filter	Type lookup or keyword search
# page	Page number (25 quotes per page)