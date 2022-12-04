def get_range(nums: list) -> list:
    # make a list with one number for each section
    if nums[1] == nums[0]:
        return [int(nums[0])]
    return list(range(int(nums[0]), int(nums[1])+1))


def includes_full_overlap(pair: list) -> bool:
    # split pair into lists
    pair1 = get_range(pair[0].split('-'))
    pair2 = get_range(pair[1].split('-'))
    # check if either pair has any items not included in the other
    flag1 = True
    for item in pair1:
        if item not in pair2:
            flag1 = False
    flag2 = True
    for item in pair2:
        if item not in pair1:
            flag2 = False
    return flag1 or flag2


def includes_partial_overlap(pair: list) -> bool:
    # split pair into lists
    pair1 = get_range(pair[0].split('-'))
    pair2 = get_range(pair[1].split('-'))
    # check if any item in a list is included in the other
    for item in pair1:
        if item in pair2:
            return True
    return False


def count_overlaps(data: str, finder) -> int:
    lines = data.split('\n')
    count = 0
    for line in lines:
        pair = line.split(',')
        if finder(pair):
            count += 1
    return count


if __name__ == '__main__':
    with open('advent-of-code/danny/day4/input.txt') as f:
        data: str = f.read()
    print(count_overlaps(data, includes_full_overlap))
    print(count_overlaps(data, includes_partial_overlap))
