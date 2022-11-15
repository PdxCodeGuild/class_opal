# # Lab 15: Tic-Tac-Toe 

# Players take turns placing tokens (a 'O' or 'X') into a 3x3 grid.
# Whoever gets three in a row first wins.

# You will write a **Player** class and **Game** class to model Tic Tac Toe, and a function **main** that models gameplay taking in user inputs through REPL.


class Game:
    def __init__(self):
        self.board = [[' ',' ',' '],[' ',' ',' '],[' ',' ',' ']]


    def __repr__(self):
        '''Returns a pretty string representation of the game board'''
        new_board = []
        for i, string in enumerate(self.board):
            string = '|'.join(self.board[i])
            new_board.append(string)
        return "\n".join(new_board)


    def move(self): # , x, y, player):
        '''Place a player's token character string at a given coordinate 
(top-left is 0, 0), x is horizontal position, y is vertical position.'''
        x = 0
        y = 1
        player = 'X'
        self.board[y][x] = player

# ```py
# >>> board.move(2, 1, player_1)
#  | | 
#  | |X
#  | | 
# ```

        ...


    def calc_winner(self):
        ''' What token character
string has won or `None` if no one has.'''
# ```py
# X| | 
# O|X|O
#  | |X
# >>> board.calc_winner()
# X
# ```

        ...


    def is_full(self):
        '''Returns true if the game board is full.'''
        ...
# ```py
# X|O|X
# X|X|O
# O|O|X
# >>> board.is_full()
# True
# ```


    def game_over(self):
        '''Returns true if the game board
is full or a player has won.'''
        ...
# ```py
# X|O|X
# X|X|O
# O|O|X
# >>> board.is_game_over()
# True

# X|O|
#  | |X
#  | |
# >>> board.is_game_over()
# False
# ```


game = Game()
print(game)
game.move()
print(game)

# class Player:
#     def __init__(self, name, token):
        #name = player_name
        #token = 'X' or 'O'