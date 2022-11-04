def handle_card(ordinal: str, possible_values: list):
    card = input(f'What is your {ordinal} card? ').lower()
    if card in ['k', 'q', 'j']:
        for i in range(len(possible_values)):
            possible_values[i] += 10
    elif card == 'a':
        for i in range(len(possible_values)):
            val = possible_values[i]
            possible_values[i] += 1
            possible_values.append(val + 11)
    else:
        try:
            if int(card) >= 2 and int(card) <= 10:
                for i in range(len(possible_values)):
                    possible_values[i] += int(card)
            else:
                print('invalid input')
                handle_card(ordinal, possible_values)
        except ValueError:
            print('invalid input')
            handle_card(ordinal, possible_values)
    return possible_values


first = handle_card('first', [0])
second = handle_card('second', first)
hands = handle_card('third', second)

if 21 in hands:
    print('BLACKJACK!')
elif len(hands) > 1:
    hands = [val for val in hands if val <= 21]
    if min(hands) > 21:
        print('BUST')
    elif max(hands) >= 19:
        print('stay')
    elif max(hands) <= 16:
        print('hit')
    else:
        print('this hand might be worth:')
        for val in hands:
            print(f'{val} points')
        print('do what you want with that information')
else:
    if hands[0] > 21:
        print('BUST')
    elif hands[0] >= 17:
        print('stay')
    else:
        print('hit')
