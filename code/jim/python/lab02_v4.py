my_time = input("Enter a time in HH:MM format: ")

hours = int(my_time[0:2])
minutes = int(my_time[3:5])

minutes_tens_digit = minutes // 10
minutes_ones_digit = minutes % 10

english_hours = {
    0: 'twelve',
    1: 'one',
    2: 'two',
    3: 'three',
    4: 'four',
    5: 'five',
    6: 'six',
    7: 'seven',
    8: 'eight',
    9: 'nine',
    10: 'ten',
    11: 'eleven',
    12: 'twelve',
    13: 'one',
    14: 'two',
    15: 'three',
    16: 'four',
    17: 'five',
    18: 'six',
    19: 'seven',
    20: 'eight',
    21: 'nine',
    22: 'ten',
    23: 'eleven'
}

english_ones_digit = {
    0: '',
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

if minutes == 0:
    response = english_hours[hours]
elif minutes < 10:
    response = english_hours[hours] + " O'" + english_ones_digit[minutes_ones_digit]
elif minutes < 20:
    response = english_hours[hours] + " " + english_teens[minutes_ones_digit]
elif minutes < 60:
    if minutes_ones_digit == 0:
        response = english_hours[hours] + " " + english_tens_digit[minutes_tens_digit]
    else:
        response = english_hours[hours] + " " + english_tens_digit[minutes_tens_digit] + "-" + english_ones_digit[minutes_ones_digit]
else:
    response = "Have a nice day!"

if hours < 12:
    response = response.capitalize() + " am"
elif hours < 24:
    response = response.capitalize() + " pm"
else:
    response = "Have a great day!"

print(response)
