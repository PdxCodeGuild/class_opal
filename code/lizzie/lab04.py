print('''
Welcome to the (bad) Blackjack Advice-Giver!
Available cards: A, 2, 3, 4, 5, 6, 7, 8, 9, 10, J, Q, and K. 
This assumes ace has a value of 1.
''')

card1 = input("Please enter your first card: ")
card2 = input("Please enter your second card: ")
card3 = input("Please enter your third card: ")

dict_cards = {
    'A': 1,
    '2': 2,
    '3': 3,
    '4': 4,
    '5': 5,
    '6': 6,
    '7': 7,
    '8': 8,
    '9': 9,
    '10': 10,
    'J': 10,
    'Q': 10,
    'K': 10
}

num_card1 = dict_cards[card1] #accessing the dictionary so we can have only the value of the card.
num_card2 = dict_cards[card2]
num_card3 = dict_cards[card3]

total = num_card1 + num_card2 + num_card3

if total < 17:
    print(f'{total} Hit.')
    
elif total >= 17 and total < 21:
    print(f'{total} Stay.')

elif total == 21:
    print(f'{total} Blackjack!')

else:
    print(f'{total} Already Busted!')