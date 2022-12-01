def find_calorie_counts_per_elf(calories: str):
    return [sum([int(c) for c in c_list.split('\n')])
            for c_list in calories.split('\n\n')]


def find_max_calories(calories: str):
    return max(find_calorie_counts_per_elf(calories))


def find_top_3_total(calories: str):
    return sum(sorted(find_calorie_counts_per_elf(calories))[-3:])


if __name__ == '__main__':
    with open('advent-of-code/puzzles/day1/input1.txt') as f:
        calories: str = f.read()
    print(find_max_calories(calories))
    print(find_top_3_total(calories))
