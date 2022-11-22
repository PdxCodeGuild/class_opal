import requests
from pprint import pprint
from os import system
from time import sleep


def random_joke():
    response = requests.get(f'https://icanhazdadjoke.com/',
                            headers={'accept': 'application/json'})
    system('cls||clear')

    print(response.json()['joke'])
    print('\n\n\n')
    sleep(10)
    while True:
        yes_or_no = input(
            'Would you like to see another joke? yes or no').lower()
        if yes_or_no == 'yes':
            random_joke()
        break
    return


def search_joke(term, page):
    parameters = {
        'page': str(page),
        'limit': '1',
        'term': term
    }
    endpoint = 'search'
    response = requests.get(f'https://icanhazdadjoke.com/{endpoint}', params=parameters,
                            headers={'accept': 'application/json'})
    system('cls||clear')
    try:
        pprint(response.json()["results"][0]['joke'])
    except IndexError:
        print(f"That's it for jokes about {term}!")
        return
    # sleep(3)
    while True:
        yes_or_no = input(
            'Would you like to see the next joke? yes or no').lower()
        if yes_or_no == 'yes':
            page += 1
            search_joke(term, page)
        return


while __name__ == '__main__':
    print('Welcome to the Dad Joke API!')
    while True:
        command = input(
            "Enter 'random' to get a random Dad Joke or 'search' to search for dad jokes using a keyword.").lower()
        if command == 'search':
            search_term = input(
                'Type the term for which you would like to search:')
            search_joke(search_term, page=1)
            break
        elif command == 'random':
            random_joke()
            break
        else:
            print('This is an invalid command.')

    print('Thank you for laughing, bye!')
    exit()
