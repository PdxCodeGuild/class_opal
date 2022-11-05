# three card blackjack game with strategic advice
playing_cards = ['A', "2", "3", "4", "5", "6", "7", "8", "9", "10", 'J', 'Q','K']
input_error_message = "You must enter a valid playing card (A, 2, 3, 4, 5, 6, 7, 8, 9, 10, J, Q, or K)."

# get user to input three card values
while True:
    card_1 = input("What's your first card?: ")
    if card_1 in playing_cards:
        break
    else:
        print(input_error_message)

while True:
    card_2 = input("What's your second card?: ")
    if card_2 in playing_cards:
        break
    else:
        print(input_error_message)      

while True: 
    card_3 = input("What's your third card?: ")
    if card_3 in playing_cards:
        break
    else:
        print(input_error_message)

# collect cards in list
cards = [card_1, card_2, card_3]

card_values = []
total = 0

# convert Ace and face cards to integer values
point_value_conversions = {
    'A': 11,
    'J': 10,
    'Q': 10,
    'K': 10
}

for card in cards:
    try:
        card = point_value_conversions[card]
    except KeyError:
        pass
    card_values.append(card)

# convert number cards to integer values and calculate hand total
for card_value in card_values:
    card_value = int(card_value)
    total += card_value

# output strategic advice based on hand total
if total < 17:
    advice = "Hit"
elif total < 21:
    advice = "Stay"
elif total == 21:
    advice = "Blackjack!"
else:
    if cards.count('A') == 0:
        advice = "Already Busted"
    elif cards.count('A') == 1:
        total = total - 10
        if total < 17 + 10:
            advice = "Hit"
        elif total < 21 + 10:
            advice = "Stay"
        elif total == 21 + 10:
            advice = "Blackjack!"
        else:
            advice = "Already Busted"
    elif cards.count('A') == 2:
        if total < 17 + 10:
            total = total - 10
            advice = "Hit"
        elif total < 21 + 10:
            total = total - 10
            advice = "Stay"
        elif total == 21 + 10:
            total = total - 10
            advice = "Blackjack!"
        else:
            total = total - 20
            advice = "Hit"
    else:
        total = 13
        advice = "Hit"

print(f"{total} {advice}")

