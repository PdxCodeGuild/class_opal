num_cards = {'2':2,'3':3,'4':4, '5':5, '6':6, '7':7, '8':8, '9':9, '10':10,'A':1,'J':10,'Q':10,'K':10}

def blackjack():
    hand = []
        
    first_card = input("What's your first card? ")
    hand.append(first_card)
    second_card = input("What's your second card? ")
    hand.append(second_card)
    third_card = input("What's your third card? ")
    hand.append(third_card)
    print(hand)
       
    total = num_cards[first_card] + num_cards[second_card] + num_cards[third_card]
    print(total)            

    if total <= 10 and 'A' in hand:
        num_cards['A']:11
    else:
        num_cards['A']:1
    if int(total) < 17:
        print(total, "Hit")
    elif int(total) >= 17 and int(total) < 21:
        print(total, "Stay")
    elif int(total) == 21:
        print(total, "Blackjack!")
    elif int(total) > 21:
        print(total, "Already Busted")
blackjack()

    


