number = int(input("Enter a number from 1-999: "))

hundreds_digit = number // 100
tens_digit = number // 10 % 10
ones_digit = number % 10

roman_ones_digit = {
    0: '',
    1: 'I',
    2: 'II',
    3: 'III',
    4: 'IV',
    5: 'V',
    6: 'VI',
    7: 'VII',
    8: 'VIII',
    9: 'IX'
}

roman_teens = {
    0: 'X',
    1: 'XI',
    2: 'XII',
    3: 'XIII',
    4: 'XIV',
    5: 'XV',
    6: 'XVI',
    7: 'XVII',
    8: 'XVIII',
    9: 'XIX'
}

roman_tens_digit = {
    2: 'XX',
    3: 'XXX',
    4: 'XL',
    5: 'L',
    6: 'LX',
    7: 'LXX',
    8: 'LXXX',
    9: 'XC'
}

roman_hundreds_digit = {
    1: 'C',
    2: 'CC',
    3: 'CCC',
    4: 'CD',
    5: 'D',
    6: 'DC',
    7: 'DCC',
    8: 'DCCC',
    9: 'CM'
}

if number < 10:
    response = roman_ones_digit[ones_digit]
elif number < 20:
    response = roman_teens[ones_digit]
elif number < 100:
    if ones_digit != 0:
        response = roman_tens_digit[tens_digit] + roman_ones_digit[ones_digit]
    else:
        response = roman_tens_digit[tens_digit]
elif number < 1000:
    if tens_digit == 0:
        response = roman_hundreds_digit[hundreds_digit] + roman_ones_digit[ones_digit]        
    elif tens_digit == 1:
        response = roman_hundreds_digit[hundreds_digit] + roman_teens[ones_digit]
    else:
        if ones_digit != 0:
            response = roman_hundreds_digit[hundreds_digit] + roman_tens_digit[tens_digit] + roman_ones_digit[ones_digit]
        else:
            response = roman_hundreds_digit[hundreds_digit] + roman_tens_digit[tens_digit]
else:
    response = "Have a nice day!"

print(response)
