def find_calorie_counts_per_elf(calories: str):
    calorie_lists: list = calories.split('\n\n')
    for i in range(len(calorie_lists)):
        calorie_lists[i] = sum(
            [int(c) for c in calorie_lists[i].split('\n')])
    return calorie_lists


def find_max_calories(calories: str):
    calorie_totals = find_calorie_counts_per_elf(calories)
    return max(calorie_totals)


def find_top_3_total(calories: str):
    calorie_lists: list = find_calorie_counts_per_elf(calories)
    calorie_lists.sort()
    return sum(calorie_lists[-3:])


if __name__ == '__main__':
    with open('advent-of-code/danny/day1/input.txt') as f:
        calories: str = f.read()
    print(find_max_calories(calories))
    print(find_top_3_total(calories))
