import unittest
from string import ascii_lowercase, digits
import sys
sys.path.insert(0, 'code/nick/python/lab09')
import lab09  # nopep8

'''passage taken from an explanation of ARI. All metrics are known.
https://readabilityformulas.com/automated-readability-index.php
sentences = 6, words = 151, characters = 623, ari = 11(10.6)'''

test_book = '''The rule of rhythm in prose is not so intricate. 
Here, too, we write in groups, or phrases, as I prefer to call them, for the prose phrase is greatly longer and is much more nonchalantly uttered than the group in verse; so that not only is there a greater interval of continuous sound between the pauses, but, for that very reason, word is linked more readily to word by a more summary enunciation. 
Still, the phrase is the strict analogue of the group, and successive phrases, like successive groups, must differ openly in length and rhythm. 
The rule of scansion in verse is to suggest no measure but the one in hand; in prose, to suggest no measure at all. 
Prose must be rhythmical, and it may be as much so as you will; but it must not be metrical. 
It may be anything, but it must not be verse.'''


def test_title():
    '''
    test that the title of a file is extracted in title case
    file name must use '_' as separator
    '''
    test_title_path = 'path/path1/path2/path3/rhythm_in_prose.txt'
    assert lab09.title(test_title_path) == 'Rhythm In Prose'
    test_title_path = 'turtle/turtle/turtle/turtles/turtles_all_the_way_down.file'
    assert lab09.title(test_title_path) == 'Turtles All The Way Down'
    test_title_path = 'turtle/turtle/turtle/turtles/turtles-all-the-way-down.txt'
    assert lab09.title(test_title_path) == 'Turtles-All-The-Way-Down'


def test_sentence_counter():
    '''
    test for accurate count of sentences within margin of error
    Sentences must be separated by standard sentence endings. (read: will not work for Cormac McCarthy)
    '''
    assert lab09.sentence_counter(test_book) == 6
    assert lab09.sentence_counter(
        'Does it work with exclamation and question marks? It does!') == 2
    assert lab09.sentence_counter(
        'It does not work correctly if a sentence does not end with proper punctuation* Like with this one here$ Or here') == 1


def test_word_counter():
    '''
    test for accurate count of words within margin of error
    does not work for words separated by '/'
    '''
    assert lab09.word_counter(test_book) == 151
    assert lab09.word_counter('a list of seven words to test') == 7
    assert lab09.word_counter('a list of seven/eight words to test') == 7


def test_char_counter():
    '''
    test for accurate count of letters and numbers within margin of error
    '''
    assert lab09.char_counter(test_book) == 623
    assert lab09.char_counter(ascii_lowercase) == 26
    assert lab09.char_counter(digits) == 10
    assert lab09.char_counter('0 !N-1 /u $2@ M !3 =B_4. e,5/r ?6;s "7*') == 15


def test_ari_calculator():
    '''
    test accurate ari determination
    '''
    assert lab09.ari_calculator(test_book) == 11
    assert lab09.ari_calculator(
        'A shorter passage. Very simple. Low ARI.') == 1
    assert lab09.ari_calculator(
        'Here is presented one diminutive albeit exceedingly verbose passage, condensed, arguably unnecessarily, into a single example of a sentence, alone and solitary.') == 14
