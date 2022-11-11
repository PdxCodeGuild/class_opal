# Lab 12: ATM
# Implement the initializer, as well as the following functions:

class ATM():
    def __init__(self, balance = 0, interest_rate = 0.01): #balance of $0 and int rate of 0.1%
        self.balance = balance
        self.interest_rate = interest_rate
    # returns the account balance
    def check_balance(amount):
        return amount.balance
    # deposits the given amount in the account
    def deposit(self, amount):
        self.balance += amount
        return self.balance + amount
    # returns true if the withdrawn amount won't put the account in the negative
    def check_withdrawal(self, amount):
        if self.balance >= amount:
            return True
        else:
            return False
    # withdraws the amount from the account and returns it
    def withdraw(self, amount):
        self.balance -= amount
        return self.balance - amount
    # returns the amount of interest calculated on the account
    def calc_interest(self, amount):
        self.deposit * self.interest_rate

atm = ATM() # create an instance of our class
print('Welcome to the ATM')
while True:
    command = input('Enter a command: ')
    if command == 'balance':
        balance = atm.check_balance() # call the check_balance() method
        print(f'Your balance is ${balance}')
    elif command == 'deposit':
        amount = float(input('How much would you like to deposit? '))
        atm.deposit(amount) # call the deposit(amount) method
        print(f'Deposited ${amount}')
    elif command == 'withdraw':
        amount = float(input('How much would you like '))
        if atm.check_withdrawal(amount): # call the check_withdrawal(amount) method
            atm.withdraw(amount) # call the withdraw(amount) method
            print(f'Withdrew ${amount}')
        else:
            print('Insufficient funds')
    elif command == 'interest':
        amount = atm.calc_interest() # call the calc_interest() method
        atm.deposit(amount)
        print(f'Accumulated ${amount} in interest')
    elif command == 'help':
        print('Available commands:')
        print('balance  - get the current balance')
        print('deposit  - deposit money')
        print('withdraw - withdraw money')
        print('interest - accumulate interest')
        print('exit     - exit the program')
    elif command == 'exit':
        break
    else:
        print('Command not recognized')


# Version 2

# Have the ATM maintain a list of transactions. Every time the user makes a deposit or withdrawal, add a string to a list saying 'user deposited $15' 
# or 'user withdrew $15'. Add a new method print_transactions() to your class for printing out the list of transactions, and add a transactions option 
# to your REPL loop.