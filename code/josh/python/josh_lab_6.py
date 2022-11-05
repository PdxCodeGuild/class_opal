# Lab 6: Credit Card Validation


def credit_card_validator():
    user_input = list(input("Please enter credit card number with no spaces: "))
    credit_card_number = [int(i) for i in user_input]
    check_digit = credit_card_number[-1]
    credit_card_number.pop(-1)
    credit_card_number.reverse()
    for i in range(len(credit_card_number)):
        if i % 2 == 0:
            credit_card_number[i] = credit_card_number[i] * 2
    for i in range(len(credit_card_number)):
        if credit_card_number[i] > 9:
            credit_card_number[i] = credit_card_number[i] - 9
    list_sum = sum(credit_card_number)
    comparison_digit = (check_digit * -1) - list_sum
    if (comparison_digit * -1) - list_sum == check_digit:
        print("Credit card is valid!")
    else:
        print("Credit card is not valid!")


credit_card_validator()