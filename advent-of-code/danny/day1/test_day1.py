'''
Additional tests of Advent of Code, Day 1

To use these tests, change the import to match your file name
and method names
'''

from day1 import find_max_calories as find_max, find_top_3_total as find_top_3

TEST_LIST_1 = '''1
2
3

1
1

1

3'''

TEST_LIST_2 = '''1
2
3

1
1

100'''


def test_find_max_calories():
    assert find_max(TEST_LIST_1) == 6
    assert find_max(TEST_LIST_2) == 100


def test_find_top_3_total():
    assert find_top_3(TEST_LIST_1) == 11
    assert find_top_3(TEST_LIST_2) == 108
