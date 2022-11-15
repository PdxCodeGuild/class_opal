# Lab 14: Test Peaks and Valleys

import peaks_and_valleys
from peaks_and_valleys import peak, valley, peaks_and_valleys_fun, printxmarkings


def test_peak():
    pav_list:list = [3, 4, 3, 4, 3]
    #peaks are at indeces of 1 and 3 (aka 4 and 4.)
    assert peak(pav_list) == [1, 3]
    assert peak(pav_list) > [0, 2, 4]


def test_valley():
    pav_list:list = [1, 2, 1, 0, 1]
    assert valley(pav_list) == [3]
    # comparing just the ints by using their index
    assert pav_list[valley(pav_list)[0]] < pav_list[2]
    pav_list:list = [2, 1, 2, 0, 1, 2]
    assert valley(pav_list) == [1, 3]
    assert valley(pav_list) < [2]
    assert pav_list[valley(pav_list)[0]] < pav_list[0]


def test_peaks_and_valleys_fun():
    data:list = [1, 0, 1, 2, 1]
    assert peaks_and_valleys_fun(data) == [1, 3]
    # confirming that sorting works by flipping the values in the list
    data:list = [1, 2, 1, 0, 1]
    assert peaks_and_valleys_fun(data) == [1, 3]


def test_printxmarkings():
    data:list = [1, 0, 1, 0, 1]
    #testing that it's printing a string with 'X' to represent the int 1
    assert printxmarkings(data) == 'X X X'
    assert type(printxmarkings(data)) is str