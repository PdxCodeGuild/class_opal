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
search_response = requests.get('https://favqs.com/api/quotes?page=page&filter=' + keyword + '&type=tag', headers=header)
search_response_text = search_response.json()
author = search_response_text['quotes'][1]['author']
quote = search_response_text['quotes'][1]['body']
page = search_response_text['page']
print(f'25 quotes associated with {keyword} - page {page}')
# print(search_response_text)
print(f'\"{quote}\" - {author}')
# for keystroke in keyword:
#     if keyword == 'q':
#         break
#     else:
#         print(f'{int} quotes associated with {keyword}.')
#         print('<list of quotes>')
# next = input('Enter \'next page\' or \'done\': ')
# if next == 'next page':
#     print(f'{int} quotes associated with {keyword}.')
#     print('<list of quotes>')
# elif next == 'done':
#     continue
# else:

#     continue

# Prompt the user for a keyword, list the quotes you get in response, and prompt the user to either show the next page or enter a new keyword. 
# You can use string concatenation to build the URL.
