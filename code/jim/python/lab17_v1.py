"""
PDX Code Guild Lab 17: Quotes API using https://favqs.com/api
"""

import requests

base_url = "https://favqs.com/api/qotd"

response = requests.get(base_url,
                        headers={'accept': 'application/json'})

# convert response to dict and print quote and author
response_dict = response.json()
author = response_dict['quote']['author']
quote_body = response_dict['quote']['body']

print(f'{author.title()} once said, "{quote_body}"')
