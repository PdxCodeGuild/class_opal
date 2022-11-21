import lab04_blackjack
from lab04_blackjack import handle_card, get_advice, main
from unittest.mock import patch
import pytest


@patch('builtins.input')
def test_handle_card(mock_input):
    mock_input.return_value = 'k'
    assert handle_card('test', [0]) == [10]
    assert handle_card('test', [5]) == [15]
    assert handle_card('test', [1, 11]) == [11, 21]
    assert handle_card('test', [8, 18]) == [18, 28]

    mock_input.return_value = '4'
    assert handle_card('test', [0]) == [4]
    assert handle_card('test', [10]) == [14]
    assert handle_card('test', [1, 11]) == [5, 15]
    assert handle_card('test', [8, 18]) == [12, 22]

    mock_input.return_value = 'a'
    assert handle_card('test', [0]) == [1, 11]
    assert handle_card('test', [1, 11]) == [2, 12, 12, 22]
    assert handle_card('test', [8, 18]) == [9, 19, 19, 29]

    mock_input.return_value = 'hello :)'
    with pytest.raises(RecursionError):
        handle_card('test', [0])


def test_get_advice():
    assert get_advice([21]) == 'BLACKJACK!'
    assert get_advice([16]) == 'hit'
    assert get_advice([19]) == 'stay'
    assert get_advice([22]) == 'BUST'
    assert get_advice([21, 9]) == 'BLACKJACK!'
    assert get_advice([16, 14]) == 'hit'
    assert get_advice([19, 10]) == 'stay'
    assert get_advice([22, 23]) == 'BUST'
    assert len(get_advice([2, 17])) > 20


@patch('lab04_blackjack.handle_card')
def test_main(mock_hands):
    mock_hands.return_value = [21, 31]
    assert main() == 'BLACKJACK!'
    mock_hands.return_value = [22, 31]
    assert main() == 'BUST'
    mock_hands.return_value = [16]
    assert main() == 'hit'
    mock_hands.return_value = [19]
    assert main() == 'stay'
