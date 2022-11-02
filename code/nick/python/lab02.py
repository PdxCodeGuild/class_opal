def main():
    '''take a number or time from user, and convert it into English phrase and Roman numerals'''
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
        1000: ['one thousand'],
    }

    int_to_roman_dict = {
        1: 'I',
        4: 'IV',
        5: 'V',
        9: 'IX',
        10: 'X',
        40: 'XL',
        50: 'L',
        90: 'XC',
        100: 'C',
        400: 'CD',
        500: 'D',
        900: 'CM',
        1000: 'M',
    }

    def int_to_words(num=24):
        '''converts numbers to written phrase form'''
        if num in int_to_words_dict:
            return int_to_words_dict[num][0]
        else:
            hundred = num//100
        
        if hundred == 0:
            ten = num//10
            one = num%10
            ten_word = int_to_words_dict[ten][1]
            one_word = int_to_words_dict[one][0]
            return f'{ten_word}-{one_word}'

        else:
            hundred_word = int_to_words_dict[hundred][2]
            num = num%100
            return f'{hundred_word} {int_to_words(num)}'

    def int_to_roman(num=24):
        '''Convert given integer to Roman numerals
        paraphrased from https://pencilprogrammer.com/python-programs/convert-integer-to-roman-numerals/#:~:text=So%2C%20to%20convert%20an%20integer%20into%20its%20corresponding,to%20the%20remainder%20of%20the%20division.%20More%20items
        '''
        resolution_order = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
        roman_complete = []

        for x in resolution_order:
            if num != 0:
                quotient = num//x

                if quotient != 0:
                    for y in range(quotient):
                        roman_complete.append(int_to_roman_dict[x])

                num = num%x

        return ''.join(roman_complete)


    def time_converter(time = '12:49'):
        '''convert a given time to written form and roman numeral'''
        time_split = time.split(':')
        # print(time_split)   #test
        hour_int = int(time_split[0])
        minute_int = int(time_split[1])
        # print(hour_int, minute_int)   #test
        hour_phrase = int_to_words(hour_int)
        hour_roman = int_to_roman(hour_int)
        minute_phrase = int_to_words(minute_int)
        minute_roman = int_to_roman(minute_int)
        return f'''{hour_phrase} {minute_phrase}
    {hour_roman} {minute_roman}'''

    def number_converter(req = '137'):
        '''Converts number to both English phrase and Roman numeral'''
        num = int(req)
        phrase = int_to_words(num)
        roman = int_to_roman(num)
        return f'''
    {phrase}
    {roman}'''
    # print(time_converter())   #test

    print(
    '''Welcome to the Number converter! 
    We take a number between 0 and 1000 or a time and convert it to English phrase and Roman numerals.\n'''
    )

    request = input("What number do you want to convert? If it is a time, please denote it with an appropriately placed ':' \n")

    if int(request) == False:
        print('zero')

    elif ':' in request:
        print(time_converter(request))

    else:
        print(number_converter(request))

main()