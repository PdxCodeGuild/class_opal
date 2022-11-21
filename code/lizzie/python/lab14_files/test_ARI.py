# Lab 14: Test ARI

import ARI
from ARI import calculate_ari, number_of_sentences,  number_of_words, number_of_characters


# Reworked the code so I could test each function. Passing contents as
#parameter in the ARI function makes it possible to put in my own string to test.
def test_number_of_sentences():
    assert number_of_sentences("") == 0
    assert number_of_sentences("No period, no sentence") == 0
    assert number_of_sentences("Hello. These are two sentences.") == 2
    assert number_of_sentences("Hello, World!") == 1
    assert number_of_sentences("World?") == 1
    assert type(number_of_sentences("Argument")) is int


def test_number_of_words():
    assert number_of_words("") == 0
    assert number_of_words("Word") == 1
    assert number_of_words("Even w punctuation, these... are words.") == 6
    assert number_of_words("Half-Life") == 1
    assert type(number_of_words("Argument")) is int


def test_number_of_characters():
    assert number_of_characters("Eleven") == 6
    assert number_of_characters("Huh? What?") == 9
    assert number_of_characters("") == 0
    assert type(number_of_characters("Argument")) is int


def test_calculate_ari():
    assert calculate_ari("Calculating ARI is difficult \
    with small samples. This has to do with the calculations.") == 7
    assert calculate_ari("This is the easiest it can get.") == 1
    assert calculate_ari('''
    Two roads diverged in a yellow wood. \
    I took the one less traveled by, and that has \
    made all the difference.
    ''') == 4
