class ATM:
    """A simple model of an ATM"""
    def __init__(self, transactions=[], balance=0.0, interest_rate=0.001):
        self.transactions: list = transactions
        self.balance: float = balance
        self.interest_rate: float = interest_rate

    def check_balance(self):
        return self.balance
    
    def deposit(self, amount):
        self.balance += amount
        self.transactions.append(f"user deposited ${amount}")
    
    def check_withdrawal(self, amount):
        if amount <= self.balance:
            return True
    
    def withdraw(self, amount):
        self.balance -= amount
        self.transactions.append(f"user withdrew ${amount}")
        
    def calc_interest(self):
        return self.interest_rate * self.balance

    def print_transactions(self):
        print(self.transactions)

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
    elif command == 'transactions':
        atm.print_transactions()
    elif command == 'help':
        print('Available commands:')
        print('balance  - get the current balance')
        print('deposit  - deposit money')
        print('withdraw - withdraw money')
        print('interest - accumulate interest')
        print('transactions - get a list of account transactions')
        print('exit     - exit the program')
    elif command == 'exit':
        break
    else:
        print('Command not recognized')