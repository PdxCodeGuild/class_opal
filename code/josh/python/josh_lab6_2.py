# Lab 6_2: Credit Card Validation - REDUX

# Creates a function that returns whether a credit card is valid
def credit_card_validator():
    user_input = list(input("Please enter credit card number with no spaces: "))
    credit_card_number = list(map(lambda x: int(x), user_input))
    check_digit = credit_card_number[-1]
    credit_card_number.pop(-1)
    credit_card_number.reverse()
    credit_card_double = map(lambda x: x[1] * 2 if x[0] % 2 == 0 else x[1], enumerate(credit_card_number))
    ccd_minus_9 = map(lambda x: x - 9 if x > 9 else x, credit_card_double)
    list_sum = sum(ccd_minus_9)
    comparison_digit = (check_digit * -1) - list_sum
    if (comparison_digit * -1) - list_sum == check_digit:
        print("Credit card is valid!")
    else:
        print("Credit card is not valid!")


credit_card_validator()