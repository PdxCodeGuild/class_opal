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