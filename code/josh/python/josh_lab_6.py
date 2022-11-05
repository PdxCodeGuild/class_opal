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
        else:
            credit_card_number[i] = credit_card_number[i] * 1
    for i in range(len(credit_card_number)):
        if credit_card_number[i] > 9:
            credit_card_number[i] = credit_card_number[i] - 9
    ###print statements for review while developing code###
    print(check_digit)
    # print(list_sum)
    print(credit_card_number)
    ###End of program, if previous code works###
    # list_sum = sum(credit_card_number)
    # for num in list_sum[1]:
    #     if num == check_digit:
    #         print("Credit card is valid!")
    #     else:
    #         print("Credit card is not valid!")


credit_card_validator()

###Point of progress in steps in program###
# Subtract nine from numbers over nine.
# Sum all values.
# Take the second digit of that sum.
# If that matches the check digit, the whole card number is valid.


# Here is a valid credit card number to test with: 4556737586899855
# For example, the worked out steps would be:

# 1 8 9 9 7 6 7 5 5 3 5 6 1 5 8
# 85
# 5
# True Valid!