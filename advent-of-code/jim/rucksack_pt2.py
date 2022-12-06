from string import ascii_letters

with open('rucksack_data.txt') as f:
    rucksack_data: str = f.read()

rucksack_data = rucksack_data.split('\n')

rucksack_groups = []

for i in range(0, len(rucksack_data), 3):
    rucksack_groups.append(rucksack_data[i: i+3])

badges = []
for rucksack_group in rucksack_groups:
    for letter in ascii_letters:
        if letter in rucksack_group[0] and letter in rucksack_group[1] and letter in rucksack_group[2]:
            badges.append(letter)

total = 0
for item in badges:
    total += ascii_letters.index(item) + 1

print(total)
