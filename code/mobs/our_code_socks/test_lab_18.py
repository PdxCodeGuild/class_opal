from lab_18v2 import sock_generator, sock_sorter, SOCK_TYPES, SOCK_COLORS
from itertools import product


def test_sock_generator():
    assert isinstance(sock_generator(), list)
    for item in sock_generator():
        assert type(item) == tuple
    assert len(sock_generator()) == 100
    for sock in sock_generator():
        assert sock[0] in SOCK_TYPES and sock[1] in SOCK_COLORS


def test_sock_sorter():
    # assert set(sock_sorter(sock_generator()).keys) == set(product(
    #     SOCK_TYPES, SOCK_COLORS))
    assert type(sock_sorter([])) == dict
    sorted_socks = sock_sorter([('crew', 'blue'), ('crew', 'blue')])
    assert len(sorted_socks) == len(list(product(SOCK_TYPES, SOCK_COLORS)))
    count = 0
    # print(sorted_socks)
    for sock in sorted_socks.values():
        # print(sock)
        count += sock[0]*2+sock[1]
    assert count == 2
    # assert sum(sorted_socks.values()) == 100
    # for v in sorted_socks.values():
    #     assert type(v) == tuple
