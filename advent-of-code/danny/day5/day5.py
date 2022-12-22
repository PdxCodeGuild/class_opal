from string import digits, ascii_uppercase

TEST_DATA = """    [D]    
[N] [C]    
[Z] [M] [P]
 1   2   3 

move 1 from 2 to 1
move 3 from 1 to 3
move 2 from 2 to 1
move 1 from 1 to 2"""


def get_stack_count(lines: list) -> int:
    for line in lines:
        if line[1] in digits:
            return int(line[-2])


def read_stacks(lines: list) -> int:
    count = get_stack_count(lines)
    stacks = dict.fromkeys(range(1, count+1), '')

    for line in lines[:count]:
        for i in range(count):
            chunk = line[i*4:(i*4)+4]
            for char in chunk:
                if char in ascii_uppercase:
                    stacks[i+1] += char

    for key in stacks:
        stacks[key] = stacks[key][::-1]
    return stacks


def crate_mover_9000(data: str):
    lines = data.split('\n')
    stacks = read_stacks(lines)

    for line in lines:
        if len(line) > 0 and line[0] == 'm':
            words = line.split()
            num_to_move = int(words[1])
            from_stack = int(words[3])
            to_stack = int(words[5])
            for _ in range(num_to_move):
                moved = stacks[from_stack][-1]
                stacks[from_stack] = stacks[from_stack][:-1]
                stacks[to_stack] += moved
    return stacks


def crate_mover_9001(data: str):
    lines = data.split('\n')
    stacks = read_stacks(lines)

    for line in lines:
        if len(line) > 0 and line[0] == 'm':
            words = line.split()
            num_to_move = int(words[1])
            from_stack = int(words[3])
            to_stack = int(words[5])
            moved = stacks[from_stack][len(stacks[from_stack])-num_to_move:]
            stacks[from_stack] = stacks[from_stack][:len(
                stacks[from_stack])-num_to_move]
            stacks[to_stack] += moved
    return stacks


def give_answer(stacks: dict) -> str:
    output = ''
    for key in stacks:
        output += stacks[key][-1]
    return output


if __name__ == '__main__':
    with open('advent-of-code/danny/day5/input.txt') as f:
        data: str = f.read()
    print(give_answer(crate_mover_9000(data)))
    print(give_answer(crate_mover_9001(data)))
