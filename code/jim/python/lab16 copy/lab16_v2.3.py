"""
PDX Code Guild Lab 16 (v2): Dad Joke API
"""
import time
from comedian import Comedian
from audience import Audience

seinfeld = Comedian()
audience = Audience()
search_term = audience.give_prompt()

joke_count = 0
limit = 5
page_count = 1
while True:
    joke_dict = seinfeld.get_jokes(search_term, page_count)
    joke_results = joke_dict['results']
    total_jokes = seinfeld.total_jokes(joke_dict)

    if total_jokes == 0:
        break

    loop_count = 1
    while True:
        joke = joke_dict['results'][loop_count - 1]['joke']
        seinfeld.tell_joke(joke)
        audience.react()
        joke_count += 1

        if joke_count == total_jokes:
            break
        elif loop_count == limit:
            more_jokes = seinfeld.keep_joking(search_term)
            break
        else:
            more_jokes = seinfeld.keep_joking(search_term)
            if more_jokes == 'n':
                break
        loop_count += 1
    page_count += 1

    if joke_count == total_jokes:
        time.sleep(1)
        print(f"No more jokes to tell about {search_term}.")
        break
    elif more_jokes == 'n':
        break
