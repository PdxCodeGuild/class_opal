# Lab 5 - Pick6 - Version 1

from random import randint


# Creates a function to return a list of 6 random integers from 1 to 99
def pick6():
    return [randint(1, 99) for num in range(6)]


winning_numbers = pick6()


# Creates a function to compare the value and position of integer matches between 2 lists.  Increases the 'balance' variable based upon matches.
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
expenses = 0

# Loops through 'num_matches' function 100k times, decreasing total $2 for each ticket purchase, increasing total based upon winnings, and increasing expenses by $-2. 
for pick in range(100000):
    total += num_matches(winning_numbers, pick6())
    total -= 2
    expenses -= 2

print(f"Your final balance is ${total}.")

# Version 2 - ROI

ROI = total / (expenses * -1)
print(f'''
Your earnings are {total + (expenses * -1)}.
Your expenses are {expenses}.
Your return on investment is {ROI}.
''')