with open('rps_data.txt') as f:
    rps_data: str = f.read()

rps_data = rps_data.split('\n')

# outcome_dict = {
#     'A X': 4,
#     'A Y': 8,
#     'A Z': 3,
#     'B X': 1,
#     'B Y': 5,
#     'B Z': 9,
#     'C X': 7,
#     'C Y': 2,
#     'C Z': 6,
# }

outcome_dict = {
    'A X': 3,
    'A Y': 4,
    'A Z': 8,
    'B X': 1,
    'B Y': 5,
    'B Z': 9,
    'C X': 2,
    'C Y': 6,
    'C Z': 7,
}

outcomes = []
for rps in rps_data:
    outcomes.append(outcome_dict[rps])

print(sum(outcomes))
