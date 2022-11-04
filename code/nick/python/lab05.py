from random import randint

winnings_by_match = {
    0: 0,
    1: 4,
    2: 7,
    3: 100,
    4: 50000,
    5: 1000000,
    6: 25000000,
}

def pick6_generator():
    '''pick 6 random numbers, and assign them to a list'''
    pick6_numbers = []
    for i in range(6):
        pick6_numbers.append(randint(1, 99))

    return pick6_numbers

# establish a winning sequence with which to compare all tickets
pick6_winner = pick6_generator()
# print(pick_6_winner) # test

def pick6_game(win_tick: int):
    '''buy 100,00 pick6 tickets, compare them against the winning ticket,
    track the expense of buying the tickets, and track earnings'''
    expenses = 0
    earnings = 0
    for i in range(100000):
        expenses += 2
        num_matches = 0
        ticket = pick6_generator()
        for num in ticket:
            if num == win_tick[ticket.index(num)]:
                num_matches += 1
            else:
                continue
        
        earnings += winnings_by_match[num_matches]

    return expenses, earnings
    

total_earnings = pick6_game(pick6_winner)[1]
total_expenses = pick6_game(pick6_winner)[0]
roi = (total_earnings - total_expenses)/total_expenses*100

def idea_analysis(roi):
    if roi > 0:
        return f'You got lucky, big time.'
    if roi < 0:
        return f'Yeah, that wasn\'t such a good idea, was it?'
    else:
        return f'Well, that could have gone worse.'

was_that_a_good_idea = idea_analysis(roi)

print(f'''
You played 100,000 games of Pick6. 
In so doing, you spent ${total_expenses} and won ${total_earnings}.
Your ROI was {roi}%.
{was_that_a_good_idea}''')