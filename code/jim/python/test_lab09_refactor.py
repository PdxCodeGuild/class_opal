from random import randint

from lab09_refactor import count_sentences, calculate_ari, ARI_SCALE


def test_calculate_ari():
    assert calculate_ari(0,5,10) == 1
    assert calculate_ari(0,0,0) == 1
    assert calculate_ari(1000,100,10) == 14
    character_count = randint(1,100_000)
    assert calculate_ari(character_count,character_count/5,character_count/50) <= 14


def test_count_sentences():
    assert count_sentences("Hi. I'm Jim.") == 2
    assert count_sentences("I'm in the U.S. I'm Jim.") == 2
    assert count_sentences("Hi!") == 1
    assert count_sentences("Where are you?") == 1
    assert count_sentences("This is not a sentence") == 0


def test_ARI_SCALE():
    assert ARI_SCALE[1]['grade_level'] == 'Kindergarten' 
