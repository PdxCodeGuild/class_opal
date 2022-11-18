import lab09
from lab09 import find_ari, get_counts
import pytest


ari_function = find_ari(148661, 31447, 1638)


def test_find_ari():
    assert ari_function == [11, '10th Grade', '15-16']
    assert type(ari_function[0]) == int
    assert type(ari_function[1]) == str
    assert type(ari_function[2]) == str


def test_get_counts():
    assert get_counts() == [148661, 31447, 1638]
    assert type(get_counts()[0]) == int
    assert type(get_counts()[1]) == int
    assert type(get_counts()[2]) == int
