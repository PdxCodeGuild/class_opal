# Lab 12: ATM


class ATM:
    def __init__(self):
        self.balance: float = 0
        self.interest_rate: float = 0.1
    
    def check_balance(self) -> float:
        #returns the account balance
        return self.balance

    def deposit(self, amount):
        #deposits the given amount in the account
        self.balance = self.balance + amount
        return self.balance

    def check_withdrawal(self, amount):
        #returns true if the withdrawn amount won't put the account in the negative
        if amount <= self.balance:
            return True

    def withdraw(self,amount):
        # withdraws the amount from the account and returns it
        self.balance = self.balance - amount
        return self.balance

    def calc_interest(self):
        #returns the amount of interest calculated on the account
        return self.balance * self.interest_rate * 1

    def print_transactions(self):
        print(atm_list)


if __name__ == '__main__':
    #Put everything that's not a function
    atm = ATM() # create an instance of our class
    atm_list = []

    print('Welcome to the ATM')
    while True:
        command = input('Enter a command: ')
        if command == 'balance':
            balance = atm.check_balance() # call the check_balance() method
            print(f'Your balance is ${balance}')
        elif command == 'transactions':
            atm.print_transactions()
        elif command == 'deposit':
            amount = float(input('How much would you like to deposit? '))
            atm_list.append(f"User deposited {amount}")
            atm.deposit(amount) # call the deposit(amount) method
            print(f'Deposited ${amount}')
        elif command == 'withdraw':
            amount = float(input('How much would you like '))
            if atm.check_withdrawal(amount): # call the check_withdrawal(amount) method
                atm_list.append(f"User withdrew {amount}")
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
            print('transactions  - get list of transactions')
            print('deposit  - deposit money')
            print('withdraw - withdraw money')
            print('interest - accumulate interest')
            print('exit     - exit the program')
        elif command == 'exit':
            break
        else:
            print('Command not recognized')
