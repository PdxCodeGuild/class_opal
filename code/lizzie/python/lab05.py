import random

def pick6():
    '''
    Generate a random list of six numbers between 1 and 99.
    '''
    six_nums = []
    for i in range(0,6):
        x = random.randint(1,99)
        six_nums.append(x)
    return six_nums


def num_matches(winning, ticket):
    '''
    Determine how many matches there are between tickets.
    '''
    matches = 0

    for i in range(6):
        if winning[i] == ticket[i]:
            matches += 1
    return matches


balance = 0
tickets_bought = 0


while tickets_bought < 100000:
    balance -= 2
    user_ticket = pick6()
    winning_ticket = pick6()
    matches=num_matches(winning_ticket, user_ticket)

    if matches == 1:
        balance += 4

    if matches == 2:
        balance += 7

    if matches == 3:
        balance += 100

    if matches == 4:
        balance += 50000

    if matches == 5:
        balance += 1000000

    if matches == 6:
        balance += 25000000
    
    tickets_bought += 1


#we know rexpenses is 200000 because we will always buy 100000 tickets for $2 each.
roi = balance/200000


print(f"Your final balance is {balance} and your roi is {roi}.")