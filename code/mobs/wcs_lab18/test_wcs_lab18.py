import wcs_lab18
from wcs_lab18 import SOCK_TYPES, Sorter

def test_socks_sorter():
    sorter = Sorter
    assert type(SOCK_TYPES) is list
    assert len(SOCK_TYPES) is 4
    assert len(sorter.rand_sock) is 100

