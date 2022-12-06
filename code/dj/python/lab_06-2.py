from functools import reduce


def add_list(list1, list2):
    list_sum = sum(list1) + sum(list2[1::2])
    return list_sum


def credit_card_validator(card_nums: str):
    card_list = list(card_nums)

    # for num in card_nums:
    #     card_list.append(int(num))
    list_append = list(map(lambda num: int(num), card_list))
    print(list_append)
    last_digit = list_append.pop(-1)
    list_append.reverse()
    double_list = []
    for digit in list_append[0:: 2]:
        double_digit = digit * 2
        if double_digit > 9:
            double_digit -= 9
        double_list.append(double_digit)
    # list_sum = sum(double_list) + sum(card_list[1::2])
    list_addition = reduce(lambda num1, num2: num1 + num2, double_list) + \
        reduce(lambda num1, num2: num1 + num2, list_append[1::2])
    # list_sum = str(list_sum)
    list_addition = str(list_addition)
    if last_digit == int(list_addition[-1]):
        return True
    else:
        return False


if credit_card_validator("4556737586899855"):
    print("Valid")
else:
    print("Invalid")
