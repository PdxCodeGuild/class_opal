import sys
sys.path.insert(0, 'code/nick/python')
import lab08  # nopep8
data1 = [1, 2, 3, 2, 3]
data2 = [2, 3, 4, 3, 4, 3, 4, 3]


def test_peaks():
    '''
    test that the correct indeces are being returned as peaks
    '''
    assert lab08.peaks(data1) == [2]
    assert lab08.peaks(data2) == [2, 4, 6]


def test_valleys():
    '''
    test that the correct indeces are being returned as valleys
    '''
    assert lab08.valleys(data1) == [3]
    assert lab08.valleys(data2) == [3, 5]


def test_mountains():
    '''
    test that there are the correct number of peaks represented,
    that the bottom line is filled in with an X for every item in data,
    that the mountains have an amount of layers equal to the highest number in the data
    '''
    count = lab08.mountains(data1)[1][0].count('X')
    assert count == 2
    assert len(lab08.mountains(data1)[1]) == max(data1)
    count = lab08.mountains(data1)[1][max(data1)-1].count('X')
    assert count == len(data1)

    count = lab08.mountains(data2)[1][0].count('X')
    assert count == 3
    assert len(lab08.mountains(data2)[1]) == max(data2)
    count = lab08.mountains(data2)[1][max(data2)-1].count('X')
    assert count == len(data2)
