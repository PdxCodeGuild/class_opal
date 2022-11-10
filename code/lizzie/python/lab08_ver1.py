data = [1, 2, 3, 4, 5, 6, 7, 6, 5, 4, 5, 6, 7, 8, 9, 8, 7, 6, 7, 8, 9]


def peak(data):
    peaks:list = []
    #range dismisses 1st and last index because peaks only look at areas where there are numbers on BOTH sides
    for i in range(1, len(data)-1):
        #Determining whether data is larger than indeces on both sides (peak!)
        if (data[i] > data[i-1] and data[i] > data [i+1]):
            peaks.append(i)
    return peaks


print(peak(data))


def valley(data):
    valleys:list = []
    for i in range(1, len(data)-1):
        if (data[i] < data[i-1] and data[i] < data [i+1]):
            valleys.append(i)
    return valleys


print(valley(data))


def peaks_and_valleys(data: list):
    '''
    Executes both peak and valley functions and sorts the resulting lists by their indeces.
    '''
    peak_index = peak(data)
    valley_index = valley(data)
    indeces:list = peak_index + valley_index
    indeces.sort()
    return indeces


print(peaks_and_valleys(data))


'''
Still working on version 2!
'''

# def marks(data):
#     for i in data:
#         if 


# ## Version 2
# Using the `data` list above, draw the image of `X`'s above.