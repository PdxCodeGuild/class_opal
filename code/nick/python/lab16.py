import requests
from pprint import pprint


# response.json()
def random_joke():
    ...


def search_joke():
    page = 1
    search_term = input('Type the term for which you would like to search:')
    parameters = {
        'page': str(page),
        'limit': '1',
        'term': search_term
    }
    endpoint = 'search'
    response = requests.get(f'https://icanhazdadjoke.com/{endpoint}', params=parameters,
                            headers={'accept': 'application/json'})

    pprint(response.json()['joke'])


command = input(
    "Enter 'random' to get a random Dad Joke or 'search' to search for dad jokes using a keyword.").lower()
match command:
    case 'search':
        search_joke()
