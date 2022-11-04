card_1 = input("What's your first card?: ")
card_2 = input("What's your second card?: ")
card_3 = input("What's your third card?: ")

cards = [card_1, card_2, card_3]
card_values = []
total = 0

point_value_conversions = {
    'A': 1,
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

for card_value in card_values:
    card_value = int(card_value)
    total += card_value

if total < 17:
    advice = "Hit"
elif total < 21:
    advice = "Stay"
elif total == 21:
    advice = "Blackjack!"
else:
    advice = "Already Busted"

print(f"{total} {advice}" )

