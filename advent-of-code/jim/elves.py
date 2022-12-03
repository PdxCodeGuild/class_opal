with open('elves.txt') as f:
    elf_data: str = f.read()

elf_data = elf_data.split("\n\n")

elf_list = []
for elf in elf_data:
    elf = elf.split("\n")
    elf_list.append(elf)

elf_calorie_list = []
for elf in elf_list:
    elf_calories = 0
    for food in elf:
        elf_calories += int(food)
    elf_calorie_list.append(elf_calories)

print(max(elf_calorie_list))

list1 = [elf_calorie_list.pop(elf_calorie_list.index(max(elf_calorie_list)))]
list1.append(elf_calorie_list.pop(
    elf_calorie_list.index(max(elf_calorie_list))))
list1.append(elf_calorie_list.pop(
    elf_calorie_list.index(max(elf_calorie_list))))

answer = sum(list1)

print(list1)
print(answer)
