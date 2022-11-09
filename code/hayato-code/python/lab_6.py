credit_card = list(input(f"Please type in your Credit Number: ")) #converting input into a list

credit_card_input_as_int= [int(i) for i in credit_card] #converting the list into an integer rather than a string
print(credit_card_input_as_int)
check_digit = credit_card_input_as_int.pop() #deleting the last number of the card with the pop method
print(credit_card_input_as_int)
credit_card_input_as_int.reverse()#reversing the order after the pop method
print(credit_card_input_as_int)

for i in range(len(credit_card_input_as_int)): #running the range within the length of the list and multiplying by 2 if the numbers are over 9
    if i % 2 == 0:
        credit_card_input_as_int[i] = 2 * credit_card_input_as_int[i]
print(credit_card_input_as_int)

for i in range(len(credit_card_input_as_int)): #running the range within the length of the list by subtracting the numbers if it over 9
    if credit_card_input_as_int[i] > 9:
        credit_card_input_as_int[i] = credit_card_input_as_int[i] - 9
print(credit_card_input_as_int)

sum_digits = str(sum(credit_card_input_as_int)) #getting the total sum of the calculated formula from above
print(sum_digits)

if sum_digits[1] == str(check_digit): #checking to see if the calculated sum and the original popped out # matches. 
    print(f"True Valid")
else:
    print(f'False')