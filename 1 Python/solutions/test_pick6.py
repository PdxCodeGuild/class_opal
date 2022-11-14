import lab05_pick6
from lab05_pick6 import make_ticket, count_matches, play
from unittest.mock import patch


EXPECTED_COST = lab05_pick6.ITERATIONS * lab05_pick6.TICKET_COST


def test_make_ticket():
    ticket = make_ticket()
    assert type(ticket) is list
    assert len(ticket) == 6
    for num in ticket:
        assert num >= 1 and num <= 99


def test_count_matches():
    # ticket = make_ticket()
    ticket1 = [0, 1, 2, 3, 4, 5]
    ticket2 = [1, 2, 3, 4, 5, 6]
    ticket3 = [1, 2, 3, 3, 3, 3]
    assert count_matches(ticket1, ticket2) == 0
    assert count_matches(ticket1, ticket1) == 6
    assert count_matches(ticket2, ticket3) == 3
    assert count_matches(ticket1, ticket3) == 1


def test_play():
    play_outcome = play()
    assert type(play_outcome) is tuple
    assert play_outcome[1] == EXPECTED_COST
    assert play_outcome[0] >= 0
    assert play_outcome[0] <= 27_000_00


@patch('lab05_pick6.count_matches', return_value=3)
def test_play_with_mocked_matches(mocked_count):
    expected = lab05_pick6.PAYOUTS[mocked_count.return_value] * \
        lab05_pick6.ITERATIONS
    assert play() == (expected, EXPECTED_COST)
