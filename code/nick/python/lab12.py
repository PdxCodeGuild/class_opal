class ATM:
    def __init__(self, balance) -> None:
        if balance < 0:
            balance = 0
        self.balance = balance
        self.transactions = []

    def check_balance(self):
        '''
        display total balance
        '''
        return self.balance

    def deposit(self, amount):
        '''
        add deposit amount to balance, log in transaction history
        '''
        self.balance += abs(amount)
        self.transactions.append(f'You deposited ${abs(amount)}.')

    def check_withdrawal(self, amount):
        return abs(amount) <= self.balance

    def withdraw(self, amount):
        '''
        subtract withdrawal amount from balance, log in transaction history
        '''
        self.balance -= abs(amount)
        self.transactions.append(f'You withdrew ${abs(amount)}.')

    def calc_interest(self):
        '''
        calculate .1% interest of balance
        '''
        return self.balance * .001

    def print_transactions(self):
        '''
        print transaction history in order, column
        '''
        for trans in self.transactions:
            print(trans)


atm = ATM(0)  # create an instance of our class

if __name__ == '__main__':
    print('Welcome to the ATM')
    while True:
        command = input('Enter a command: ')
        if command == 'balance':
            balance = atm.check_balance()  # call the check_balance() method
            print(f'Your balance is ${balance}')
        elif command == 'deposit':
            amount = float(input('How much would you like to deposit? '))
            atm.deposit(amount)  # call the deposit(amount) method
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
        elif command == 'transactions':
            atm.print_transactions()
        elif command == 'help':
            print('Available commands:')
            print('balance  - get the current balance')
            print('deposit  - deposit money')
            print('withdraw - withdraw money')
            print('interest - accumulate interest')
            print('transactions - view transaction history')
            print('exit     - exit the program')
        elif command == 'exit':
            break
        else:
            print('Command not recognized')

    print("Goodbye!")
