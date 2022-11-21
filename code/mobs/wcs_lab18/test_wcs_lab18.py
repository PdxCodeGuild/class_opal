import wcs_lab18
from wcs_lab18 import rand_sock, find_pairs, SOCK_TYPES


def test_rand_sock():
    sock = rand_sock()
    assert len(sock) is 100
    for s in sock:
        assert s in SOCK_TYPES
    assert 'ankle' and 'crew' in sock

def test_find_pairs():
    assert type(find_pairs([])) == dict
    test_data = ['ankle', 'ankle', 'crew', 'long', 'thigh', 'more']
    sock_drawer = find_pairs(test_data)
    #asserting that values in dict are ints.
    for item in sock_drawer:
        assert type(sock_drawer[item]) == int
    assert sock_drawer['ankle'] == 2
    assert sock_drawer['crew'] == 1
