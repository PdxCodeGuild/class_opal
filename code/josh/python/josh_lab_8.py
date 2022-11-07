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


# Data	1	2	3	4	5	6	7	6	5	4	5	6	7	8	9	8	7	6	7	8	9
# Index	0	1	2	3	4	5	6	7	8	9	10	11	12	13	14	15	16	17	18	19	20
# POI							P			V					P			V			
# Example I/O:

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

# Lab 8 - Peaks and Valleys, Version 2
# Using the data list above, draw the image of X's above.

# data = {
#     1: 0,
#     2: 1,
#     3: 2,
#     4: 3,
#     5: 4,
#     6: 5,
#     7: 6,
#     6: 7,
#     5: 8,
#     4: 9,
#     15: 10,
#     16: 11,
#     17: 12,
#     18: 13,
#     19: 14,
#     18: 15,
#     17: 16,
#     16: 17,
#     17: 18,
#     18: 19,
#     29: 20
# }