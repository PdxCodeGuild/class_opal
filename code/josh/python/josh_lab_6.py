# Lab 6: Credit Card Validation

# Let's write a function credit_card_validator which returns whether a string containing a credit card number is valid as a boolean. The steps are as follows:


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
    # for num in credit_card_number:
    #     if num > 9:
    #         num = num - 9
    #     else:
    #         num = num


    credit_card_number = [i - 9 for i in credit_card_number if i > 9]
    #list_sum = sum(credit_card_number)
    print(check_digit)
    #print(list_sum)
    print(credit_card_number)


credit_card_validator()


# Subtract nine from numbers over nine.
# Sum all values.
# Take the second digit of that sum.
# If that matches the check digit, the whole card number is valid.


# Here is a valid credit card number to test with: 4556737586899855
# For example, the worked out steps would be:

# 4 5 5 6 7 3 7 5 8 6 8 9 9 8 5 5
# 4 5 5 6 7 3 7 5 8 6 8 9 9 8 5
# 5 8 9 9 8 6 8 5 7 3 7 6 5 5 4
# 10 8 18 9 16 6 16 5 14 3 14 6 10 5 8
# 1 8 9 9 7 6 7 5 5 3 5 6 1 5 8
# 85
# 5
# True Valid!
# Git Add, Commit & Push:
# > git add files-to-be-added
# > git commit -m "your commit message goes here"
# > git push -u origin your_name-python-lab6
# Then go to the repository to create a PR.