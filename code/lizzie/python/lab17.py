# Lab 17: Quote API

"""The URL to get a random quote is https://favqs.com/api/qotd, 
send a request here, parse the JSON in the response into a python 
dictionary, and show the quote and the author."""


import requests
from pprint import pprint


response = requests.get('https://favqs.com/api/qotd')

response_text = response.json()

author = (response_text['quote']['author'])
quote = (response_text['quote']['body'])

print(f'\n"{quote}" \n-- {author}')
