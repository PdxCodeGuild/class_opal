"""
A simple Pick6 program
"""
from random import randint

trials = 100000

def get_numbers():
    """ computer picks 6 random numbers """
    computer_numbers = []
    for _ in range(6):
        computer_numbers.append(randint(1,99))
    return computer_numbers

def calculate_match_total(computer_numbers, player_numbers):
    """ calculate the number of matches """
    match_total = 0
    for i in range(6):
        if computer_numbers[i] == player_numbers[i]:
            match_total +=1
        else:
            pass
    return match_total

def calculate_roi(earnings):
    """ calculate return on investment from the game"""
    net_earnings = earnings - (2 * trials)
    return  100*net_earnings/(2 * trials)

def run_game():
    """run the Pick6 game for number of trials"""
    computer_numbers = get_numbers()
    winnings = [0, 4, 7, 100, 50000, 1000000, 25000000]
    total_earnings = 0
    j = 0
    while j < trials:
        player_numbers = get_numbers()
        match_total = calculate_match_total(computer_numbers, player_numbers)
        total_earnings += winnings[match_total]
        j += 1
    print(f"My earnings: {total_earnings}")
    my_expenses = (2 * trials)
    print(f"My expenses: {my_expenses}")
    my_roi = calculate_roi(total_earnings)
    print(f"My ROI: {my_roi}%")

run_game()



