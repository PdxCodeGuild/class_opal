import random


balance = 0


def pick6():
    number_list = []
    for i in range(0, 6):
        random_range = random.randint(1, 99)
        number_list.append(random_range)

    return number_list


def num_matches(winning, ticket):
    counter = 0
    for i in range(6):
        if winning[i] == ticket[i]:
            counter += 1
    return counter


times_played = 0
earnings = 0
expenses = 200000
while times_played < 100000:
    times_played += 1
    balance -= 2
    winning_number = pick6()
    ticket_number = pick6()

print(num_matches(winning_number, ticket_number))

# print(f"{winning_number} {ticket_number} ")

if num_matches(winning_number, ticket_number) == 6:
    balance += 25000000
    earnings += 25000000
    print("you win $25,000,000")
elif num_matches(winning_number, ticket_number) == 5:
    balance += 1000000
    earnings += 1000000
    print("you win $1,000,000")
elif num_matches(winning_number, ticket_number) == 4:
    balance += 50000
    earnings += 50000
    print("you win $50,000")
elif num_matches(winning_number, ticket_number) == 3:
    balance += 100
    earnings += 100
    print("you win $100")
elif num_matches(winning_number, ticket_number) == 2:
    balance += 7
    earnings += 7
    print("you win $7")
elif num_matches(winning_number, ticket_number) == 1:
    balance += 4
    earnings += 4
    print("you win $4")
else:
    print("you had no matches")

roi = (earnings - expenses) / expenses
print(roi)
print(balance)
