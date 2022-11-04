import random
#Generate a list of 6 random numbers representing the winning tickets

# for i in range(1):
#     numbers = random.sample(range(0, 100),6)
#     winning_numbers.append(numbers)
#     print("WINNING NUMBERS: ", winning_numbers)
def pick6():
    numbers = []
    for i in range(6):
        numbers.append(random.randint(0,100))
    return numbers


#Start your balance at 0

#Loop 100,000 times, for each loop:
#Generate a list of 6 random numbers representing the ticket
def matching_numbers_and_winnings(my_ticket, winning_numbers):    
    matching_numbers = 0
    for i in range(6):
        if my_ticket[i] == winning_numbers[i]: #Find how many numbers match
            matching_numbers += 1
    return matching_numbers


balance = 0
earnings= 0
expenses = 0
for j in range(100000):
    winning_numbers = pick6()
    my_ticket = pick6()
    balance -= 2  #Subtract 2 from your balance (you bought a ticket)
    expenses =+ 2
    if matching_numbers_and_winnings(winning_numbers, my_ticket) == 1:
        earnings += 4
    if matching_numbers_and_winnings(winning_numbers, my_ticket) == 2:
        earnings += 7
    if matching_numbers_and_winnings(winning_numbers, my_ticket) == 3:
        earnings += 100
    if matching_numbers_and_winnings(winning_numbers, my_ticket) == 4:
        earnings += 50000
    if matching_numbers_and_winnings(winning_numbers, my_ticket) == 5:
        earnings += 1000000
    if matching_numbers_and_winnings(winning_numbers, my_ticket) == 6:
        earnings += 25000000
print(earnings + balance)
print("My earnings: $",earnings)
def return_on_investment(earnings, expenses):
    return (earnings - expenses)/expenses
print("ROI: $", return_on_investment(earnings, expenses))