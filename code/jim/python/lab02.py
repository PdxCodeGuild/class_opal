number = int(input("Enter a number from 0-99: "))

tens_digit = number // 10
ones_digit = number % 10

english_ones_digit = {
    0: 'zero',
    1: 'one',
    2: 'two',
    3: 'three',
    4: 'four',
    5: 'five',
    6: 'six',
    7: 'seven',
    8: 'eight',
    9: 'nine'
}

english_teens = {
    0: 'ten',
    1: 'eleven',
    2: 'twelve',
    3: 'thirteen',
    4: 'fourteen',
    5: 'fifteen',
    6: 'sixteen',
    7: 'seventeen',
    8: 'eightteen',
    9: 'nineteen'
}

english_tens_digit = {
    2: 'twenty',
    3: 'thirty',
    4: 'forty',
    5: 'fifty',
    6: 'sixty',
    7: 'seventy',
    8: 'eighty',
    9: 'ninty'
}

if number < 10:
    response = english_ones_digit[ones_digit]
elif number < 20:
    response = english_teens[ones_digit]
elif number < 100:
    if ones_digit != 0:
        response = english_tens_digit[tens_digit] + "-" + english_ones_digit[ones_digit]
    else:
        response = english_tens_digit[tens_digit]
else:
    response = "Have a nice day!"

print(response)