deck_of_cards = {
    "A": 1,
    "2": 2,
    "3": 3,
    "4": 4,
    "5": 5,
    "6": 6,
    "7": 7,
    "8": 8,
    "9": 9,
    "10": 10,
    "J":  10,
    "Q": 10,
    "K": 10,
}

print(f"Welcome to blackjack! Your following deck choice is: ")

for deck in deck_of_cards:
    print(deck,end= " ")

print("       ")

first_hand = input(f"Please select from the following choice " )
second_hand = input(f"Please select from the following choice " )
last_hand = input(f"Please select from the following choice " )

total_hand = deck_of_cards[first_hand] + deck_of_cards[second_hand] + deck_of_cards[last_hand] 

if total_hand < 17:
    print("Hit")
elif total_hand >= 17 and total_hand < 21:
    print('Stay')
elif total_hand == 21:
    print('Blackjack!')
else:
    print('Already Busted')


