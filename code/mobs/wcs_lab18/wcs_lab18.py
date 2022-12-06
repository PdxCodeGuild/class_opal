from itertools import product
import random

SOCK_TYPES = ['ankle', 'crew', 'calf', 'thigh']


def rand_sock():
    sock_list = random.choices(SOCK_TYPES, k=100)
    return sock_list

def find_pairs(sock_list):
    sock_drawer = {}
    print(sock_drawer)
    for sock_type in SOCK_TYPES:
        sock_drawer[sock_type] = sock_list.count(sock_type)
    return sock_drawer
