import lab08
from lab08 import peaks, valleys, peaks_and_valleys, data, peak_list, valley_list
import pytest


def test_peaks():
    peaks_outcome = peaks(data)
    data1 = [1, 2, 1, 4, 8, 5, 6, 9]
    data2 = [8, 2, 4, 7, 4, 1, 2, 4]
    data3 = [4, 2, 5, 6, 3, 8, 2, 1]
    # print(peaks(data1), "--------------")
    assert type(peaks_outcome) is list
    assert peaks(data1) == [2, 8]
    assert peaks(data2) == [8, 7]
    assert peaks(data3) == [4, 6, 8]


def test_valleys():
    valleys_outcome = valleys(data)
    data1 = [1, 4, 3, 4, 7, 3, 5, 2]
    data2 = [3, 5, 4, 7, 5, 9, 3, 1]
    data3 = [2, 3, 7, 2, 4, 1, 2, 1]
    assert type(valleys_outcome) is list
    assert valleys(data1) == [1, 3, 3]
    assert valleys(data2) == [4, 5]
    assert valleys(data3) == [2, 1]


def test_peaks_and_valleys():
    peaks_and_valleys_outcome = peaks_and_valleys(peak_list, valley_list)
    peak_list1 = [2, 8]
    valley_list1 = [1, 3, 3]
    peak_list2 = [8, 7]
    valley_list2 = [4, 5]
    peak_list3 = [4, 6, 8]
    valley_list3 = [2, 1]
    assert type(peaks_and_valleys_outcome) is list
    assert peaks_and_valleys(peak_list1, valley_list1) == [2, 8, 1, 3, 3]
    assert peaks_and_valleys(peak_list2, valley_list2) == [8, 7, 4, 5]
    assert peaks_and_valleys(peak_list3, valley_list3) == [4, 6, 8, 2, 1]


def test_image():
    assert type(data) is list
