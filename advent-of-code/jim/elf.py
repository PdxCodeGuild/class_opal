with open('elf_data.txt') as f:
    elf_data: str = f.read()

elf_data = elf_data.split('\n')

new_elf_data = []
for pair in elf_data:
    pair = pair.split(",")
    new_elf_data.append(pair)

assignments = []
for pair in new_elf_data:
    assignment = []
    for elf in pair:
        elf = elf.split("-")
        assignment.append(elf)
    assignments.append(assignment)

contains_count = 0
for pair in assignments:
    if (int(pair[0][0]) <= int(pair[1][0]) and int(pair[0][1]) >= int(pair[1][1])) or (int(pair[0][0]) >= int(pair[1][0]) and int(pair[0][1]) <= int(pair[1][1])):
        contains_count += 1

overlap_count = 0
for pair in assignments:
    if (int(pair[1][0]) <= int(pair[0][0]) and int(pair[0][0]) <= int(pair[1][1])) or (int(pair[1][0]) <= int(pair[0][1]) and int(pair[0][1]) <= int(pair[1][1])):
        overlap_count += 1
    elif (int(pair[0][0]) <= int(pair[1][0]) and int(pair[0][1]) >= int(pair[1][1])) or (int(pair[0][0]) >= int(pair[1][0]) and int(pair[0][1]) <= int(pair[1][1])):
        overlap_count += 1

print(overlap_count)
