from lab_18 import sock_generator, sock_sorter


def test_sock_generator():
    assert sock_generator()[0] == ['ankle', 'crew', 'calf', 'thigh']
    # assert sock_generator()[1] == []
    random_socks = sock_generator()[1]
    assert len(random_socks) == 100


def test_sock_sorter():
    # assert sock_sorter() == {}
    sorted_socks = sock_sorter(sock_generator())
    # assert len(sorted_socks) == 4
    assert sum(sorted_socks.values()) == 100
    assert sorted_socks