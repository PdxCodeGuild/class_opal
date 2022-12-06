# Let's write a python program to give basic blackjack playing advice during a game by asking the player for cards. First, ask the user for three playing cards (A, 2, 3, 4, 5, 6, 7, 8, 9, 10, J, Q, or K). Then, figure out the point value of each card individually. Number cards are worth their number, all face cards are worth 10. At this point, assume aces are worth 1. Use the following rules to determine the advice:

# * Less than 17, advise to "Hit"
# * Greater than or equal to 17, but less than 21, advise to "Stay"
# * Exactly 21, advise "Blackjack!"
# * Over 21, advise "Already Busted"

# Print out the current total point value and the advice.

# ```
# What's your first card? Q
# What's your second card? 2
# What's your third card? 3
# 15 Hit

# What's your first card? K
# What's your second card? 5
# What's your third card? 5
# 20 Stay

# What's your first card? Q
# What's your second card? J
# What's your third card? A
# 21 Blackjack!

blackjack_options = {
    "A": 1, "2": 2, "3": 3, "4": 4, "5": 5,
    "6": 6, "7": 7, "8": 8, "9": 9, "10": 10,
    "J": 10, "Q": 10, "K": 10
}


card_list = []


first_card = input(f"What's your first card?: ")
card_list.append(blackjack_options[first_card])

second_card = input(f"What's your second card?: ")
card_list.append(blackjack_options[second_card])

third_card = input(f"What's your third card?: ")
card_list.append(blackjack_options[third_card])

card_sum = sum(card_list)

if card_sum == 21:
    print(f"{card_sum} BLACKJACK!!!!!!")
elif card_sum >= 17:
    print(f"{card_sum} I would stay if I was you")
elif card_sum > 21:
    print(f"{card_sum} Already Busted.... Sorry :(")
else:
    print(f"{card_sum} HIT!!!")
