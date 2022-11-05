import random

def pick_6(): #defined to run the 6 numbers
    random_numbers= []
    for numbers in range(6):
        random_numbers.append(random.randint(1, 99))
    return random_numbers

def num_matches(winning_numbers, user_numbers): # going through both tickets to see if there is a match in each list
    match = 0
    if winning_numbers[0] == user_numbers[0]:
        match= match +1
    if winning_numbers[1] == user_numbers[1]:
        match= match +1
    if winning_numbers[2] == user_numbers[2]:
        match= match +1
    if winning_numbers[3] == user_numbers[3]:
        match= match +1
    if winning_numbers[4] == user_numbers[4]:
        match= match +1 
    if winning_numbers[5] == user_numbers[5]:
        match= match +1
    return match

loop_counter = 0 #just a loop counter 
balance = 0 #the amount of money being spent
winning = 0 #the total amount of winnings
while loop_counter < 100000: #the amount of loops to run
    winning_numbers = pick_6()
    user_numbers = pick_6()
    if num_matches(winning_numbers, user_numbers) == 1: # for ever run if there is a match then it will add the proper amount of money 
        winning = winning + 4
    if num_matches(winning_numbers, user_numbers) == 2:
        winning = winning + 7
    if num_matches(winning_numbers, user_numbers) == 3:
        winning = winning + 100
    if num_matches(winning_numbers, user_numbers) == 4:
        winning = winning + 50000
    if num_matches(winning_numbers, user_numbers) == 5:
        winning = winning + 1000000
    if num_matches(winning_numbers, user_numbers) == 6:
        winning = winning + 25000000
    balance = balance - 2 # the amount of money you are spending per loop
    loop_counter = loop_counter +1 

final_balance = (winning + balance) #final balance 
print(final_balance)
roi = ((winning + balance)/ balance) 
print(f'Return of Investment is {roi} and your Earnings are ${winning} and your expenses is ${balance}')
