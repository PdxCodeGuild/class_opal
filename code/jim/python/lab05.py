"""
A simple Pick6 program
"""
from random import randint

trials = 5

def get_computer_numbers():
    """ computer picks 6 random numbers """
    computer_numbers = []
    for _ in range(6):
        computer_numbers.append(randint(1,99))
    return computer_numbers

def get_player_numbers():
    """ player picks 6 random numbers """
    player_numbers = []
    for _ in range(6):
        player_numbers.append(randint(1,99))
    return player_numbers

def calculate_match_total(computer_numbers, player_numbers):
    """ calculate the number of matches """
    match_total = 0
    for i in range(6):
        if computer_numbers[i] == player_numbers[i]:
            match_total +=1
        else:
            pass
    return match_total

def calculate_earnings(outcome_list):
    """ calculate the player's net winnngs"""
    total_earnings = 0
    winnings = [0, 4, 7, 100, 50000, 1000000, 25000000]
    for i in range(len(winnings)):
        total_earnings += winnings[i] * outcome_list[i]
    return total_earnings

def calculate_expenses(trials):
    """ calculate the player's expenses"""
    return 2 * trials

def calculate_roi(outcome_list):
    """ calculate return on investment from the game"""
    net_earnings = calculate_earnings(outcome_list) - calculate_expenses(trials)
    return  100*net_earnings/calculate_expenses(trials)

outcomes_list = [0, 0, 0, 0, 0, 0, 0, 0]

def run_game():
    """run the Pick6 game for number of trials"""
    computer_numbers = get_computer_numbers()
    j = 0
    while j < trials:
        player_numbers = get_player_numbers()
        match_total = calculate_match_total(computer_numbers, player_numbers)
        outcomes_list[match_total] += 1
        j += 1
    print(outcomes_list)
    my_earnings = calculate_earnings(outcomes_list)
    print(f"My earnings: {my_earnings}")
    my_expenses = calculate_expenses(trials)
    print(f"My expenses: {my_expenses}")
    my_roi = calculate_roi(outcomes_list)
    print(f"My ROI: {my_roi}%")

run_game()



