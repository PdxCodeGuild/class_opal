# data:list = [1, 2, 3, 4, 5, 6, 7, 6, 5, 4, 5, 6, 7, 8, 9, 8, 7, 6, 7, 8, 9]


def peak(data):
    peaks:list = []
    #range dismisses 1st and last index because peaks only look at areas where there are numbers on BOTH sides
    for i in range(1, len(data)-1):
        #Determining whether data is larger than indeces on both sides (peak!)
        if (data[i] > data[i-1] and data[i] > data [i+1]):
            peaks.append(i)
    return peaks


def valley(data):
    valleys:list = []
    for i in range(1, len(data)-1):
        if (data[i] < data[i-1] and data[i] < data [i+1]):
            valleys.append(i)
    return valleys


# print(valley(data))


def peaks_and_valleys_fun(data: list):
    '''
    Executes both peak and valley functions and sorts the resulting lists by their indeces.
    '''
    indeces:list = peak(data) + valley(data)
    indeces.sort()
    return indeces


# print(peaks_and_valleys_fun(data))
# data:list = [1, 0, 1, 2, 1]


#Using (max(data)) to cycle through nine times (which is the maximum)
def printxmarkings(data):
    # print(max(data))

    for i in range(max(data)):
        xmarks = ''
        for index in range(len(data)):
            #subtracting i each time to lower the index we're working with so this if statement runs.
            if data[index] >= max(data) - i:
                xmarks += 'X'
            else:
                xmarks += ' '
        print(xmarks)
    return xmarks


# printxmarkings(data)