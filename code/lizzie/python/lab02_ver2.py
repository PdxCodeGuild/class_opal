number = input("Please enter a number between 0 and 999: ")
number = int(number)

ones_digit = number%10
tens_digit = (number%100)//10 ##Uses modulus to remove remaining hundreds place
hundreds_digit = number//100
teens_digit = str(tens_digit)+str(ones_digit)

ones_list = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 
'ten', 'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen',
'nineteen']

tens_list = [' ', 'ten', 'twenty', 'thirty', 'fourty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety']

hundreds_list = [' ', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']

if number < 20:
    print(ones_list[number])

elif number > 99:
    if tens_digit == 1: ##Indicates the number ends with 'teen', like 'fourteen,' so we use the concantenated teens_digit
        print(f'{hundreds_list[hundreds_digit]}-hundred-{ones_list[int(teens_digit)]}')
    
    elif ones_digit == 0: ##Prevents the result from including unneccessary zeroes from ones place
        print(f'{hundreds_list[hundreds_digit]} hundred {tens_list[tens_digit]}')
    
    else:
        print(f'{hundreds_list[hundreds_digit]}-hundred-{tens_list[tens_digit]}-{ones_list[ones_digit]}')

elif ones_digit == 0: ##To catch any numbers like 60, 70, etc. to prevent extra zeroes at the end.
        print(f'{tens_list[tens_digit]}')

else: print(f'{tens_list[tens_digit]}-{ones_list[ones_digit]}') ##Catches all 21-99 numbers not already dealt with