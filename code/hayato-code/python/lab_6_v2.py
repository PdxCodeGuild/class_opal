from functools import reduce
card_numberz = []
card_number = '4556737586899855'

def credit(card_number):
    return int(card_number)

user_credit_card= map(credit, card_number)
credit_card_input= list(user_credit_card)

for nums in credit_card_input:
    card_numberz.append(nums)

print(card_numberz)

check_digit = card_numberz.pop() #deleting the last number of the card with the pop method
print(card_numberz)
card_numberz.reverse()#reversing the order after the pop method
print(card_numberz)

for i in range(len(card_numberz)): #running the range within the length of the list and multiplying by 2 if the numbers are over 9
    if i % 2 == 0:
        card_numberz[i] = 2 * card_numberz[i]
print(card_numberz)

def card_numberz_minus_nine(card_numberz):
    if card_numberz > 9:
        card_numberz = card_numberz - 9
    return card_numberz

minus_nine_number= map(card_numberz_minus_nine, card_numberz)
minus_nine_list= list(minus_nine_number)

print(minus_nine_list)
sum_digits = str(sum(minus_nine_list))
print(sum_digits)

sum_digits = str(sum(minus_nine_list))[1]#getting the total sum of the calculated formula from above
sum_digitzzz= sum_digits + str(check_digit)

def card_checker(card_numberz, check_digit):
    if str(card_numberz) == str(check_digit): #checking to see if the calculated sum and the original popped out # matches. 
        print(f"True Valid")
    else:
        print(f'False')

final_card_checker= reduce(card_checker, sum_digitzzz)
