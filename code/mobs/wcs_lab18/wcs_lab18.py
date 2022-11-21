from itertools import product
import random

SOCK_TYPES = ['ankle', 'crew', 'calf', 'thigh']


def rand_sock():
    sock_list = random.choices(SOCK_TYPES, k=100)
    return sock_list

def find_pairs():
    sock_drawer = {}
    print(sock_drawer)
    for sock_type in SOCK_TYPES:
        sock_drawer[sock_type] = sock_type
    return sock_drawer

        # {sock_type: count}

print(find_pairs())


# Find number of duplications and loners for each sock type. 
# Sort your socks into pairs and pull out any loners.

# 2) Find the number of duplicates and loners for each sock
#  type. Hint: dictionaries are helpful here.


# ## Version 2

# Now you have a mix of types **and** colors. Represent socks
# using tuples containing one color and one type
# `('black', 'crew')`. Randomly generate these, and then
# group them into pairs.

# `sock_colors = ['black', 'white', 'blue']`



# from itertools import combinations
# sample_list = ['a', 'b', 'c']
# list_combinations = list()
# for n in range(len(sample_list) + 1):
#     list_combinations += list(combinations(sample_list, n))
# print(list_combinations)
