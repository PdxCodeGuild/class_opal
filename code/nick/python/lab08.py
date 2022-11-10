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
    

list_of_lists =[]


def mountains(data, lists):
    highest_peak = max(data)
    for num in reversed(range(1, highest_peak+1)):
        string_of_chars = ' ' * len(data)
        list_of_chars = list(string_of_chars)
        for i, d in enumerate(data):
            if d >= num:
                list_of_chars[i] = 'X'
        
        lists.append(list_of_chars)
    output_list = ""
    for list_chars in lists:
        output_list += " ".join(list_chars) + '\n'

    data_string = ""
    for d in data:
        data_string += str(d)
        
    data_string = " ".join(data_string)
    # print(output_list) #test
    return f'''
{output_list}
{data_string}
'''
    


        

def flood():
    ...


peaks = peaks(data)
valleys = valleys(data)
points_of_interest = peaks + valleys
points_of_interest.sort()
mountains = mountains(data, list_of_lists)

print(f'''
{mountains}
Peaks: {peaks}
Valleys: {valleys}
POI: {points_of_interest}
''')