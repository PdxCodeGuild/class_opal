def find_start(data: str, interval: int):
    return [i for i in range(len(data))
            if i >= interval and len(set(data[i-interval:i])) == interval][0]


if __name__ == '__main__':
    with open('advent-of-code/danny/day6/input.txt') as f:
        data: str = f.read()
    print(find_start(data, 4))
    print(find_start(data, 14))
