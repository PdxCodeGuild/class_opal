from random import sample

TICKET_COST: int = 2
ITERATIONS: int = 100_000
PAYOUTS: dict = {
    0: 0,
    1: 4,
    2: 7,
    3: 100,
    4: 50_000,
    5: 1_000_000,
    6: 25_000_000,
}


def make_ticket() -> list:
    '''returns a ticket with 6 numbers between 1 and 99'''
    return sample(range(1, 99), 6)


def count_matches(winner, ticket) -> int:
    matches: int = 0
    for i in range(len(winner)):
        if winner[i] == ticket[i]:
            matches += 1
    return matches


def play() -> tuple:
    expenses: int = TICKET_COST * ITERATIONS
    winning_ticket: list = make_ticket()
    winnings: int = 0

    for _ in range(ITERATIONS):
        matches: int = count_matches(winning_ticket, make_ticket())
        winnings += PAYOUTS[matches]

    return winnings, expenses


if __name__ == '__main__':
    winnings, expenses = play()

    print(f'''
    balance: {winnings - expenses}
    winnings: {winnings}
    expenses: {expenses}
    ROI: {(winnings - expenses) / expenses}
    ''')
