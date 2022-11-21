from tic_tac_toe import Game
import pytest


def test_game_init():
    game = Game()
    assert game.board == [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]
    # assert isinstance(game, Game)
    # assert type(game.board) is list
    # assert type(game.board[0]) is list
    # assert len(game.board) == 3
    # for i in range(3):
    #     assert len(game.board[i]) == 3
    #     assert ' ' in game.board[i]


def test_repr():
    game = Game()
    assert '|' in game.__repr__()
    assert game.__repr__() == ' | | \n | | \n | | '
    game.move(0, 0, 'X')
    assert game.__repr__() == 'X| | \n | | \n | | '
    game.move(2, 1, 'O')
    assert game.__repr__() == 'X| | \n | | \n |O| '


def test_move():
    game = Game()
    game.move(0, 0, 'X')
    assert game.board[0][0] == 'X'
    game.move(0, 0, 'O')
    assert game.board[0][0] == 'O'
    game.move(1, 0, 'X')
    assert game.board[1][0] == 'X'
    game.move(1, 1, 'O')
    assert game.board[1][1] == 'O'
    with pytest.raises(IndexError):
        game.move(0, 4, ':)')


def test_is_full():
    game = Game()
    assert game.is_full() == False
    game.move(0, 0, 'X')
    assert game.is_full() == False
    for i in range(3):
        for j in range(3):
            game.move(i, j, 'X')
    assert game.is_full() == True


def test_calc_winner():
    game = Game()
    assert game.calc_winner() == None
    # test a full board
    for i in range(3):
        for j in range(3):
            game.move(i, j, 'X')
    assert game.calc_winner() == 'X'
    # test a row
    for i in range(3):
        game.move(0, i, 'O')
    assert game.calc_winner() == 'O'
    # test a column
    for i in range(3):
        game.move(i, 0, '1')
    assert game.calc_winner() == '1'
    # test one diagonal
    for i in range(3):
        game.move(i, i, '2')
    assert game.calc_winner() == '2'
    # test the other diagonal
    game.move(2, 0, 'B')
    game.move(1, 1, 'B')
    game.move(0, 2, 'B')
    assert game.calc_winner() == 'B'


def test_is_game_over():
    game = Game()
    assert game.is_game_over() == False
    # test a full board
    for i in range(3):
        for j in range(3):
            game.move(i, j, 'X')
    assert game.is_game_over() == True
    # test a winner
    game = Game()
    for i in range(3):
        game.move(0, i, 'O')
    assert game.is_game_over() == True
