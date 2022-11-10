# cc_number = input('Please enter the credit card number in question with no spaces or symbols\n'
cc_number = '4556737586899855' # test

def credit_card_validator(ccn: str):
    valid = False
    try:
        cc_num = int(ccn)
    except ValueError:
        return f'Invalid!'
    
    # Convert the input string into a list of ints
    cc_num = list(str(cc_num))
    cc_num = [int(i) for i in cc_num]
    if len(cc_num) != 16:
        return f'Invalid!'

    # Slice off the last digit. That is the check digit.
    check_digit = cc_num.pop()
    # Reverse the digits.
    cc_num.reverse()
    # Double every other element in the reversed list (starting with the first number in the list).
    # for x in range(0, len(cc_num), 2):
    #     cc_num[x]*2
    cc_num = [cc_num[x]*2 for x in range(0, len(cc_num), 2)]
    # Subtract nine from numbers over nine.
    # for n in cc_num:
    #     if n > 9:
    #         n - 9
    cc_num = [n - 9 for n in cc_num if n > 9]
    # Sum all values.
    cc_num = [sum(cc_num)]
    # Take the second digit of that sum.
    cc_num = [int(i) for i in str(cc_num[0])]
    cc_num = cc_num.pop()
    valid = cc_num == check_digit
    if valid:
        return 'Valid!'
    else:
        return 'Invalid!'


print(credit_card_validator(cc_number))