import random
import string


def code_generator():
    characters = [
        list(string.ascii_uppercase),
        list(string.ascii_lowercase),
        list(string.digits),
    ]

    # put all characters into one list
    code_characters = []

    for _ in range(2):
        code_characters.append(random.choice(characters[0]))
        code_characters.append(random.choice(characters[1]))
        code_characters.append(random.choice(characters[2]))

    # randomize
    random.shuffle(code_characters)

    # join into string
    code = ''.join(code_characters)
    return code
