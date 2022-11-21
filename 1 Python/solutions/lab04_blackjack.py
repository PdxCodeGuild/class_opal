def handle_card(ordinal: str, possible_values: list) -> list:
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


def get_advice(hands: list) -> str:
    if 21 in hands:
        return 'BLACKJACK!'
    elif min(hands) > 21:
        return 'BUST'
    elif len(hands) > 1:
        # hands = filter(lambda n: n <= 21, hands)
        hands = [val for val in hands if val <= 21]
        if max(hands) >= 19:
            return 'stay'
        elif max(hands) <= 16:
            return 'hit'
        else:
            vals = ''
            for val in hands:
                vals += f'{val} points\n'
            return f"this hand might be worth:\n{vals}\ndo what you want with that information"
    else:
        if hands[0] >= 17:
            return 'stay'
        else:
            return 'hit'


def main() -> str:
    first = handle_card('first', [0])
    second = handle_card('second', first)
    hands = handle_card('third', second)
    return get_advice(hands)


if __name__ == '__main__':
    print(main())
