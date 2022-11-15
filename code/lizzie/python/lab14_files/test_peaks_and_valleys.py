# Lab 14: Test Peaks and Valleys

import peaks_and_valleys
from peaks_and_valleys import peak, valley, peaks_and_valleys_fun
# from unittest.mock import patch
# import pytest


def test_peak():
    peaks_and_vals:list = [1, 2, 3, 2]
    # for i in range(len(peaks_and_vallies)):
    #     assert 
    assert peak(peaks_and_vals) == [2] # 3, which is at the index of [2], is a peak.


# def test_peaks_and_valleys_fun():
#     # assert type() is list
#     ...
