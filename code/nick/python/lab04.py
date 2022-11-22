# establish values of all possible cards
card_values_dict = {
    'a': [1, 11],
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


def hand_builder():
    hand_value_no_aces = 0
    aces = []
    questions_left = 3
    which_card = {
        3: 'first',
        2: 'second',
        1: 'third',
    }

    while questions_left > 0:
        while True:
            # mandate lower case for edge case
            card_addition = input(
                f'What is your {which_card[questions_left]} card?\n').lower()
            # if response is valid, keep going
            if card_addition in card_values_dict.keys():
                break
            # if not, ask again
            else:
                print('Invalid response. Try again.')

        # store our aces in our list
        if card_addition == 'a':
            aces.append(card_addition)
        # add standard cards' values to our hand total
        else:
            hand_value_no_aces += card_values_dict[card_addition]

        questions_left -= 1

    return hand_value_no_aces, aces


def ace_manager(aces: list, hand_value: int):
    '''Multiplies the amount of possible hands by 2 for each ace dealt 
    and adds one possible value of ace to each hand created. 
    Compiles all possible hands into a list'''
    # create a list of all possible hands that currenty exist, starts with hand minus aces
    list_of_poss_hands = [hand_value]
    # for each ace, adjust our list of possible hands using another function
    for a in aces:
        list_of_poss_hands = hand_adjustor(list_of_poss_hands)

    return list_of_poss_hands


def hand_adjustor(poss_hands: list):
    '''takes possible hands and doubles it, adding a possible possible value for 'a' to each'''
    # create a list to store each hand as we generate it
    new_possible_hands = []
    # replace each existing hand
    for hand in poss_hands:
        # with 2 new hands using each of the ace's values
        for value in card_values_dict['a']:
            # add ace value to hand to be adjusted
            total_hand_value = hand + value
            # store the adjusted hand in our list of new hands
            new_possible_hands.append(total_hand_value)
    # give the list of new hands to our ace_manager function to be used with additional aces
    return new_possible_hands


def advise(hand):
    '''advises the user based on the total of their hand'''
    if hand < 17:
        return 'Hit!'
    if hand == 21:
        return 'Blackjack!'
    if hand > 21:
        return 'Already busted :('
    else:
        return 'Stay'


def advisor():
    hand_value_no_aces, aces = hand_builder()
    final_list_poss_hands = ace_manager(aces, hand_value_no_aces)
    # remove all redundant hands
    final_unique_hands = []
    for hand in final_list_poss_hands:
        if hand not in final_unique_hands:
            final_unique_hands.append(hand)

    # put the hands in ascending order
    final_unique_hands.sort()

    # for user experience, put a blackjack at the top of the list
    if 21 in final_unique_hands:
        final_unique_hands.insert(
            0, final_unique_hands.pop(final_unique_hands.index(21)))

    # deliver our advise
    final_advise = ''
    for final_hand in final_unique_hands:
        final_advise += f'{final_hand} {advise(final_hand)}\n'

    return final_advise


def main():
    print('Welcome to the Blackjack Advisor!')
    print(advisor())


if __name__ == '__main__':
    main()
