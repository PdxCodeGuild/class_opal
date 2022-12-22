#create dictionary with each card's value
#ask for user input; match to dictionary
#create variable adding the three card values
# start if / elif tree

card_values = {'a': 1, 'Ace': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10, 'j': 10, 'jack': 10, 'q': 10, 'queen': 10, 'k': 10, 'king': 10}

first_card = input("What's your first card? ")
second_card = input("What's your second card? ")
third_card = input("What's your third card? ")

first_card = card_values[first_card]
second_card = card_values[second_card]
third_card = card_values[third_card]

cards_total = first_card + second_card + third_card

if cards_total <= 16:
    print(f'{cards_total} hit')
elif cards_total <= 20 :
    print(f'{cards_total} stay')
elif cards_total == 21 :
    print(f'{cards_total} blackjack!')
elif cards_total > 21 :
    print(f'{cards_total} Busted')