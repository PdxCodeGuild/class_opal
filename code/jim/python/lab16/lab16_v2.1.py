"""
PDX Code Guild Lab 16 (v2): Dad Joke API using https://icanhazdadjoke.com/
"""
import requests
import time
import re

# allow searching for jokes
search_term = input("What subject to you want jokes for? ")

joke_count = 0
limit = 5
page_count = 1

base_url = "https://icanhazdadjoke.com/search?"

while True:
    parameters = {
        'page': page_count,
        'limit': limit,
        'term': search_term
    }

    joke_search_response = requests.get(
        base_url, params=parameters, headers={'accept': 'application/json'})

    joke_search_response_dict = joke_search_response.json()
    joke_results = joke_search_response_dict['results']
    total_jokes = joke_search_response_dict['total_jokes']
    total_pages = joke_search_response_dict['total_pages']

    if total_jokes == 0:
        print("Sorry, I have no jokes about that topic.")
        break

    loop_count = 1
    while True:
        joke = joke_search_response_dict['results'][loop_count - 1]['joke']
        joke_sentences = re.split(r'(?<=[\.\!\?])\s*', joke)
        print(joke_sentences[0])
        if len(joke_sentences) > 1:
            time.sleep(0.5)
            for sentence in joke_sentences[1:]:
                print(sentence)
        joke_count += 1

        if joke_count == total_jokes:
            break
        elif loop_count == limit:
            more_jokes = input(
                f"Would you like to hear more jokes about {search_term}? (y/n) ")
            if more_jokes == 'n':
                time.sleep(1)
                print("Have a nice day.")
            break
        else:
            more_jokes = input(
                f"Would you like to hear more jokes about {search_term}? (y/n) ")
            if more_jokes == 'n':
                time.sleep(1)
                print("Have a nice day.")
                break
        loop_count += 1
    page_count += 1

    if joke_count == total_jokes or more_jokes == 'n':
        time.sleep(1)
        print(f"No more jokes to tell about {search_term}.")
        break
