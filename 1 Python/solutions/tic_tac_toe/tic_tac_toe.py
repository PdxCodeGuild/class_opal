class Game:
    def __init__(self) -> None:
        self.board = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]

    def __repr__(self) -> str:
        rows = ["|".join(row) for row in self.board]
        return '\n'.join(rows)

    def move(self, x, y, token) -> None:
        self.board[x][y] = token

    def is_full(self):
        return ' ' not in self.__repr__()

    def calc_winner(self):
        if 'X' in self.board[0]:
            return 'X'

        possible_wins = [
            [self.board[0][0], self.board[1][1], self.board[2][2]],
            [self.board[2][0], self.board[1][1], self.board[0][2]],
        ]
        # find rows and columns
        for i in range(3):
            col = []
            row = []
            for j in range(3):
                col.append(self.board[j][i])
                row.append(self.board[i][j])
            possible_wins.append(col)
            possible_wins.append(row)

        # check each possible win
        for row in possible_wins:
            if len(set(row)) == 1 and ' ' not in row:
                return row[0]

    def is_game_over(self):
        if self.is_full():
            return True
        if self.calc_winner():
            return True
        return False
