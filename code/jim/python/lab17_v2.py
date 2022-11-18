"""
PDX Code Guild Lab 17: Quotes API using https://favqs.com/api
"""

import requests
import pprint

base_url = "https://favqs.com/api/quotes/"
headers = {'Authorization': 'Token token="855df50978dc9afd6bf86579913c9f8b"'}

search_term = input("enter a keyword to search for quotes: ")

page = 1
while True:
    url = base_url + f"?page={page}&filter={search_term}"

    response = requests.get(url, headers=headers)
    response_dict = response.json()

    print(f"25 quotes associated with {search_term} - page {page}")
    for quote in response_dict['quotes']:
        author = quote['author']
        quote_body = quote['body']
        print(f'{author.title()} once said, "{quote_body}"\n')

    if response_dict['last_page'] == True:
        break
    else:
        page += 1

    answer = input("enter 'next page' or 'done': ")

    if answer == 'done':
        print("Thank you. Goodbye.")
        break

print("No more quotes on that topic. Goodbye.")
