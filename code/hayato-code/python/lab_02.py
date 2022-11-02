users_input_for_number= int(input("Please enter a number from 0- 999: "))
ones_digit= users_input_for_number%10
tens_digit= users_input_for_number//10
hundreds_digit= int(users_input_for_number//100)
single_digits = ["zero", "one", "two", "three",
                     "four", "five", "six", "seven",
                     "eight", "nine"]
  
two_digits = ["ten", "eleven", "twelve",
                  "thirteen", "fourteen", "fifteen",
                  "sixteen", "seventeen", "eighteen",
                  "nineteen"]
  
tens_multiple = ["", "ten", "twenty", "thirty", "forty",
                 "fifty", "sixty", "seventy", "eighty",
                 "ninety"]
hundreds_digits = ["zero", "one", "two", "three",
                     "four", "five", "six", "seven",
                     "eight", "nine"]  

if users_input_for_number > 99:
    tens= users_input_for_number%100
    tens_digit= tens//10
    print(tens_digit)
    if tens_digit == 1:
        print(f'{hundreds_digits[hundreds_digit]} hundred {two_digits[ones_digit]}') 
    elif tens_digit >= 2 and ones_digit == 0:
        print(f'{hundreds_digits[hundreds_digit]} hundred {tens_multiple[tens_digit]}')
    elif tens_digit == 0 and ones_digit != 0:
        print(f'{hundreds_digits[hundreds_digit]} hundred {single_digits[ones_digit]}')
    elif ones_digit == 0 and tens_digit == 0:
        print(f'{hundreds_digits[hundreds_digit]} hundred')
    else:
        print(f'{single_digits[hundreds_digit]} hundred {tens_multiple[tens_digit]} {single_digits[ones_digit]}')
elif tens_digit == 1:
    print(two_digits[ones_digit])  
else:
    print(tens_multiple[tens_digit], single_digits[ones_digit])


