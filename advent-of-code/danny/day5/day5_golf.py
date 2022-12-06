from string import digits, ascii_uppercase


def read_stacks(lines: list) -> int:
    count = [int(line[-2]) for line in lines
             if len(line) and line[1] in digits][0]
    stacks = dict.fromkeys(range(1, count+1), '')

    for line in lines[:count]:
        for i in range(count):
            for char in line[i*4:(i*4)+4]:
                if char in ascii_uppercase:
                    stacks[i+1] += char

    for key in stacks:
        stacks[key] = stacks[key][::-1]
    return stacks


def crate_mover_9000(words: list, stacks: dict):
    num_to_move = int(words[1])
    from_stack = int(words[3])
    to_stack = int(words[5])
    for _ in range(num_to_move):
        moved = stacks[from_stack][-1]
        stacks[from_stack] = stacks[from_stack][:-1]
        stacks[to_stack] += moved
    return stacks


def crate_mover_9001(words: list, stacks: dict):
    num_to_move = int(words[1])
    from_stack = int(words[3])
    to_stack = int(words[5])
    moved = stacks[from_stack][len(stacks[from_stack])-num_to_move:]
    stacks[from_stack] = stacks[from_stack][:len(
        stacks[from_stack])-num_to_move]
    stacks[to_stack] += moved
    return stacks


def get_answer(data: str, crate_mover) -> str:
    lines = data.split('\n')
    stacks = read_stacks(lines)
    for line in lines:
        if len(line) and line[0] == 'm':
            stacks = crate_mover(line.split(), stacks)

    return ''.join([stacks[key][-1] for key in stacks])


if __name__ == '__main__':
    with open('advent-of-code/danny/day5/input.txt') as f:
        data: str = f.read()
    print(get_answer(data, crate_mover_9000))
    print(get_answer(data, crate_mover_9001))
