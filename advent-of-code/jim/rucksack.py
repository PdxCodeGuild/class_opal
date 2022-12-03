from string import ascii_letters

with open('rucksack_data.txt') as f:
    rucksack_data: str = f.read()

rucksack_data = rucksack_data.split('\n')

rucksack_lengths = [int(len(rucksack)/2) for rucksack in rucksack_data]

duplicate_items = []
for i, rucksack in enumerate(rucksack_data):
    compartment_1 = rucksack[0:rucksack_lengths[i]]
    compartment_2 = rucksack[rucksack_lengths[i]:]
    for item in rucksack:
        if item in compartment_1 and item in compartment_2:
            duplicate_items.append(item)
            break

total = 0
for item in duplicate_items:
    total += ascii_letters.index(item) + 1

# print(rucksack_lengths)

print(len(rucksack_data))
print(len(duplicate_items))
print(total)
