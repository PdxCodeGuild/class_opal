from lab08_v4 import peaks, valleys, peaks_and_valleys, draw_data,\
     calculate_interior_water, calculate_end_water, calculate_start_water

DATA = [1, 2, 3, 4, 5, 6, 7, 6, 5, 4, 5, 6, 7, 8, 9, 8, 7, 6, 7, 8, 9]
DRAWING = """                            X O O O O O X
                          X X X O O O X X
            X O O O O O X X X X X O X X X
          X X X O O O X X X X X X X X X X
        X X X X X O X X X X X X X X X X X
      X X X X X X X X X X X X X X X X X X
    X X X X X X X X X X X X X X X X X X X
  X X X X X X X X X X X X X X X X X X X X
X X X X X X X X X X X X X X X X X X X X X"""

def test_peaks(data=DATA):
    peaks_indices = peaks(data)
    assert peaks_indices == [6, 14]
    assert peaks([1,1,1]) == []

def test_valleys(data=DATA):
    valleys_indices = valleys(data)
    assert valleys_indices == [9, 17]

def test_peaks_and_valleys(data=DATA):
    peaks_indices = peaks_and_valleys(data)
    assert peaks_indices == [6, 9, 14, 17]

def test_draw_data(data=DATA):
    data_drawing = draw_data(data)
    # assert data_drawing == DRAWING
    assert draw_data([1,1,1]) == "X X X"

def test_calculate_interior_water(data=DATA):
    interior_water = calculate_interior_water(data)
    assert interior_water == 9

def test_calculate_end_water(data=DATA):
    end_water = calculate_end_water(data)
    assert end_water == 9

def test_calculate_start_water(data=DATA):
    start_water = calculate_start_water(data)
    assert start_water == 0