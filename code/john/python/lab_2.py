# word problem 

'''
fritz is a baker. He makes donuts and sells them by the dozen. 
For a given number of donuts that he has, how many will he have leftover. 



# '''


# total_donuts = 1500
# dozen_size = 12

# number_of_dozens = total_donuts // dozen_size
# leftover_donuts = total_donuts % dozen_size

# print(number_of_dozens)


# output = f'''Fritz can sell {number_of_dozens} dozen donuts
# and will have {leftover_donuts}

# '''

# print(output)

# Create a dict of numbers with their word value
'''
Convert a given number into its english representation. For example: 67 becomes 'sixty-seven'. Handle numbers from 0-99.

Hint: you can use modulus to extract the ones and tens digit.

x = 67
tens_digit = x//10
ones_digit = x%10
Hint 2: use the digit as an index for a list of strings OR as a key for a dict of digit:phrase pairs.

Version 2
Handle numbers from 100-999.
'''

ones_digits = {
0: 'zero',
1:'one', 
2: 'two', 
3: 'three', 
4: 'four',
5: 'five',
6: 'six',
7: 'seven',
8: 'eight',
9: 'nine',
  }

teens_digit = {
10: 'ten',
11:'eleven', 
12: 'twelve', 
13: 'thirteen', 
14: 'fourteen',
15: 'fifteen',
16: 'sixteen',
17: 'seventeen',
18: 'eighteen',
19: 'nineteen',
  }

tens_digit = {
2: 'twenty', 
3: 'thirty', 
4: 'fourty',
5: 'fifty',
6: 'sixty',
7: 'seventy',
8: 'eighty',
9: 'ninety',
  }

hundreds_digit = {
100: 'one-hundred',
200: 'two-hundred',
300: 'three-hundred',
400: 'four-hundred',
500: 'five-hundred',
600: 'six-hundred',
700: 'seven-hundred',
800: 'eight-hundred',
900: 'nine-hundred',
}

user_input = int(input('Enter a number: '))

# convert what the user input to text by referencing the numbers_dict

if len(str(user_input)) == 1: 
    word_conversion = ones_digits[user_input]
    print(word_conversion)
elif len(str(user_input)) == 2:
    if  user_input // 10 == 1:  
        print(teens_digit[user_input])
    else:
        tens = user_input // 10 
        ones = user_input % 10
        print(f'{tens_digit[tens]}-{ones_digits[ones]}')
elif len(str(user_input)) == 3: 
    hundreds = user_input // 100 * 100
    if user_input // 10 % 10 != 1 and user_input // 10 % 10 != 0: 
        tens = user_input // 10 % 10 
        ones = user_input % 10 
        if ones == 0:
            print(f'{hundreds_digit[hundreds]}-{tens_digit[tens]}')
            # print((f'{hundreds_digit[hundreds]}{tens_digit[tens]}-{ones_digits[ones]}'))
       



# get a number from the user 