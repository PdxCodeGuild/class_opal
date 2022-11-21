import wcs_lab18
from wcs_lab18 import rand_sock, find_pairs, SOCK_TYPES


def test_rand_sock():
    sock = rand_sock()
    assert len(sock) is 100
    for s in sock:
        assert s in SOCK_TYPES
    assert 'ankle' and 'crew' in sock
   
def test_find_pairs():
    assert type(find_pairs()) == dict
    assert 

# loop over list and test that each item is in SOCK_TYPES
