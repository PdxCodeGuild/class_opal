class ATM:
    def __init__(self, balance = 0, interest_rate = 0.001): #initializer with default values
        self.balance = balance #member variables
        self.interest_rate = interest_rate
        
    def check_balance(self): #method
        return self.balance # returns account balance
    
    def deposit(self, amount):
        self.balance += amount #deposits given amount in account
       
        
    def check_withdrawal(self, amount): 
        if amount < self.balance: #if withdrawl won't put account in negative, return True
            return True        
        
    def withdraw(self, amount): #withdraws amount from account and returns it
        self.balance -= amount
        return amount
    
    def calc_interest(self): #returns amount of interest calculated on account. 
        interest = self.balance * self.interest_rate
        return interest
    
    def print_transactions(self, list_of_transactions):
        self.list_of_transactions = list_of_transactions
        print(transactions)
                                      
atm = ATM()
transactions = []
print("Welcome to the ATM")
while True:
    command = input('''
    Please enter a command.
    "Balance" -- get account balance
    "Withdraw" -- withdraw funds
    "Deposit" -- deposit funds
    "Interest" -- see earned interest
    "Transactions" -- see a list of transactions
    "Help" -- see all options

    What would you like to do? ''').lower()
    if command == 'balance':
        balance = atm.check_balance() # call the check_balance() method
        print(f'Your balance is ${balance}')
    elif command == 'deposit':
        amount = float(input('How much would you like to deposit? '))
        atm.deposit(amount)        # call the deposit(amount) method
        transactions.append(str(f"user deposited ${amount}"))
        atm.print_transactions(amount)
        print(f'Deposited ${amount}')
    elif command == 'withdraw':
        amount = float(input('How much would you like '))
        if atm.check_withdrawal(amount): # call the check_withdrawal(amount) method
            atm.withdraw(amount) # call the withdraw(amount) method
            transactions.append(str(f"user withdrew ${amount}"))
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
    elif command == "transactions":
        atm.print_transactions(amount)   
    elif command == 'exit':
        break
    else:
        print('Command not recognized')