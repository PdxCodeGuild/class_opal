MOVES = {
    # 0 is x axis, 1 is y axis
    "R": [0, 1],
    "L": [0, -1],
    "U": [1, 1],
    "D": [1, -1],
}


def track_two_positions(data: str):
    head: list = [0, 0]
    tail: list = [0, 0]
    all_tails: list = [tail]
    for line in data.split('\n'):
        direction: str = line[0]
        length: int = int(line[2:])
        for _ in range(int(length)):
            move: list = MOVES[direction]
            axis: int = move[0]

            # move head
            head[axis] += (move[1])

            # move tail
            up: int = abs(head[0] - tail[0])
            side: int = abs(head[1] - tail[1])
            if up > 1 or side > 1:
                tail = head.copy()
                tail[axis] -= move[1]
                all_tails.append(tail)
    return len(set([str(l) for l in all_tails]))


def track_ten_positions(data: str):
    # THIS ONE DOESN'T WORK YET!!
    head: list = [0, 0]
    tail: list = [0, 0]
    next_knot: list = [0, 0]
    all_tails: list = [tail]
    for line in data.split('\n'):
        direction: str = line[0]
        length: int = int(line[2:])

        for _ in range(int(length)):  # once per move
            move: list = MOVES[direction]
            axis: int = move[0]

            # move head
            new_head = head.copy()
            new_head[axis] += (move[1])
            head = new_head

            # move children
            last_knot = head
            for _ in range(9):  # once per knot
                # move tail
                up: int = abs(last_knot[0] - next_knot[0])
                side: int = abs(last_knot[1] - next_knot[1])
                if up > 1 or side > 1:
                    next_knot = last_knot.copy()
                    next_knot[axis] -= move[1]
            all_tails.append(next_knot)
    return len(set([str(l) for l in all_tails]))


if __name__ == '__main__':
    with open('advent-of-code/danny/day9/input.txt') as f:
        data: str = f.read()
    # print(track_positions('R 1\nU 2'))
    print(track_two_positions(data))
    # print(track_ten_positions(data))
