# Lab 8 - Peaks and Valleys, Version 1

data_dict = {
    0: 1,
    1: 2,
    2: 3,
    3: 4,
    4: 5,
    5: 6,
    6: 7,
    7: 6,
    8: 5,
    9: 4,
    10: 5,
    11: 6,
    12: 7,
    13: 8,
    14: 9,
    15: 8,
    16: 7,
    17: 6,
    18: 7,
    19: 8,
    20: 9
}


# Creates a function to return a list of the peaks and valleys in order of appearance in the original data
def peaks_and_valleys(data):
    peaks_and_valleys_list = []
    for key in data:
        try:
            if data[key] == data[key + 2]:
                peaks_and_valleys_list.append(key + 1)   
        except:
            break    
    print(peaks_and_valleys_list)


peaks_and_valleys(data_dict)

# Lab 8 - Peaks and Valleys, Version 2 (using the data list above, draw the image of X's above)

data = [1, 2, 3, 4, 5, 6, 7, 6, 5, 4, 5, 6, 7, 8, 9, 8, 7, 6, 7, 8, 9]
blank = '   '
x = 'X  '
graph = ''

def graph(list):
    elevation = ''
    for num in range(9):
        if num == 9:
            elevation += x
        else:
            elevation += blank

graph(data)

# for num in range(9):
#     for num in data:
#         if num == 9:
#             graph += x
#         else:
#             graph += blank
#         print(graph)




# for num in data:
#     if num == 9:
#         print(x)
#     else:
#         print(blank)


#for i in range(9):
# for num in data:
#     if num == 9:
#         graph += x
#     elif num != 9:
#         graph += blank
# print(graph)

# for num in data:
#     if num == 8:
#         graph += x
#     elif num != 8 or 9:
#         graph += blank
# print(graph)

# for num in data:
#     if num == 7:
#         graph += x
#     elif num != 7 or 8 or 9:
#         graph += blank
# print(graph)

# for num in data:
#     if num == 6:
#         graph += x
#     elif num != 6 or 7 or 8 or 9:
#         graph += blank
# print(graph)

# for num in data:
#     if num == 5:
#         graph += x
#     elif num != 5 or 6 or 7 or 8 or 9:
#         graph += blank
# print(graph)

# for num in data:
#     if num == 4:
#         graph += x
#     elif num != 4 or 5 or 6 or 7 or 8 or 9:
#         graph += blank
# print(graph)

# for num in data:
#     if num == 3:
#         graph += x
#     elif num != 3 or 4 or 5 or 6 or 7 or 8 or 9:
#         graph += blank
# print(graph)

# for num in data:
#     if num == 2:
#         graph += x
#     elif num != 2 or 3 or 4 or 5 or 6 or 7 or 8 or 9:
#         graph += blank
# print(graph)

# for num in data:
#     if num == min(data):
#         graph += x
#     elif num != min(data) or 2 or 3 or 4 or 5 or 6 or 7 or 8 or 9:
#         graph += blank
# print(graph)


#continue
 #   num = num - 1
  #  counter -= 1
   # continue

        # )for num in data:
        # if num != 9:
        #     print(blank)
        # else:
        #     print(x)
        #     # except:
            #     print(blank)
        # elif num == 8:
        #     try:
        #         print(x)
        #     except:
        #         print(blank)
        # elif num == 7:
        #     try:
        #         print(x)
        #     except:
        #         print(blank)
        # elif num == 6:
        #     try:
        #         print(x)
        #     except:
        #         print(blank)
        # elif num == 5:
        #     try:
        #         print(x)
        #     except:
        #         print(blank)
        # elif num == 4:
        #     try:
        #         print(x)
        #     except:
        #         print(blank)
        # elif num == 3:
        #     try:
        #         print(x)
        #     except:
        #         print(blank)
        # elif num == 2:
        #     try:
        #         print(x)
        #     except:
        #         print(blank)
        # else:
        #     try:
        #         print(x)
        #     except:
        #         print(blank)

    # mountains = num * 'X'
    # print(mountains)

#                                                       X                 X
#                                                    X  X  X           X  X
#                               X                 X  X  X  X  X     X  X  X
#                            X  X  X           X  X  X  X  X  X  X  X  X  X
#                         X  X  X  X  X     X  X  X  X  X  X  X  X  X  X  X
#                      X  X  X  X  X  X  X  X  X  X  X  X  X  X  X  X  X  X
#                   X  X  X  X  X  X  X  X  X  X  X  X  X  X  X  X  X  X  X
#                X  X  X  X  X  X  X  X  X  X  X  X  X  X  X  X  X  X  X  X
#             X  X  X  X  X  X  X  X  X  X  X  X  X  X  X  X  X  X  X  X  X
# >>> data = [1, 2, 3, 4, 5, 6, 7, 6, 5, 4, 5, 6, 7, 8, 9, 8, 7, 6, 7, 8, 9]