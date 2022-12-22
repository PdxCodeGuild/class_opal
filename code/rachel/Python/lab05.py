credit_card = input("Enter the credit card number: ")
credit_card = list(credit_card)
print(len(credit_card))
credit_card2 = credit_card.copy()#copying list to print check digit at end for comparison to sum_total
credit_card.pop(15)
print(credit_card)
credit_card.reverse()
print(credit_card)
cc_numbers = [int(x) for x in credit_card] #convert list items to integers cause math
print(cc_numbers)
doubled_numbers = [2*x for x in cc_numbers[::2]]#double every other number
print(doubled_numbers)
doubled_numbers.extend(cc_numbers[1::2])#include undoubled numbers in list (starting with 2nd number)
print(doubled_numbers)
minus_9 = [(i - 9 if i > 9 else i) for i in doubled_numbers] #includes both remainder from the subtracted numbers and numbers <= 9
print(minus_9)
sum_total = 0
for i in minus_9:
    sum_total += i
print(sum_total)
print(credit_card2[15]) #print check digit (5)
if sum_total % 5 == 0: #see if sum_total is divisible by check digit
    print('Credit card is valid')
else:
    print('Credit card is not valid!')  



