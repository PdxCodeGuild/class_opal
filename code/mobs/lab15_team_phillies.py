"""
Lab15: Tic-Tac-Toe 11.16.22 by Team Phillies
"""
BOARD_CORDS = {(0, 0): 0, (0, 1): 2, (0, 2): 4, (1, 0): 6, (1, 1): 8, (1, 2): 10, (2, 0): 12, (2, 1): 14, (2, 2): 16}


class Player:
    """A simple model of a player """

    def __init__(self, name: str, token: str):
        """initialize Player class with name, token"""
        self.name = name
        self.token = token

    def __str__(self) -> str:
        """create string representation of Player class"""
        return self.name


class Game:
    """A simple model of a tic-tac-toe game"""

    def __init__(self, player1: Player, player2: Player):
        """initialize Game class with 2 players and one board"""
        self.player1 = player1
        self.player2 = player2
        self.board = {player1: [], player2: []}

    def calc_winner(self) -> Player | None:

        winning_list = [
            [(0, 0), (0, 1), (0, 2)],
            [(1, 0), (1, 1), (1, 2)],
            [(2, 0), (2, 1), (2, 2)],
            [(0, 0), (1, 0), (2, 0)],
            [(0, 1), (1, 1), (2, 1)],
            [(0, 2), (1, 2), (2, 2)],
            [(0, 0), (1, 1), (2, 2)],
            [(2, 0), (1, 1), (0, 2)]
        ]
        for win in winning_list:
            if set(win).issubset(self.board[self.player1]):
                return self.player1
            elif set(win).issubset(self.board[self.player2]):
                return self.player2

    def __repr__(self):
        board_rep = " | | \n | | \n | | "
        for coord in BOARD_CORDS.keys():
            if coord in self.board[self.player1]:
                board_rep = board_rep[0:BOARD_CORDS[coord]] + \
                    "X" + board_rep[BOARD_CORDS[coord] + 1:]
            elif coord in self.board[self.player2]:
                board_rep = board_rep[0:BOARD_CORDS[coord]] + \
                    "0" + board_rep[BOARD_CORDS[coord] + 1:]
        return board_rep

    def move(self, x, y, player):
        x, y = int(x), int(y)
        z = (x, y)
        self.board[player].append(z)

    def check_move(self, x, y):
        try:
            x, y = int(x), int(y)
        except ValueError:
            print("Please choose valid coordinates e.g. (2,1) ")
            return False
        z = (x, y)
        if z in BOARD_CORDS.keys():
            if z in self.board[self.player1] or z in self.board[self.player2]:
                print("That move is already made. Choose different move.")
                return False
            else:
                return True
        else:
            print("That is not a valid move. Please choose a valid move.")
            return False

    def is_full(self):
        if len(self.board[self.player1]) + len(self.board[self.player2]) >= 9:
            return True
        else:
            return False

    def is_game_over(self):
        if self.is_full() or self.calc_winner():
            return True
        else:
            return False


if __name__ == '__main__':
    name_1 = input("Player 1 (X) Please enter your name: ")
    name_2 = input("Player 2 (O) Please enter your name: ")

    player_1 = Player(name_1, 'X')
    player_2 = Player(name_2, 'O')
    game = Game(player_1, player_2)

    while True:
        while True:
            player_1_x = input(
                f"{player_1.name} enter the horizontal coordinate for your move: (0,1,2) ")
            player_1_y = input(
                f"{player_1.name} enter the vertical coordinate for your move: (0,1,2) ")
            if game.check_move(player_1_x, player_1_y):
                break

        game.move(player_1_x, player_1_y, player_1)

        print(game.__repr__())

        print(game.board[player_1], game.board[player_2])

        if game.is_game_over():
            if game.calc_winner() is not None:
                print(f"{game.calc_winner()} wins")
            else:
                print("Tie")
            break

        while True:
            player_2_x = input(
                f"{player_2.name} enter the horizontal coordinate for your move: (0,1,2) ")
            player_2_y = input(
                f"{player_2.name} enter the vertical coordinate for your move: (0,1,2) ")
            if game.check_move(player_2_x, player_2_y):
                break
        game.move(player_2_x, player_2_y, player_2)

        print(game.__repr__())

        print(game.board[player_1], game.board[player_2])

        if game.is_game_over():
            if game.calc_winner() is not None:
                print(f"{game.calc_winner()} wins")
            else:
                print("Tie")
            break
