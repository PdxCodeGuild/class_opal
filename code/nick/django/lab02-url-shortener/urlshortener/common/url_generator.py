import random
import string


def url_generator():
    characters = [
        list(string.ascii_uppercase),
        list(string.ascii_lowercase),
        list(string.digits),
    ]

    # put all characters into one list
    url_characters = []

    for _ in range(4):
        url_characters.append(random.choice(characters[0]))
        url_characters.append(random.choice(characters[1]))
        url_characters.append(random.choice(characters[2]))

    # randomize
    random.shuffle(url_characters)

    # join into string
    url = ''.join(url_characters)
    return url
