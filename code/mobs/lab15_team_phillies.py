class Player:
    def __init__(self, name, token):
        self.name = name
        self.token = token

class Game:
    def __init__(self, player1, player2):
        self.player1 = player1
        self.player2 = player2
        self.board = {player1:[], player2:[]}
        
    
    def calc_winner(self, board):
        winning_list = [
        [(0,0), (0,1), (0,2)],
        [(1,0), (1,1), (1,2)],
        [(2,0), (2,1), (2,2)],
        [(0,0), (1,0), (2,0)],
        [(0,1), (1,1), (2,1)],
        [(0,2), (1,2), (2,2)],
        [(0,0), (1,1), (2,2)],
        [(2,0), (1,1), (0,2)]
        ]
        for win in winning_list:
            if set(win).issubset(self.board[self.player1]):
                return self.player1
            elif set(win).issubset(self.board[self.player2]):
                return self.player2


    def __repr__(self):
        board_coords = {(0, 0): 0, (0,1): 2, (0,2): 4, (1,0): 6, (1,1): 8, (1,2): 10, (2,0): 12, (2,1): 14, (2,2): 16}
        board_rep = " | | \n | | \n | | "
        # board_rep_list = [" ", "|"]
        # board_rep.format()
        for coord in board_coords.keys():
            if coord in self.board[self.player1]:
                board_rep = board_rep[0:board_coords[coord]] + "X" + board_rep[board_coords[coord]+ 1:]
            elif coord in self.board[self.player2]:
                board_rep = board_rep[0:board_coords[coord]] + "0" + board_rep[board_coords[coord]+ 1:]
        return board_rep

    
    def move(self, x, y, player):
        # TODO handle the case where the player selects an invalid move (or a move that is already made) 
        z = (x, y)
        self.board[player].append(z)


    def is_full(self,board):
        # board_coords = [(0, 0), (0,1), (0,2), (1,0), (1,1), (1,2), (2,0), (2,1), (2,2)]
        # players_board = self.board[self.player1].extend(self.board[self.player2])
        # if players_board == board_coords:
        if len(self.board[self.player1]) + len(self.board[self.player2]) >= 9:
            return True
        else:
            return False
    

    def is_game_over(self, board):
        if self.is_full(self.board) or self.calc_winner(self.board):
            return True
        else:
            return False


if __name__ == '__main__':
    jokic = Player('jokic', 'X')
    curry = Player('curry', 'O')
    game = Game(jokic, curry)
    
    while True:
        player_1_x = int(input(f"{jokic.name} enter the coordinates the horizontal coordinate for your move: (0,1,2) "))
        player_1_y = int(input(f"{jokic.name} enter the coordinates the horizontal coordinate for your move: (0,1,2) "))
        
        game.move(player_1_x,player_1_y,jokic)
        
        print(game.__repr__())

        print(game.board[jokic], game.board[curry])

        if game.is_game_over(game.board):
            print(f"{game.calc_winner(game.board).name} wins")
            break
        
        player_2_x = int(input(f"{curry.name} enter the coordinates the horizontal coordinate for your move: (0,1,2) "))
        player_2_y = int(input(f"{curry.name} enter the coordinates the horizontal coordinate for your move: (0,1,2) "))

        game.move(player_2_x,player_2_y,curry)
        
        print(game.__repr__())

        print(game.board[jokic], game.board[curry])

        if game.is_game_over(game.board):
            print(f"{game.calc_winner(game.board).name} wins")
            break

    
    
    
    
    # game.move(0,0,jokic)
    # game.move(0,1,jokic)
    # game.move(0,2, jokic)
    # print(game.board[jokic])
    # # print(game)
    # print(game.calc_winner(game.board))

    # game.move(1,0,jokic)
    # game.move(1,1,jokic)
    # game.move(1,2, jokic)
    # game.move(2,0,jokic)
    # game.move(2,1,jokic)
    # #game.move(2,2, jokic)
    # print(game.is_full(game.board))

    # print(game.is_game_over(game.board))

    # print(game.__repr__())