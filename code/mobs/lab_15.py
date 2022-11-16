# # Lab 15: Tic-Tac-Toe

# Players take turns placing tokens (a 'O' or 'X') into a 3x3 grid.
# Whoever gets three in a row first wins.

# You will write a **Player** class and **Game** class to model Tic Tac Toe, and a function **main** that models gameplay taking in user inputs through REPL.


class Game:
    def __init__(self):
        self.board = [['X', ' ', 'O'], ['X', ' ', 'X'], ['X', ' ', ' ']]

    def __repr__(self):
        '''Returns a pretty string representation of the game board'''
        board_output = []
        for i, string in enumerate(self.board):
            string = '|'.join(self.board[i])
            board_output.append(string)
        return "\n".join(board_output)

    def move(self):  # , x, y, player):
        '''Place a player's token character string at a given coordinate 
(top-left is 0, 0), x is horizontal position, y is vertical position.'''
        x = 0
        y = 1
        player = 'X'
        self.board[y][x] = player

    def calc_winner(self):
        ''' What token character
string has won or `None` if no one has.'''
        for row in self.board:
            if row[0] == row[1] and row[1] == row[2]:
                if row[0] != ' ':
                    return row[0]
            else:
                continue
        for i, column in enumerate(self.board[0]):
            if column == self.board[1][i] and self.board[2][i] == column:
                if column[0] != ' ':
                    return column[0]
            else:
                continue
        if self.board[0][0] == self.board[1][1] and self.board[2][2] == self.board[1][1]:
            if self.board[0][0] != ' ':
                return self.board[0][0]
        if self.board[0][2] == self.board[1][1] and self.board[2][0] == self.board[1][1]:
            if self.board[0][0] != ' ':
                return self.board[0][0]
        else:
            return None

    def is_full(self):
        '''Returns true if the game board is full.'''
        is_full = True
        for list in self.board:
            if ' ' not in list:
                continue
            else:
                is_full = False

        return is_full


# need to adjust game_over parameters to make sure one if statement isn't taking prority over the other
###########
#############!!!!
    def game_over(self):
        '''Returns true if the game board
is full or a player has won.'''
        if self.is_full() is True:
            return True
        if self.calc_winner() != None:
            return True



game = Game()
# print(game)
# game.move()
# print(game)
game.calc_winner()
# print(game.calc_winner())
# print(game.is_full())
print(game.game_over())
# class Player:
#     def __init__(self, name, token):
#name = player_name
#token = 'X' or 'O'
