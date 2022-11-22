"""
PDX Code Guild Lab 16: Dad Joke API using https://icanhazdadjoke.com/
"""
import requests
import pprint
import time
import re

response = requests.get('https://icanhazdadjoke.com/',
                        headers={'accept': 'application/json'})

# convert response to dict and print joke
response_dict = response.json()
joke = response_dict['joke']

# Regex to split on sentences without removing punctuation found here:
# https://stackoverflow.com/questions/44244583/splitting-on-regex-without-removing-delimiters
joke_sentences = re.split(r'(?<=[\.\!\?])\s*', joke)

pprint.pprint(joke_sentences[0])

if len(joke_sentences) > 1:
    time.sleep(4.25)
    for sentence in joke_sentences[1:]:
        pprint.pprint(sentence)
