class ATM:
    # initializer with default values
    def __init__(self, list_of_transactions=[], balance=0, interest_rate=0.001):
        self.balance = balance  # member variables
        self.interest_rate = interest_rate
        self.list_of_transactions = list_of_transactions

    def check_balance(self):  # method
        return self.balance  # returns account balance

    def deposit(self, amount):
        self.balance += amount  # deposits given amount in account
        self.list_of_transactions.append(f"User deposited ${amount}")
        print(self.list_of_transactions)
        return amount

    def check_withdrawal(self, amount):
        if amount < self.balance:  # if withdrawl won't put account in negative, return True
            return True
        else:
            return False

    def withdraw(self, amount):  # withdraws amount from account and returns it
        self.balance -= amount
        self.list_of_transactions.append(f"User withdrew ${amount}")
        return self.balance

    # returns amount of interest calculated on account.
    def calc_interest(self):
        interest = self.balance * self.interest_rate
        print(interest)
        return interest

    def print_transactions(self):
        for transaction in self.list_of_transactions:
            print(transaction)


if __name__ == '__main__':
    atm = ATM()
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
            balance = atm.check_balance()  # call the check_balance() method
            print(f'Your balance is ${balance}')
        elif command == 'deposit':
            amount = float(input('How much would you like to deposit? '))
            atm.deposit(amount)        # call the deposit(amount) method
            print(f'Deposited ${amount}')
        elif command == 'withdraw':
            amount = float(input('How much would you like '))
            # call the check_withdrawal(amount) method
            if atm.check_withdrawal(amount):
                atm.withdraw(amount)  # call the withdraw(amount) method
                print(f'Withdrew ${amount}')
            else:
                print('Insufficient funds')
        elif command == 'interest':
            amount = atm.calc_interest()  # call the calc_interest() method
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
            atm.print_transactions()
        elif command == 'exit':
            break
        else:
            print('Command not recognized')
