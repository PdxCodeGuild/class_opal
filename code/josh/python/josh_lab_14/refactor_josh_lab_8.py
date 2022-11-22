# Lab 8 - Peaks and Valleys, Version 1

data = [1, 2, 3, 4, 5, 6, 7, 6, 5, 4, 5, 6, 7, 8, 9, 8, 7, 6, 7, 8, 9]

# Creates a function to return a list of the peaks and valleys in order of appearance in the original data
def peaks_and_valleys(data):
    peaks_and_valleys_list = []
    for i in range(len(data)):
        try:
            if data[i] == data[i + 2]:
                peaks_and_valleys_list.append(i + 1)   
        except:
            break    
    return (peaks_and_valleys_list)
    # print(peaks_and_valleys_list)

print(peaks_and_valleys(data))



# Lab 8 - Peaks and Valleys, Version 2 (using the data list above, draw the image of X's above)

data = [1, 2, 3, 4, 5, 6, 7, 6, 5, 4, 5, 6, 7, 8, 9, 8, 7, 6, 7, 8, 9]
blank = '   '
x = 'X  '

# Iterates a loop equal to the greatest value in 'data' (to graph 'x'/'blank' peaks/valleys no higher/lower than list values)
for i in range(max(data)):
    graph = ''
# Iterates a loop equal to the number of elements in 'data' (to graph 'x'/'blank' peaks/valleys no wider/narrower than # of list indices)    
    for num in range(len(data)):
# Graphs 'x' if index of 'data' >= max element in 'data' minus current loop iteration, else graphs 'blank' (shifts peaks/valleys by 1 with each iteration) 
        if data[num] >= max(data) - i:
            graph += x
        else:
            graph += blank
    print(graph)