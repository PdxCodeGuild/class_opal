int_to_words_dict = {
    0: [''],
    1: ['one', '', 'one-hundred'],
    2: ['two', 'twenty', 'two-hundred'],
    3: ['three', 'thirty', 'three-hundred'],
    4: ['four', 'forty', 'four-hundred'],
    5: ['five', 'fifty', 'five-hundred'],
    6: ['six', 'sixty', 'six-hundred'],
    7: ['seven', 'seventy', 'seven-hundred'],
    8: ['eight', 'eighty', 'eight-hundred'],
    9: ['nine', 'ninety', 'nine-hundred'],
    10: ['ten'],
    11: ['eleven'],
    12: ['twelve'],
    13: ['thirteen'],
    14: ['fourteen'],
    15: ['fifteen'],
    16: ['sixteen'],
    17: ['seventeen'],
    18: ['eighteen'],
    19: ['nineteen'],
}


def int_to_words(num=24):
    if num in int_to_words_dict:
        return int_to_words_dict[num][0]
    else:
        hundred = num//100
    
    if hundred == 0:
        ten = num//10
        one = num%10
        ten_word = int_to_words_dict[ten][1]
        one_word = int_to_words_dict[one][0]
        return f'{ten_word} {one_word}'

    if hundred > 0:
        hundred_word = int_to_words_dict[hundred][2]
        num = num%100
        return f'{hundred_word} {int_to_words(num)}'

    

print('Welcome to the Integer to Phrase numerical converter!')
number = int(input("What number do you want to convert?\n"))

print(int_to_words(number))
