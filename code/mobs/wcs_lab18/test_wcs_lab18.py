import wcs_lab18
from wcs_lab18 import SOCK_TYPES, Sorter


def test_socks_sorter():
    sorter = Sorter()
    assert len(sorter.rand_sock()) is 100
# loop over list and test that each item is in SOCK_TYPES
