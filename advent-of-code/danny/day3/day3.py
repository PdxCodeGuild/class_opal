from string import ascii_letters


def find_match(set1, set2):
    for item in set1:
        if item in set2:
            return item


def find_all_matches(data: str):
    matches = []
    for line in data.split('\n'):
        half = int(len(line)/2)
        match = find_match(line[half:], line[:half])
        matches.append(match)
    return matches


def split_groups(data: str):
    lines = data.split('\n')
    groups = []
    for i in range(0, len(lines), 3):
        group = lines[i:i+3]
        groups.append(group)
    return groups


def find_shared(group: list):
    return list(set(group[0]) & set(group[1]) & set(group[2]))


def find_all_badges(data: str):
    groups = split_groups(data)
    badges = []
    for group in groups:
        badges.append(find_shared(group)[0])
    return badges


def get_match_priority(letter):
    return ascii_letters.index(letter) + 1


def tally_priorities(data: list):
    priorities = [get_match_priority(l) for l in data]
    return sum(priorities)


if __name__ == '__main__':
    with open('advent-of-code/danny/day3/input.txt') as f:
        data: str = f.read()
    # part 1
    matches = find_all_matches(data)
    print(tally_priorities(matches))
    # part 2
    badges = find_all_badges(data)
    print(tally_priorities(badges))
