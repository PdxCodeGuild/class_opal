import requests
import pprint
import json

while True:
    user_request = input(f'Would you like to hear a joke? Press any key to conitnue or q of quit: ').lower()
    if user_request == 'q':
        break
    response = requests.get('https://icanhazdadjoke.com/search', headers={'accept': 'application/json'}, params={'term': user_request})
    response_dict = response.json()
    result_joke = response_dict['results']
    for joke in result_joke:
        print(joke['joke'])
        user_continue= input(f'Would you like to see the next joke? Press any key to conitnue or q of quit: ')
        if user_continue == 'q':
            break

