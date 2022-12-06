from random import choice
# # Lab: Sock Sorter

# You've just finished laundry and your expansive sock collection is in complete disorder. Sort your socks into pairs and pull out any loners.

# 1) Generate a list of 100 random socks, randomly chosen from a set of types: `sock_types = ['ankle', 'crew', 'calf', 'thigh']`

# 2) Find the number of duplicates and loners for each sock type. Hint: dictionaries are helpful here.


# ## Version 2

# Now you have a mix of types **and** colors. Represent socks using tuples containing one color and one type `('black', 'crew')`. Randomly generate these, and then group them into pairs.

# `sock_colors = ['black', 'white', 'blue']`

SOCK_TYPES = ['ankle', 'crew', 'calf', 'thigh']
SOCK_COLORS = ['black', 'white', 'blue']


def sock_generator():
    sock_basket = [choice(SOCK_TYPES) for i in range(100)]
    return sock_basket


def sock_sorter(sock_basket):
    # sock_drawer = dict.fromkeys(SOCK_TYPES, 0)
    sock_drawer = {sock: 0 for sock in SOCK_TYPES}
    socks = sock_basket
    for sock in socks:
        sock_drawer[sock] += 1
    for k in sock_drawer.keys():
        num_dupe = sock_drawer[k]//2
        num_loners = sock_drawer[k] % 2
        sock_drawer[k] = (num_dupe, num_loners)

    return sock_drawer


print(sock_sorter(sock_generator()))
