data = [1, 2, 3, 4, 5, 6, 7, 6, 5, 4, 5, 6, 7, 8, 9, 8, 7, 6, 7, 8, 9]

def peaks(data):
    peaks = []
    for i, num in enumerate(data[0:-1]):
        if num > data[i + 1] and num > data[i - 1]: 
            peaks.append(i)
    return peaks


def valley(data):
    valley = []
    for i, num in enumerate(data[0:-1]):
        if i == 0:
            pass
        elif num < data[i + 1] and num < data[i - 1]: 
            valley.append(i)
    return valley


def peaks_and_valley(peaks,valley):
    peaks_and_valley_list = peaks + valley
    peaks_and_valley_list.sort()
    print(peaks_and_valley_list)

peaks_and_valley(peaks(data),valley(data))

def draw_x(data):
    for i in range(max(data)):
        xs = ""
        for p in range(len(data)):
            if data[p] >= max(data) - i:
                xs += "X "
            else:
                xs += "  "
        print(xs)            

draw_x(data)
