def get_pairs(pair: list) -> tuple:
    return [int(n) for n in pair[0].split('-')], [int(n) for n in pair[1].split('-')]


def includes_full_overlap(pairs: tuple) -> bool:
    return (min(pairs[0]) >= min(pairs[1]) and max(pairs[0]) <= max(pairs[1])) \
        or (min(pairs[0]) <= min(pairs[1]) and max(pairs[0]) >= max(pairs[1]))


def includes_partial_overlap(pairs: tuple) -> bool:
    return min(pairs[0]) <= max(pairs[1]) and min(pairs[1]) <= max(pairs[0])


def count_overlaps(data: str, finder) -> int:
    return len([True for line in data.split('\n')
                if finder(get_pairs(line.split(',')))])


if __name__ == '__main__':
    with open('advent-of-code/danny/day4/input.txt') as f:
        data: str = f.read()
    print(count_overlaps(data, includes_full_overlap))
    print(count_overlaps(data, includes_partial_overlap))
