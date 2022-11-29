from lab_12_volume_2 import ATM

atm = ATM()


def test_check_balance():
    atm = ATM()
    assert atm.balance == 0
    assert atm.check_balance() == 0
    assert type(atm.balance) is int


def test_deposit():
    atm = ATM()
    atm.deposit(100)
    assert atm.check_balance() == 100

    atm = ATM()
    atm.deposit(-100)
    assert atm.check_balance() == -100


def test_check_withdrawal():
    atm = ATM()
    assert atm.check_withdrawal(-100) == True

    amount = 50
    atm.deposit(amount)
    assert atm.check_withdrawal(amount) == True


def test_withdraw():
    atm = ATM()
    atm.withdraw(-10)
    assert atm.balance == 10

    atm = ATM()
    atm.withdraw(100)
    assert atm.balance == -100

    atm = ATM(balance=950)
    atm.withdraw(150)
    assert atm.balance == 800

def test_calc_interest():
    atm = ATM(balance=1000, interest_rate=0.05)
    assert round(atm.calc_interest()) == 50

    atm = ATM(balance=-50)
    assert atm.calc_interest() == -50 * 0.001


def test_print_transactions():
    atm = ATM(transactions=[], balance=0.0)
    atm.deposit(900)
    assert type(atm.transactions) == list
    atm.withdraw(100)
    assert atm.transactions == [
        "user deposited $900", "user withdrew $100"]