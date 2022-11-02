# Lab 4: Blackjack Advice

card_values = {
    'A': 1,
    '2': 2,
    '3': 3,
    '4': 4,
    '5': 5,
    '6': 6,
    '7': 7,
    '8': 8,
    '9': 9,
    'J': 10,
    'Q': 10,
    'K': 10
}

while True:
    card_1 = input("""
    Blackjack \"advice\". Tell me your cards from the following list: 
    \"A, 2, 3, 4, 5, 6, 7, 8, 9, J, Q, or K.\"
    What is your first card ? """)
    card_2 = input("What is your second card? ")
    card_3 = input("What is your third card? ")
    card_sum = card_values[card_1] + card_values[card_2] + card_values[card_3]
    if card_sum == 21:
        print(f"Your current hand is {card_sum}. Blackjack!")
        break
    elif card_sum >= 17 and card_sum < 21:
        print(f"Your current hand is {card_sum}. Stay.")
        break
    elif card_sum > 21:
        print(f"Your current hand is {card_sum}. You've already busted.")
        break
    else:
        print(f"Your current hand is {card_sum}. Hit.")
        break