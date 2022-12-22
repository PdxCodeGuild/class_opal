def find_packet_start(data: str):
    """
    >>> find_packet_start('mjqjpqmgbljsphdztnvjfqwrcgsmlb')
    7
    >>> find_packet_start('bvwbjplbgvbhsrlpgdmjqwftvncz')
    5
    >>> find_packet_start('nppdvjthqldpwncqszvftbrmjlhg')
    6
    >>> find_packet_start('nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg')
    10
    >>> find_packet_start('zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw')
    11
    """
    for i in range(len(data)):
        if i >= 4:
            if len(set(data[i-4:i])) == 4:
                return i


def find_message_start(data: str):
    """
    >>> find_message_start('mjqjpqmgbljsphdztnvjfqwrcgsmlb')
    19
    >>> find_message_start('bvwbjplbgvbhsrlpgdmjqwftvncz')
    23
    >>> find_message_start('nppdvjthqldpwncqszvftbrmjlhg')
    23
    >>> find_message_start('nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg')
    29
    >>> find_message_start('zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw')
    26
    """
    for i in range(len(data)):
        if i >= 14:
            if len(set(data[i-14:i])) == 14:
                return i


if __name__ == '__main__':
    with open('advent-of-code/danny/day6/input.txt') as f:
        data: str = f.read()
    print(find_packet_start(data))
    print(find_message_start(data))
