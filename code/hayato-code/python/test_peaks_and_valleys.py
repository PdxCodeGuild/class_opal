import lab_8
from lab_8 import peaks, valley, peaks_and_valley, draw_x
import lab_8

data = [1, 2, 3, 4, 5, 6, 7, 6, 5, 4, 5, 6, 7, 8, 9, 8, 7, 6, 7, 8, 9]


def test_peaks():
    assert peaks(data) == [6, 14]

def test_valley():
    assert valley(data) == [9, 17]

def test_peaks_and_valley(check_peaks = [6, 14], check_valley =[9, 17]):
    assert peaks_and_valley(check_peaks, check_valley) == [6, 9, 14, 17]

def test_draw_x():
    assert type(draw_x(data)) == str
