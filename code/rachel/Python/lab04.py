#generate random numbers using random.randint(x,y) & generate winning ticket
#create pick6 function to generate random tickets
#create number matching function to compare winning ticket to random tickets
#for loop that runs pick6 function 100,000 times
    #for every instance of the loop running, subtract 2 from balance
    #for every instance, run number matching function to compare tickets & return how many matching pairs of numbers occur in each loop
#add if / elif to each loop that tells it how much to add to the balance based on how many matching pairs are in each loop
#print balance
import random
winning_ticket = [random.randint(1, 99) for i in range(6)]
print(winning_ticket) #<class 'list'>
balance = 0
balance = int(balance)

def pick6(): #argument not needed since function needs to generate random_ticket (only add if modifying st that already exists)
    ticket = [random.randint(1, 99) for i in range(6)]
    return ticket

def number_matches(winning_ticket, ticket): #argument included because the two already exist and will be modified by this function
    num_matches = 0
    #num_matches = int(num_matches)
    for i, j in zip(winning_ticket, ticket):
        if i == j:
            num_matches += 1
    return num_matches

for i in range(100000): #make sure no commas in numbers!!
    ticket = pick6() #call the function
    #ticket = pick6(ticket) #call the function
    balance -= 2
    expenses = (i * 2) + 2
    num_matches = number_matches(winning_ticket, ticket)
    if num_matches == 1:
        balance += 4
    elif num_matches == 2:
        balance += 7
    elif num_matches == 3:
        balance += 100
    elif num_matches == 4:
        balance += 50000
    elif num_matches == 5:
        balance += 1000000
    elif num_matches == 5:
        balance += 25000000

balance1 = balance - expenses
final_balance = balance1 / expenses

print(f'Expenses = ${expenses} and earnings = ${balance} so the ROI is {final_balance:.2f}.')
