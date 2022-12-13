from itertools import combinations


teams = {"team_diamond": ('Josh', 'Lizzie', 'DJ'),
         "team_3": ('Nick', 'Leslie', 'Hayato', 'Jim'),
         "team_indecisive": ('Nick', 'DJ', 'Leslie'),
         "team_pumpkin_spice": ('Jim', 'Hayato', 'Josh', 'Lizzie'),
         "team_tic_tap_nope": ('Nick', 'Josh', 'Hayato', 'Lizzie'),
         "team_phillies": ('Jim', 'Leslie', 'DJ'),
         "team_world_cup_spoilers": ('Leslie', 'Lizzie', 'Josh'),
         "team_our_code_socks": ('Jim', 'Nick', 'Hayato'),
         "room 1": ('Jim', 'Lizzie', 'Nick'),
         "room 2": ('Josh', 'Hayato', 'Leslie', 'Rachel')
         }

students = [
    "Jim",
    "Lizzie",
    "Hayato",
    "Nick",
    "Josh",
    "Leslie",
    "Rachel"
]

pairings = combinations(students, 2)
pairing_counts = dict.fromkeys(pairings, 0)
for pair in pairing_counts:
    for team in teams:
        if pair[0] in teams[team] and pair[1] in teams[team]:
            pairing_counts[pair] += 1

sorted_pairs = list(pairing_counts.items())
sorted_pairs.sort(key=lambda k: k[1])

for pair in sorted_pairs:
    print(pair)
