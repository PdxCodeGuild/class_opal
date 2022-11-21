from random import choice
from itertools import product

SOCK_TYPES = ['ankle', 'crew', 'calf', 'thigh']
SOCK_COLORS = ['black', 'white', 'blue']


def sock_generator():
    sock_basket = [(choice(SOCK_TYPES), choice(SOCK_COLORS))
                   for i in range(100)]
    return sock_basket


def sock_sorter(sock_basket):
    sock_drawer = {sock: 0 for sock in product(SOCK_TYPES, SOCK_COLORS)}
    for sock in sock_basket:
        sock_drawer[sock] += 1
    sock_drawer = {k: (sock_drawer[k]//2, sock_drawer[k] % 2)
                   for k in sock_drawer}

    return sock_drawer


print(sock_sorter(sock_generator()))
