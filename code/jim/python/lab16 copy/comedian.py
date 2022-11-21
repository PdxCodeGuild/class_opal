"""
PDX Code Guild Lab 16 (v2): Dad Joke API 
A simple model of a comedian using https://icanhazdadjoke.com/
"""
import requests
import time
import re


class Comedian():
    """A simple model of a dad-joke-telling comedian."""

    def __init__(self) -> None:
        self.base_url = "https://icanhazdadjoke.com/search?"
        pass

    def get_prompt(self):
        """Initialize joke telling with an audience prompt."""
        print("How's everybody doing tonight?")
        time.sleep(2)
        search_term = input("Someone shout out a topic... ")
        return search_term

    def get_jokes(self, search_term: str, page=1, limit=20):
        """Return a dict with jokes and metadata about a search topic."""
        parameters = {'page': page, 'limit': limit, 'term': search_term}
        joke_search_response = requests.get(
            self.base_url, params=parameters, headers={'accept': 'application/json'})
        return joke_search_response.json()

    def total_jokes(self, joke_dict: dict):
        """Counts the total number of jokes in a joke dictionary."""
        total_jokes = joke_dict['total_jokes']
        if total_jokes == 0:
            time.sleep(2)
            print("Sorry, I have no jokes about that topic.")
        return total_jokes

    def tell_joke(self, joke: str):
        """Parse joke into setup/punchline and display to user with timing."""
        joke_sentences = re.split(r'(?<=[\.\!\?])\s*', joke)
        print(joke_sentences[0])
        if len(joke_sentences) > 1:
            time.sleep(0.5)
            for sentence in joke_sentences[1:]:
                print(sentence)

    def keep_joking(self, search_term: str):
        """Ask the user if they want to hear more jokes."""
        while True:
            more_jokes = input(
                f"Would you like to hear more jokes about {search_term}? (y/n) ")
            if more_jokes == 'n':
                time.sleep(1)
                print("Thanks, folks. You've been a great audience.")
                break
            elif more_jokes == 'y':
                break
            else:
                print("Invalid repsonse. Please choose 'y' or 'n'.")
        return more_jokes
