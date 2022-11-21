# peaks - Returns the indices of peaks. A peak has a lower number on both the left and the right.

# valleys - Returns the indices of 'valleys'. A valley is a number with a higher number on both the left and the right.

# peaks_and_valleys - uses the above two functions to compile a single list of the peaks and valleys in order of appearance in the original data.
data = [1, 2, 3, 4, 5, 6, 7, 6, 5, 4, 5, 6, 7, 8, 9, 8, 7, 6, 7, 8, 9]
peak_list = []
valley_list = []
def peaks(data):
    # peak_list = []
    for i in range(len(data) -1):
        if data[i-1] < data[i] and data[i+1] < data[i]:
            # return data[i]
            peak_list.append(data[i])
    print("peaks: ", peak_list)
peaks(data)

def valleys(data):
    for i in range(len(data) -1):
        if data[i-1] > data[i] and data[i+1] > data[i]:
            valley_list.append(data[i])
    print("valleys: ", valley_list)
valleys(data)

def peaks_and_valleys(peak_list, valley_list):
    return (peak_list + valley_list)
print(peaks_and_valleys(peak_list, valley_list))

def image(data):
    str1 = ''
    str2 = ''
    str3 = ''
    str4 = ''
    str5 = ''
    str6 = ''
    str7 = ''
    str8 = ''
    str9 = ''
    for d in data:
        if d >= 9:
            str1 += "X"
        else:
            str1 += " "
    for e in data:
        if e >= 8:
            str2 += "X"
        else: 
            str2 += " "
    for f in data:
        if f >= 7:
            str3 += "X"
        else:
            str3 += " "
    for g in data:
        if g >= 6:
            str4 += "X"
        else:
            str4 += " "
    for h in data:
        if h >= 5:
            str5 += "X"
        else:
            str5 += " "
    for i in data:
        if i >= 4:
            str6 += "X"
        else:
            str6 += " "
    for j in data:
        if j >= 3:
            str7 += "X"
        else:
            str7 += " "
    for k in data:
        if k >= 2:
            str8 += "X"
        else:
            str8 += " "
    for l in data:
        if l >= 1:
            str9 += "X"
        else:
            str9 += " "
    
    print(str1)
    print(str2)
    print(str3)
    print(str4)
    print(str5)
    print(str6)
    print(str7)
    print(str8)
    print(str9)
image(data)