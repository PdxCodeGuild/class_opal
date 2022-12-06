def rps_score_1(rps):
    moves = {
        'A': 'rock',
        'B': 'paper',
        'C': 'scissors',
        'X': 'rock',
        'Y': 'paper',
        'Z': 'scissors',
    }

    score = 0
    draws = 0
    for round in rps.split('\n'):
        move = round.split(' ')
        a = moves[move[0]]
        b = moves[move[1]]

        if a == b:
            draws += 1
        if b == 'rock':
            score += 1
            if a == 'scissors':
                score += 6
        elif b == 'paper':
            score += 2
            if a == 'rock':
                score += 6
        elif b == 'scissors':
            score += 3
            if a == 'paper':
                score += 6

    score = score + (draws * 3)
    return score


def rps_score_2(rps):
    moves = {
        'A': 'rock',
        'B': 'paper',
        'C': 'scissors',
    }

    options = {
        'rock': (1, 'scissors', 'paper'),
        'paper': (2, 'rock', 'scissors'),
        'scissors': (3, 'paper', 'rock')
    }

    score = 0
    for round in rps.split('\n'):
        move = round.split(' ')
        a = moves[move[0]]
        b = move[1]

        if b == 'X':  # lose
            play = options[a][1]
        elif b == 'Y':  # draw
            play = a
            score += 3
        elif b == 'Z':  # win
            play = options[a][2]
            score += 6

        score += options[play][0]
    return score


if __name__ == '__main__':
    with open('advent-of-code/danny/day2/input.txt') as f:
        rps: str = f.read()
    print(rps_score_1(rps))
    print(rps_score_2(rps))
