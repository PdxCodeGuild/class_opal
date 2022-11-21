import requests
from pprint import pprint
import json

# response = requests.get('https://favqs.com/api/qotd', headers={
#                         'Content-Type': 'application/json'})

# quote_info = response.json()['quote']

# print(f'\n', quote_info['body'], '--', quote_info['author'], '\n',)

# version 2


def find_quote():
    while True:
        keyword = input(
            "What would you like to see a quote about? Enter keyword: ")
        my_params = {'filter': keyword}
        response = requests.get('https://favqs.com/api/quotes', headers={
                                'Content-Type': 'application/json', 'Authorization': 'Token token="855df50978dc9afd6bf86579913c9f8b"'}, params=my_params)
        quotes = response.json()['quotes']

        for dic in quotes:
            for key in dic:
                if key == "body":
                    print(dic[key], '\n')

        last_page = response.json()['last_page']
        print("Last page? ", last_page)
        page = response.json()['page']
        print('page ', page)

        while last_page == False:
            next = input(
                "To see the next page, type 'next'. To search by new keyword, type 'new': ")
            if next == 'next':
                page = response.json()['page'] + 1
                my_params = {'filter': keyword, 'page': page}
                response = requests.get('https://favqs.com/api/quotes', headers={
                    'Content-Type': 'application/json', 'Authorization': 'Token token="855df50978dc9afd6bf86579913c9f8b"'}, params=my_params)
                quotes = response.json()['quotes']
                for dic in quotes:
                    for key in dic:
                        if key == 'body':
                            print(dic[key], '\n')
                last_page = response.json()['last_page']
                # just to prove it's the last page
                print("Last page? ", last_page)
                page = response.json()['page']
                print("Page ", page)
            else:
                find_quote()
            if last_page == True:
                print(f"All out of quotes about {keyword}!")
                find_quote()


find_quote()
