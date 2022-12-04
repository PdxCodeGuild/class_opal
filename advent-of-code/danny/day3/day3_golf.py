from string import ascii_letters


def find_all_matches(data: str):
    return map(lambda line: list(set(line[int(len(line)/2):]) &
                                 set(line[:int(len(line)/2)]))[0],
               data.split('\n'))


def find_all_badges(data: str):
    lines = data.split('\n')
    return map(lambda group: list(set(group[0]) &
                                  set(group[1]) &
                                  set(group[2]))[0],
               [lines[i:i+3] for i in range(0, len(lines), 3)])


def tally_priorities(data: list):
    return sum([ascii_letters.index(l) + 1 for l in data])


if __name__ == '__main__':
    with open('advent-of-code/danny/day3/input.txt') as f:
        data: str = f.read()
    # part 1
    print(tally_priorities(find_all_matches(data)))
    # part 2
    print(tally_priorities(find_all_badges(data)))
