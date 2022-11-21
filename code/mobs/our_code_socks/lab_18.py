from random import choice
# # Lab: Sock Sorter

# You've just finished laundry and your expansive sock collection is in complete disorder. Sort your socks into pairs and pull out any loners.

# 1) Generate a list of 100 random socks, randomly chosen from a set of types: `sock_types = ['ankle', 'crew', 'calf', 'thigh']`

# 2) Find the number of duplicates and loners for each sock type. Hint: dictionaries are helpful here.


# ## Version 2

# Now you have a mix of types **and** colors. Represent socks using tuples containing one color and one type `('black', 'crew')`. Randomly generate these, and then group them into pairs.

# `sock_colors = ['black', 'white', 'blue']`

SOCK_TYPES = ['ankle', 'crew', 'calf', 'thigh']


def sock_generator():
    sock_basket = [choice(SOCK_TYPES) for i in range(100)]
    return sock_basket


def sock_sorter(random_socks):
    # sock_drawer = dict.fromkeys(SOCK_TYPES, 0)
    sock_drawer = {sock: 0 for sock in random_socks[0]}
    socks = random_socks[1]
    for sock in socks:
        sock_drawer[sock] += 1
    return sock_drawer
