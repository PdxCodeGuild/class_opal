data = [1, 2, 3, 4, 5, 6, 7, 6, 5, 4, 5, 6, 7, 8, 9, 8, 7, 6, 7, 8, 9]


def peaks(data):
    peaks = []
    for i, d in enumerate(data):
        if i == 0 or i == (len(data)-1):
            continue
        if d > data[i-1] and d > data[i+1]:
            peaks.append(i)
    
    return peaks
        

def valleys(data):
    valleys = []
    for i, d in enumerate(data):
        if i == 0 or i == (len(data)-1):
            continue
        if d < data[i-1] and d < data[i+1]:
            valleys.append(i)
    
    return valleys
    

def mountains(data):
    ...
    data.sort(reverse=True)
    data_set = (data)

def flood():
    ...


peaks = peaks(data)
valleys = valleys(data)
points_of_interest = peaks + valleys
points_of_interest.sort()

print(f'''
Peaks: {peaks}
Valleys: {valleys}
POI: {points_of_interest}''')
print(set(data))