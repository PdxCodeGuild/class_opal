from lab_18 import sock_generator, sock_sorter, SOCK_TYPES


def test_sock_generator():
    assert isinstance(sock_generator(), list)
    assert len(sock_generator()) == 100
    for sock in sock_generator():
        assert sock in SOCK_TYPES


# def test_sock_sorter():
#     # assert sock_sorter() == {}
#     sorted_socks = sock_sorter(sock_generator())
#     # assert len(sorted_socks) == 4
#     assert sum(sorted_socks.values()) == 100
#     assert sorted_socks
