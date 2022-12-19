def track_signal(data: str):
    lines = data.split('\n')

    iteration = 1
    tracker = {}
    x = 1
    for i in range(len(lines)):
        if lines[i] == 'noop':
            iteration += 1
        else:
            instructions = lines[i].split()
            x += int(instructions[1])
            iteration += 2
            tracker[iteration] = x
    # print(tracker)

    result = 0
    for i in [20, 60, 100, 140, 180, 220]:
        x_val = tracker.get(i)
        next = 1
        while x_val == None:
            x_val = tracker.get(i - next)
            next += 1
        result += x_val * i
    return result


if __name__ == '__main__':
    with open('advent-of-code/danny/day10/input.txt') as f:
        data: str = f.read()

    print(track_signal(data))
