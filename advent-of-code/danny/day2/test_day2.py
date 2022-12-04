'''
Additional tests of Advent of Code, Day 2

To use these tests, change the import to match your file name
and method names
'''
from day2 import rps_score_1 as game1, rps_score_2 as game2

TEST_DATA = '''A Y
B X
C Z'''


def test_1():
    assert game1(TEST_DATA) == 15
    # draws
    assert game1('A X') == 4
    assert game1('B Y') == 5
    assert game1('C Z') == 6
    # wins
    assert game1('C X') == 7
    assert game1('A Y') == 8
    assert game1('B Z') == 9
    # loses
    assert game1('B X') == 1
    assert game1('C Y') == 2
    assert game1('A Z') == 3


def test_2():
    assert game2(TEST_DATA) == 12
    # draws
    assert game2('A Y') == 4
    assert game2('B Y') == 5
    assert game2('C Y') == 6
    # wins
    assert game2('A Z') == 8
    assert game2('B Z') == 9
    assert game2('C Z') == 7
    # loses
    assert game2('A X') == 3
    assert game2('B X') == 1
    assert game2('C X') == 2
