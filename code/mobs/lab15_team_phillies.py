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
                return f'{self.player1} wins'
            elif set(win).issubset(self.board[self.player2]):
                return self.player2
            else:
                return None


    # def __repr__(self):
        # return  self.board
        # self.board = "|    |\n|    |\n|    |"

    
    def move(self, x, y, player):
        z = (x, y)
        self.board[player].append(z)

    def is_full(self,board):
        

if __name__ == '__main__':
    jokic = Player('jokic', 'X')
    curry = Player('curry', 'O')
    game = Game(jokic, curry)
    game.move(0,0,jokic)
    game.move(0,1,jokic)
    game.move(0,2, jokic)
    print(game.board[jokic])
    # print(game)
    print(game.calc_winner(game.board))