data = [1, 2, 3, 4, 5, 6, 7, 6, 5, 4, 5, 6, 7, 8, 9, 8, 7, 6, 7, 8, 9]

def peaks(data: list):
    peaks_indices = []
    for i in range(1,len(data)-1):
        if data[i] > max(data[i - 1], data[i + 1]):
            peaks_indices.append(i)
    return peaks_indices

def valleys(data: list):
    valleys_indices = []
    for i in range(1, len(data) -1):
        if data[i] < min(data[i - 1], data[i + 1]):
            valleys_indices.append(i)
    return valleys_indices

def peaks_and_valleys(data: list):
    peaks_indices = peaks(data)
    valleys_indices = valleys(data)
    peaks_indices.extend(valleys_indices)
    peaks_indices.sort()
    return peaks_indices

print(peaks_and_valleys(data))

def draw_data(data: list):
    for i in range(max(data)):
        drawing_row = ""
        for j in range(len(data)):
            if data[j] >= max(data) - i:
                drawing_row += "X "
            else:
                drawing_row += "  "
        print(drawing_row)            

draw_data(data)

def calculate_interior_water(data: list):
    peaks_indices = peaks(data)
    interior_water = 0
    for i in range(len(peaks_indices) - 1):
        for j in range(peaks_indices[i], peaks_indices[i + 1]):
            interior_water += max(min(data[peaks_indices[i]], data[peaks_indices[i + 1]]) - data[j], 0)
    return interior_water

print(calculate_interior_water(data))

def calculate_end_water(data: list):
    peaks_indices = peaks(data)
    end_water = 0
    if data[-1] > data[-2]:
        for i in range(peaks_indices[-1], len(data)):
            end_water += max(min(data[peaks_indices[-1]], data[-1]) - data[i], 0)
    return end_water

def calculate_start_water(data: list):
    peaks_indices = peaks(data)
    start_water = 0
    if data[0] > data[1]:
        for i in range(0, peaks_indices[0]):
            start_water += max(min(data[peaks_indices[0]], data[0]) - data[i], 0)
    return start_water

total_water = calculate_interior_water(data) + calculate_end_water(data) + calculate_start_water(data)

print(total_water)
