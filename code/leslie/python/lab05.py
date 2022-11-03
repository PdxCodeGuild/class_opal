import random
#Generate a list of 6 random numbers representing the winning tickets
my_numbers = []
winning_numbers = []
for i in range(1):
    numbers = random.sample(range(1, 100),6)
    winning_numbers.append(numbers)
    print("WINNING NUMBERS: ", winning_numbers)

#Start your balance at 0
balance = 0
earnings= 0
matching_numbers = 0
expenses = 0
#Loop 100,000 times, for each loop:
#Generate a list of 6 random numbers representing the ticket

for j in range(100000):
    random_nums = random.sample(range(0, 100),6)    
    my_numbers.append(random_nums) 
    balance -= 2  #Subtract 2 from your balance (you bought a ticket)
    expenses += 2 #calculate investment
    
    if my_numbers[j] == winning_numbers[i]: #Find how many numbers match
        matching_numbers += 1 #Add to your balance the winnings from your matches
print("Matching numbers: ", matching_numbers)

def matching_numbers_and_winnings():    
    if matching_numbers == 1:
        balance += 4
        earnings += 4
        print("You win $4!")
    elif matching_numbers == 2:
        balance += 7
        earnings += 7
        print("You win $7!")
    elif matching_numbers == 3:
        balance += 100
        earnings += 100
        print("You win $100!")
    elif matching_numbers == 4:
        balance += 50000
        earnings += 50000
        print("You win 50,000!")
    elif matching_numbers == 5:
        balance += 1000000
        earnings += 100000
        print("You win $1,000,000!")
    elif matching_numbers == 6:
        balance += 25000000
        earnings += 25000000
        print("You win $25,000,000!")
    else:
        print("YOU LOSE!")

print("$",balance)  #After the loop, print the final balance

def return_on_investment(earnings, expenses):
    return (earnings - expenses)/expenses
print("ROI: $", return_on_investment(earnings, expenses))