import requests
from pprint import pprint


# response.json()
def random_joke():
    ...


command = input(
    "Enter 'random' to get a random Dad Joke or 'search' to search for dad jokes using a keyword.").lower()


endpoint = 'search'
response = requests.get(f'https://icanhazdadjoke.com/{endpoint}',
                        headers={'accept': 'application/json'})

pprint(response.json()['joke'])
