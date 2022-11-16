# # Lab 15: Tic-Tac-Toe


class Player:
    def __init__(self, name, token):
        self.name = name
        self.token = token


    def __str__(self) -> str:
        return self.name


class Game:
    def __init__(self):
        self.board = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]


    def __repr__(self):
        '''Returns a pretty string representation of the game board'''
        board_output = []
        for i, string in enumerate(self.board):
            string = '|'.join(self.board[i])
            board_output.append(string)
        return "\n".join(board_output)


    def move(self, x, y, player):
        '''Place a player's token character string at a given coordinate 
(top-left is 0, 0), x is horizontal position, y is vertical position.'''
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
            if self.board[0][2] != ' ':
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


    def is_game_over(self):
        '''Returns true if the game board
is full or a player has won.'''
        if self.is_full() is True:
            return True
        if self.calc_winner() is not None:
            return True
        return False


def game_setup():
    piece_list = ['X', 'O']
    player_1_name = input("Enter a name for Player 1: ")
    while True:
        player_1_piece = input("Choose between 'X' and 'O': ").upper()
        if player_1_piece in piece_list:
            break
        else:
            print("Your choice is invalid.")
    for i, piece in enumerate(piece_list):
        if player_1_piece == piece:
            #pops chosen piece and leaves only the other option 
            piece_list.pop(i)
    player_2_name = input("Enter a name for Player 2: ")
    player_2_piece = piece_list[0]
    player_1 = Player(player_1_name, player_1_piece)
    print(player_1.name, player_1.token)
    player_2 = Player(player_2_name, player_2_piece)
    print(player_2.name, player_2.token)
    game = Game()
    return player_1, player_2, game


def player_move(player, game):
    print(f"{player}'s turn.")
    while True:
        player_move_list = []
        player_move = input("Enter 2 coordinates (left to right 0, 1, 2 & top to bottom 0, 1, 2): ")
        for n in player_move:
            player_move_list.append(int(n))
        if game.board[player_move_list[0]][player_move_list[1]] != ' ':
            print("This space is full.")
        else:
            break
    game.move(player_move_list[1], player_move_list[0], player.token)


def gameplay(game_setup):
    player_1, player_2, game = game_setup
    player_1_turn = True
    loser = [player_1, player_2]
    while not game.is_game_over():
        player_turn = player_1 if player_1_turn else player_2
        player_move(player_turn, game)
        player_1_turn = not player_1_turn
        print(game)
    winner = game.calc_winner()
    if winner == None:
        return "It's a Tic-Tac-Tie."
    else:
        loser.remove(player_turn)
        return f"{player_turn} Tic-Tac-Terminated {loser[0]}!"


print(gameplay(game_setup()))