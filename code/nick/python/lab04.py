card_values_dict = {
    'a': 1,
    '2': 2,
    '3': 3,
    '4': 4,
    '5': 5,
    '6': 6,
    '7': 7,
    '8': 8,
    '9': 9,
    '10': 10,
    'j': 10,
    'q': 10,
    'k': 10,
}

hand_value = 0
which_card = {
    3: 'first',
    2: 'second',
    1: 'third',
}                  

questions_left = 3
while questions_left > 0:
    while True:
        card_addition = input(
            f'What is your {which_card[questions_left]} card?\n').lower()
        if card_addition in card_values_dict.keys():
            break
        else:
            print('Invalid response. Try again.')

    hand_value += card_values_dict[card_addition]

    questions_left -= 1


def advisor(hand):
    if hand < 17:
        return 'Hit!'
    if hand == 21:
        return 'Blackjack!'
    if hand > 21: 
        return 'Already busted :('
    else:
        return 'Stay'


print(hand_value, advisor(hand_value))