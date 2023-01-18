import random
import string

letters = string.ascii_letters
digits = string.digits


def get_code():
    first_part = [random.choice(letters) for x in range(3)]
    second_part = [random.choice(digits)]
    third_part = [random.choice(letters) for x in range(2)]
    my_list = first_part + second_part + third_part
    code = "".join(my_list)
    return code
