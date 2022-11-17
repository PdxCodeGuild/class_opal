# Lab 14: Test ARI

import ARI
from ARI import calculate_ari, number_of_sentences,  number_of_words, number_of_characters
from unittest.mock import patch


def test_number_of_sentences():
    assert number_of_sentences() == 2
    assert type(number_of_sentences()) is int


def test_number_of_words():
    assert number_of_words() == 9
    assert type(number_of_words()) is int


def test_number_of_characters():
    assert number_of_characters() == 41
    assert type(number_of_characters()) is int


def test_calculate_ari():
    assert calculate_ari() == [2, 9, 2.0, 41.0]
    assert type(calculate_ari()) is list
