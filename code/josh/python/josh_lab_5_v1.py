# Lab 5 - Pick6

from random import randint


def pick6():
    return [randint(1, 99) for num in range(6)]


winning_numbers = pick6()
pick_6_list = pick6()


def num_matches(winning, ticket):
    balance = 0
    match = 0
    for num in range(len(pick6())):
        if winning[num] == ticket[num]:
            match += 1
    if match == 6:
        balance += 25000000
    elif match == 5:
        balance += 1000000
    elif match == 4:
        balance += 50000
    elif match == 3:
        balance += 100
    elif match == 2:
        balance += 7
    elif match == 1:
        balance += 4
    else:
        balance += 0
    return balance


total = 0

for pick in range(100000):
    #pick6()
    total += num_matches(winning_numbers, pick6())
    total -= 2

print(f"Your final balance is ${total}.")


#Version 2
#The ROI (return on investment) is defined as (earnings - expenses)/expenses. Calculate your ROI, print it out along with your earnings and expenses.