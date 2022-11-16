import sys
sys.path.insert(0, 'code/nick/python')
import lab08  # nopep8
data1 = [1, 2, 3, 2, 3]
data2 = [2, 3, 4, 3, 4, 3, 4, 3]


def test_peaks():
    assert lab08.peaks(data1) == [2]
    assert lab08.peaks(data2) == [2, 4, 6]


def test_valleys():
    assert lab08.valleys(data1) == [3]
    assert lab08.valleys(data2) == [3, 5]
