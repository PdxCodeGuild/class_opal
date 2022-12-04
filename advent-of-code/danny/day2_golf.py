def rps_score_1(rps):
    score = 0
    for move in [round.split(' ') for round in rps.split('\n')]:
        move2 = {'X': 'A', 'Y': 'B', 'Z': 'C'}[move[1]]
        score += 3 if move[0] == move2 else 0  # draw
        if move2 == 'A':
            score += 6 + 1 if move[0] == 'C' else 1
        elif move2 == 'B':
            score += 6 + 2 if move[0] == 'A' else 2
        elif move2 == 'C':
            score += 6 + 3 if move[0] == 'B' else 3
    return score


def rps_score_2(rps):
    options = {
        'A': (1, 'C', 'B'),
        'B': (2, 'A', 'C'),
        'C': (3, 'B', 'A')
    }
    score = 0
    for a, b in [tuple(round.split(' ')) for round in rps.split('\n')]:
        score += options[options[a][1]][0] if b == 'X' else 0  # lose
        score += options[a][0] + 3 if b == 'Y' else 0  # draw
        score += options[options[a][2]][0] + 6 if b == 'Z' else 0  # win
    return score


if __name__ == '__main__':
    with open('advent-of-code/puzzles/day2/input2.txt') as f:
        rps: str = f.read()
    print(rps_score_1(rps))
    print(rps_score_2(rps))
