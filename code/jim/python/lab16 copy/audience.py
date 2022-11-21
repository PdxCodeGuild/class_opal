"""
PDX Code Guild Lab 16 (v2): Dad Joke API 
A simple model of an audience for comedy
Uses the following library https://pypi.org/project/Random-Word/
"""

from random_word import Wordnik
from random import randint


class Audience():
    def __init__(self) -> None:
        pass

    def give_prompt(self):
        r = Wordnik()
        prompt = r.get_random_word(
            hasDictionaryDef="true", maxCorpusCount=10, maxLength=5)
        print(f"{prompt}!")
        return prompt

    def react(self):
        reactions = {
            1: 'Ha-ha-ha-ha-ha',
            2: 'Ugh',
            3: 'Booooooo!',
        }
        return reactions[randint(0, 2)]
