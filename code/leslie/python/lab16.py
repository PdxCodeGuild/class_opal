import requests
from pprint import pprint
import json


response = requests.get('https://icanhazdadjoke.com/search',
                        headers={'accept': 'application/json'})

current_page = response.json()['current_page']


while True:
    keyword = input("What topic would you like a dad joke about? ")
    my_params = {'term': keyword, 'limit': 1, 'page': 1}
    response = requests.get('https://icanhazdadjoke.com/search', params=my_params,
                            headers={'accept': 'application/json'})
    response_text = response.json()
    results: list = response.json()['results']
    current_page = response.json()['current_page']
    next_page = response.json()['next_page']
    total_jokes = response.json()['total_jokes']
    # print('\n first loop', response_text)

    for dict in results:
        for key in dict:
            if key == 'joke':
                print(dict[key], '\n')

    while current_page != total_jokes:
        next = input(
            f'wanna see another joke about {keyword}? Type "y" or "n": ')

        if next == 'y':
            next_page = response.json()['next_page']
            my_params = {'term': keyword, 'limit': 1, 'page': next_page}
            response = requests.get('https://icanhazdadjoke.com/search', params=my_params,
                                    headers={'accept': 'application/json'})
            response_text = response.json()
            results: list = response.json()['results']
            current_page = response.json()['current_page']

            for dict in results:
                for key in dict:
                    if key == 'joke':
                        print('\n', dict[key], '\n')
                        # print('\n 2nd loop', response_text)

        elif next == 'n':
            break
        if current_page == total_jokes:
            print(f'Sorry! All out of {keyword} jokes!')
            break
