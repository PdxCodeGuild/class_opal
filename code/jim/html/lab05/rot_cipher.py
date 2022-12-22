from string import ascii_lowercase

letters = list(ascii_lowercase)


def get_encoding(user_string: str, rotation: int) -> str:
    user_string = user_string.lower()
    rotation = int(rotation)
    letters_rot = []
    for i in range(len(letters)):
        letters_rot.append(letters[(i + rotation) % 26])

    encoded_list = []
    for i in range(len(user_string)):
        encoded_list.append(letters_rot[letters.index(user_string[i])])

    encoded_string = ''.join(encoded_list)

    return encoded_string


if __name__ == '__main__':
    user_string = input("Enter a string: ")
    rotation = int(input("Enter a rotation amount: "))

    answer = get_encoding(user_string, rotation)
    print(answer)
