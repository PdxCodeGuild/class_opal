class ATM:

    def __init__(self):
        self.balance = 0
        self.interest_rate = 0.1
        self.transactions = []
    
    def check_balance(self):
        """Returns the account balance"""
        return f"{self.balance}"

    def deposit(self, amount):
        """Deposits the given amount in the account"""
        self.balance = amount + self.balance
        self.transactions.append(f'user deposited {amount}')
        return amount
  
    def check_withdrawal(self, amount):
        """Returns true if the withdrawn amount won't put the account in the negative"""
        if self.balance >= amount:
            return True

    def withdraw(self, amount):
        """Withdraw the amount from the account and returns it"""
        self.transactions.append(f'user withdrew {amount}')
        return amount

    def calc_interest(self):
        """Returns the amount of the interest calculated on the account"""
        self.earned_interest = (self.balance * self.interest_rate) / 100
        return self.earned_interest

    def print_transactions(self):
        for transaction in self.transactions:
            print(transaction)


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
        print(f'Deposited ${amount:.2f}')
    elif command == 'withdraw':
        amount = float(input('How much would you like '))
        if atm.check_withdrawal(amount): # call the check_withdrawal(amount) method
            atm.withdraw(amount) # call the withdraw(amount) method
            print(f'Withdrew ${amount:.2f}')
        else:
            print('Insufficient funds')
    elif command == 'interest':
        amount = atm.calc_interest() # call the calc_interest() method
        atm.deposit(amount)
        print(f'Accumulated ${amount:.2f} in interest')
    elif command == 'help':
        print('Available commands:')
        print('balance  - get the current balance')
        print('deposit  - deposit money')
        print('withdraw - withdraw money')
        print('interest - accumulate interest')
        print('transactions - view transaction log')
        print('exit     - exit the program')
    elif command == 'transactions':
        atm.print_transactions()
    elif command == 'exit':
        break
    else:
        print('Command not recognized')