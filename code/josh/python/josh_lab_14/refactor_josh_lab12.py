# Lab 12: ATM, Version 1


# class ATM():
#     def __init__(self, balance = 0, interest_rate = 0.001): #balance of $0 and int rate of 0.1%
#         self.balance = balance
#         self.interest_rate = interest_rate
#     # returns the account balance
#     def check_balance(amount):
#         return amount.balance
#     # deposits the given amount in the account
#     def deposit(self, amount):
#         self.balance += amount
#         return self.balance + amount
#     # returns true if the withdrawn amount won't put the account in the negative
#     def check_withdrawal(self, amount):
#         if self.balance >= amount:
#             return True
#         else:
#             return False
#     # withdraws the amount from the account and returns it
#     def withdraw(self, amount):
#         self.balance -= amount
#         return self.balance - amount
#     # returns the amount of interest calculated on the account
#     def calc_interest(self, amount):
#         amount = self.balance * self.interest_rate
#         return (round(amount, 2))


# atm = ATM() # create an instance of our class
# print('Welcome to the ATM')
# while True:
#     command = input('Enter a command: ')
#     if command == 'balance':
#         balance = atm.check_balance() # call the check_balance() method
#         print(f'Your balance is ${balance}')
#     elif command == 'deposit':
#         amount = float(input('How much would you like to deposit? '))
#         atm.deposit(amount) # call the deposit(amount) method
#         print(f'Deposited ${amount}')
#     elif command == 'withdraw':
#         amount = float(input('How much would you like? '))
#         if atm.check_withdrawal(amount): # call the check_withdrawal(amount) method
#             atm.withdraw(amount) # call the withdraw(amount) method
#             print(f'Withdrew ${amount}')
#         else:
#             print('Insufficient funds')
#     elif command == 'interest':
#         amount = atm.calc_interest(amount) # call the calc_interest() method
#         atm.deposit(amount)
#         print(f'Accumulated ${amount} in interest')
#     elif command == 'help':
#         print('Available commands:')
#         print('balance - get the current balance')
#         print('deposit - deposit money')
#         print('withdraw - withdraw money')
#         print('interest - accumulate interest')
#         print('exit - exit the program')
#     elif command == 'exit':
#         break
#     else:
#         print('Command not recognized')


# Lab 12: ATM, Version 2

# Creates a class 'ATM' that maintains a balance of deposits, withdrawals, interest earned, and prints a user transaction history.
class ATM():
    def __init__(self, balance = 0, interest_rate = 0.001): #balance of $0 and int rate of 0.1%
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
    def calc_interest(self):
        amount = self.balance * self.interest_rate
        return (round(amount, 2) + self.balance)
    # returns the transaction history
    def print_transactions(self, transactions: str):
        print('Transaction History:')
        if transactions != '':
            print(transactions)
        else:
            print('You have no transactions.')
        return transactions


atm = ATM() # create an instance of our class
print('Welcome to the ATM')

transactions = ''
if __name__ == '__main__':

    while True:
        command = input('Enter a command: ')
        if command == 'balance':
            balance = atm.check_balance() # call the check_balance() method
            print(f'Your balance is ${balance}')
        elif command == 'deposit':
            amount = float(input('How much would you like to deposit? '))
            atm.deposit(amount) # call the deposit(amount) method
            print(f'Deposited ${amount}')
            transactions += (f'User deposited ${amount}.\n')
        elif command == 'withdraw':
            amount = float(input('How much would you like? '))
            if atm.check_withdrawal(amount): # call the check_withdrawal(amount) method
                atm.withdraw(amount) # call the withdraw(amount) method
                print(f'Withdrew ${amount}')
                transactions += (f'User withdrew ${amount}.\n')
            else:
                print('Insufficient funds')
        elif command == 'interest':
            amount = atm.calc_interest(amount) # call the calc_interest() method
            atm.deposit(amount)
            print(f'Accumulated ${amount} in interest')
        elif command == 'transactions':
            atm.print_transactions(transactions) # call the print_transactions() method
        elif command == 'help':
            print('Available commands:')
            print('balance - get the current balance')
            print('deposit - deposit money')
            print('withdraw - withdraw money')
            print('interest - accumulate interest')
            print('transactions - view transaction history')
            print('exit - exit the program')
        elif command == 'exit':
            break
        else:
            print('Command not recognized')