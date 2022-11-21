from itertools import product
import random

SOCK_TYPES = ['ankle', 'crew', 'calf', 'thigh']


class Sorter:
    def __init__(self):
        self.socks = self.rand_sock()

    def rand_sock(self):
        self.socks = random.choices(SOCK_TYPES, k=100)
        # sock_sorter += random.choices(SOCK_TYPES, k=100)
        return self.socks
# # random.choices(sequence, weights=None, cum_weights=None, k=1)
#         for sock in range(len(SOCK_TYPES)+1):
#             sock_sorter += list(combinations(SOCK_TYPES, sock))
        # print(sock_sorter)
        # itertools.combinations(SOCK_TYPES, 100)

# Sorter.rand_sock(SOCK_TYPES)

# from itertools import combinations
# sample_list = ['a', 'b', 'c']
# list_combinations = list()
# for n in range(len(sample_list) + 1):
#     list_combinations += list(combinations(sample_list, n))
# print(list_combinations)


# Lab: Sock Sorter

# You've just finished laundry and your expansive sock

# collection is in complete disorder. Sort your socks into
# pairs and pull out any loners.

# 1) Generate a list of 100 random socks, randomly
# chosen from a set of types: `sock_types = ['ankle',
# 'crew', 'calf', 'thigh']`

# 2) Find the number of duplicates and loners for each sock
#  type. Hint: dictionaries are helpful here.


# ## Version 2

# Now you have a mix of types **and** colors. Represent socks
# using tuples containing one color and one type
# `('black', 'crew')`. Randomly generate these, and then
# group them into pairs.

# `sock_colors = ['black', 'white', 'blue']`
