data = [1, 2, 3, 4, 5, 6, 7, 6, 5, 4, 5, 6, 7, 8, 9, 8, 7, 6, 7, 8, 9]
# data = [1, 2, 3, 2, 3]


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
    ''''''
    lists = []
    highest_peak = max(data)
    for num in reversed(range(1, highest_peak+1)):
        string_of_chars = ' ' * len(data)
        list_of_chars = list(string_of_chars)
        for i, d in enumerate(data):
            if d >= num:
                list_of_chars[i] = 'X'

        lists.append(list_of_chars)
    output_string = ""
    for list_chars in lists:
        output_string += " ".join(list_chars) + '\n'

    # print(output_list) #test
    return output_string, lists  # lists here only for test


def flood():
    '''
    "floods" the valleys with Os
    '''
    ...


def present_data(data):
    data_string = ""
    for d in data:
        data_string += str(d)

    data_string = " ".join(data_string)
    peaks_list = peaks(data)
    valleys_list = valleys(data)
    points_of_interest = peaks_list + valleys_list
    points_of_interest.sort()
    return f'''
{mountains(data)[0]}
{data_string}
Peaks: {peaks_list}
Valleys: {valleys_list}
POI: {points_of_interest}
'''


if __name__ == '__main__':
    print(present_data(data))
