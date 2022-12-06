# list_1 = ["N", "W", "F", "R", "Z", "S", "M", "D"]
# list_2 = ["C", "J", "N", "S", "G", "Q", "P", "W"]
# list_3 = ["Q", "L", "D", "F", "Q", "V", "R", "W"]
# list_4 = ["J", "L", "G", "C", "P", "Z", "F"]
# list_5 = ["V", "S", "R", "W", "S", "P", "T"]
# list_6 = ["W", "V", "C", "F", "D", "H"]
# list_7 = ["Z", "F", "D", "N", "Z"]
# list_8 = ["G", "R", "N", "W"]
# list_9 = ["S", "M", "R"]

stacks = [
    ["N", "W", "F", "R", "Z", "S", "M", "D"],
    ["S", "G", "Q", "P", "W"],
    ["C", "J", "N", "F", "Q", "V", "R", "W"],
    ["L", "D", "G", "C", "P", "Z", "F"],
    ["S", "P", "T"],
    ["L", "R", "W", "F", "D", "H"],
    ["C", "D", "N", "Z"],
    ["Q", "J", "S", "V", "F", "R", "N", "W"],
    ["V", "W", "Z", "G", "S", "M", "R"]
]

instructions = [
    [1, 3, 9],
    [3, 5, 3],
    [4, 2, 5],
    [4, 1, 2],
    [3, 5, 7],
    [3, 1, 2],
    [4, 8, 7],
    [4, 9, 7],
    [4, 2, 7],
    [2, 3, 6],
    [3, 6, 2],
    [5, 4, 7],
    [7, 3, 7],
    [5, 6, 9],
    [2, 4, 8],
    [1, 3, 2],
    [4, 2, 7],
    [2, 2, 8],
    [8, 8, 5],
    [1, 2, 4],
    [1, 2, 9],
    [7, 5, 4],
    [31, 7, 1],
    [9, 9, 3],
    [12, 1, 9],
    [15, 1, 7],
    [4, 3, 8],
    [2, 5, 1],
    [12, 7, 5],
    [2, 8, 2],
    [12, 5, 4],
    [1, 3, 5],
    [6, 1, 3],
    [1, 1, 5],
    [1, 8, 7],
    [1, 8, 5],
    [7, 7, 8],
    [5, 8, 2],
    [11, 4, 2],
    [10, 3, 1],
    [1, 7, 5],
    [10, 1, 3],
    [5, 4, 2],
    [1, 4, 6],
    [7, 2, 3],
    [9, 9, 5],
    [15, 2, 3],
    [1, 9, 1],
    [7, 5, 3],
    [1, 2, 4],
    [2, 9, 2],
    [1, 8, 9],
    [5, 5, 3],
    [1, 8, 7],
    [1, 2, 4],
    [1, 7, 6],
    [1, 1, 6],
    [1, 6, 9],
    [1, 5, 4],
    [1, 6, 4],
    [1, 6, 8],
    [2, 9, 4],
    [12, 3, 1],
    [8, 4, 8],
    [1, 9, 8],
    [10, 8, 6],
    [1, 6, 7],
    [6, 6, 9],
    [1, 2, 7],
    [1, 4, 7],
    [2, 7, 3],
    [1, 1, 3],
    [6, 9, 1],
    [2, 6, 7],
    [12, 1, 3],
    [5, 1, 9],
    [1, 7, 3],
    [38, 3, 7],
    [19, 7, 8],
    [19, 8, 2],
    [1, 9, 6],
    [5, 3, 7],
    [2, 6, 7],
    [1, 3, 9],
    [2, 3, 6],
    [4, 2, 6],
    [6, 2, 4],
    [14, 7, 9],
    [8, 2, 5],
    [19, 9, 3],
    [6, 4, 1],
    [6, 1, 4],
    [4, 4, 3],
    [10, 7, 6],
    [1, 6, 4],
    [22, 3, 1],
    [5, 1, 6],
    [5, 5, 8],
    [1, 7, 4],
    [1, 2, 3],
    [15, 6, 9],
    [3, 8, 4],
    [2, 3, 1],
    [6, 9, 1],
    [1, 3, 9],
    [1, 3, 1],
    [1, 5, 9],
    [1, 7, 1],
    [1, 8, 2],
    [6, 9, 2],
    [2, 9, 1],
    [3, 6, 3],
    [2, 9, 5],
    [1, 6, 7],
    [2, 2, 7],
    [3, 3, 5],
    [1, 8, 9],
    [7, 4, 7],
    [1, 6, 3],
    [2, 9, 5],
    [10, 1, 5],
    [19, 1, 8],
    [9, 7, 1],
    [1, 3, 5],
    [2, 2, 4],
    [2, 2, 6],
    [2, 6, 4],
    [7, 1, 7],
    [3, 7, 3],
    [2, 4, 1],
    [3, 3, 4],
    [1, 2, 4],
    [2, 4, 1],
    [2, 4, 8],
    [20, 8, 2],
    [1, 8, 3],
    [4, 7, 8],
    [14, 2, 6],
    [3, 1, 2],
    [2, 1, 7],
    [1, 4, 6],
    [1, 1, 5],
    [4, 2, 8],
    [3, 7, 6],
    [1, 4, 6],
    [2, 7, 9],
    [1, 2, 6],
    [1, 3, 1],
    [3, 5, 8],
    [1, 1, 4],
    [2, 9, 5],
    [4, 6, 7],
    [1, 4, 1],
    [1, 8, 5],
    [1, 7, 6],
    [1, 2, 9],
    [2, 7, 1],
    [1, 1, 3],
    [1, 7, 2],
    [4, 2, 7],
    [1, 1, 3],
    [2, 3, 2],
    [9, 8, 3],
    [1, 8, 6],
    [2, 7, 3],
    [1, 7, 4],
    [1, 9, 7],
    [1, 7, 2],
    [2, 2, 8],
    [6, 5, 2],
    [5, 3, 7],
    [1, 4, 7],
    [3, 7, 1],
    [11, 5, 8],
    [2, 1, 6],
    [2, 1, 8],
    [2, 5, 9],
    [1, 7, 2],
    [2, 5, 4],
    [17, 6, 7],
    [1, 4, 1],
    [1, 1, 7],
    [1, 6, 5],
    [1, 6, 2],
    [9, 2, 5],
    [1, 6, 7],
    [9, 7, 4],
    [3, 7, 8],
    [3, 3, 4],
    [8, 7, 9],
    [11, 8, 1],
    [1, 4, 3],
    [1, 7, 4],
    [9, 9, 4],
    [5, 1, 7],
    [8, 5, 1],
    [3, 3, 4],
    [6, 7, 9],
    [3, 8, 5],
    [1, 3, 8],
    [1, 5, 8],
    [2, 9, 1],
    [3, 9, 7],
    [2, 7, 9],
    [3, 9, 8],
    [1, 7, 3],
    [1, 3, 9],
    [7, 4, 3],
    [18, 4, 2],
    [8, 1, 6],
    [1, 6, 7],
    [2, 3, 1],
    [14, 2, 6],
    [5, 1, 6],
    [5, 3, 2],
    [2, 9, 5],
    [3, 1, 8],
    [1, 7, 9],
    [3, 5, 1],
    [4, 8, 4],
    [1, 2, 7],
    [6, 2, 5],
    [2, 1, 6],
    [14, 6, 1],
    [2, 4, 7],
    [2, 4, 6],
    [12, 1, 6],
    [8, 8, 3],
    [11, 6, 1],
    [1, 1, 6],
    [15, 6, 9],
    [3, 7, 3],
    [11, 1, 4],
    [3, 5, 3],
    [10, 9, 5],
    [2, 6, 9],
    [2, 2, 5],
    [6, 3, 7],
    [7, 9, 3],
    [2, 1, 8],
    [1, 9, 6],
    [12, 3, 4],
    [13, 5, 6],
    [2, 7, 4],
    [3, 7, 5],
    [2, 8, 4],
    [15, 6, 5],
    [22, 4, 5],
    [2, 3, 6],
    [1, 7, 8],
    [2, 1, 2],
    [13, 5, 3],
    [1, 8, 6],
    [1, 6, 4],
    [1, 2, 7],
    [7, 5, 2],
    [4, 4, 8],
    [1, 6, 3],
    [3, 5, 6],
    [2, 8, 9],
    [4, 5, 1],
    [1, 9, 8],
    [4, 2, 5],
    [1, 7, 6],
    [4, 6, 3],
    [1, 6, 9],
    [1, 9, 6],
    [4, 1, 6],
    [1, 9, 4],
    [4, 6, 3],
    [1, 6, 4],
    [14, 5, 6],
    [23, 3, 1],
    [2, 5, 6],
    [1, 4, 2],
    [6, 5, 7],
    [16, 6, 5],
    [2, 2, 6],
    [2, 6, 1],
    [2, 2, 4],
    [1, 2, 8],
    [15, 1, 3],
    [4, 8, 2],
    [9, 1, 8],
    [12, 5, 7],
    [2, 5, 1],
    [1, 4, 6],
    [1, 5, 6],
    [3, 7, 3],
    [2, 8, 6],
    [1, 2, 3],
    [2, 3, 5],
    [3, 1, 9],
    [12, 3, 9],
    [4, 9, 7],
    [2, 9, 5],
    [4, 8, 5],
    [8, 7, 2],
    [6, 5, 8],
    [2, 5, 7],
    [12, 7, 1],
    [2, 6, 7],
    [11, 2, 4],
    [1, 6, 5],
    [1, 5, 8],
    [10, 8, 6],
    [7, 1, 9],
    [3, 3, 8],
    [2, 7, 4],
    [1, 5, 3],
    [9, 4, 7],
    [16, 9, 6],
    [2, 1, 6],
    [1, 7, 8],
    [2, 4, 1],
    [1, 1, 5],
    [1, 5, 7],
    [2, 3, 9],
    [5, 4, 6],
    [1, 3, 6],
    [1, 4, 5],
    [1, 5, 8],
    [16, 6, 5],
    [2, 7, 6],
    [21, 6, 2],
    [3, 8, 7],
    [1, 9, 1],
    [7, 7, 1],
    [14, 2, 5],
    [1, 9, 3],
    [1, 3, 1],
    [1, 8, 3],
    [2, 2, 6],
    [15, 5, 1],
    [20, 1, 8],
    [1, 3, 5],
    [4, 2, 8],
    [2, 1, 2],
    [2, 6, 8],
    [3, 7, 6],
    [2, 6, 7],
    [1, 7, 2],
    [6, 5, 6],
    [3, 5, 9],
    [2, 9, 6],
    [1, 9, 4],
    [2, 2, 3],
    [1, 3, 2],
    [2, 1, 4],
    [1, 3, 9],
    [2, 4, 7],
    [4, 8, 4],
    [8, 8, 6],
    [5, 6, 9],
    [6, 6, 7],
    [6, 6, 3],
    [5, 3, 2],
    [2, 2, 3],
    [10, 7, 1],
    [2, 5, 2],
    [2, 4, 1],
    [5, 5, 9],
    [2, 3, 5],
    [2, 9, 4],
    [5, 4, 8],
    [8, 9, 6],
    [16, 1, 9],
    [7, 2, 7],
    [10, 9, 4],
    [10, 4, 8],
    [1, 7, 3],
    [1, 2, 5],
    [3, 5, 7],
    [2, 3, 6],
    [5, 7, 4],
    [4, 4, 5],
    [17, 8, 3],
    [9, 6, 2],
    [17, 3, 9],
    [9, 8, 3],
    [2, 5, 6],
    [1, 5, 8],
    [5, 2, 4],
    [1, 6, 9],
    [3, 9, 5],
    [3, 7, 4],
    [13, 9, 3],
    [3, 9, 2],
    [1, 9, 8],
    [2, 6, 4],
    [9, 3, 4],
    [3, 9, 3],
    [1, 8, 1],
    [2, 5, 2],
    [5, 4, 7],
    [1, 9, 2],
    [6, 7, 2],
    [1, 9, 6],
    [9, 2, 4],
    [1, 1, 7],
    [1, 6, 5],
    [1, 7, 4],
    [4, 4, 2],
    [12, 3, 6],
    [7, 2, 5],
    [1, 2, 1],
    [1, 1, 9],
    [2, 2, 6],
    [5, 8, 2],
    [8, 6, 3],
    [1, 9, 3],
    [4, 2, 7],
    [1, 3, 2],
    [2, 2, 7],
    [1, 2, 5],
    [3, 6, 3],
    [10, 5, 8],
    [1, 5, 3],
    [1, 6, 5],
    [5, 8, 7],
    [1, 5, 8],
    [2, 6, 3],
    [5, 7, 4],
    [3, 3, 6],
    [2, 8, 6],
    [3, 8, 2],
    [1, 3, 7],
    [15, 4, 5],
    [10, 4, 1],
    [7, 3, 5],
    [1, 2, 9],
    [5, 5, 7],
    [8, 5, 9],
    [4, 3, 6],
    [3, 9, 6],
    [3, 1, 4],
    [10, 7, 4],
    [2, 2, 4],
    [2, 3, 5],
    [1, 7, 2],
    [1, 7, 6],
    [6, 6, 5],
    [7, 5, 3],
    [1, 8, 3],
    [5, 1, 6],
    [9, 5, 3],
    [14, 4, 7],
    [1, 2, 8],
    [1, 8, 2],
    [1, 6, 4],
    [2, 4, 7],
    [1, 2, 9],
    [1, 4, 8],
    [2, 1, 4],
    [8, 6, 1],
    [1, 4, 3],
    [1, 5, 8],
    [12, 7, 3],
    [1, 4, 8],
    [7, 9, 1],
    [3, 6, 2],
    [3, 8, 7],
    [1, 2, 9],
    [4, 7, 1],
    [6, 1, 7],
    [2, 2, 8],
    [7, 7, 3],
    [10, 1, 6],
    [20, 3, 1],
    [2, 6, 7],
    [1, 9, 1],
    [8, 6, 8],
    [6, 8, 9],
    [5, 3, 7],
    [2, 7, 3],
    [2, 9, 2],
    [5, 1, 3],
    [2, 9, 8],
    [8, 3, 7],
    [6, 8, 3],
    [1, 9, 8],
    [19, 1, 6],
    [17, 3, 6],
    [2, 2, 4],
    [1, 3, 5],
    [1, 4, 1],
    [1, 4, 8],
    [2, 8, 5],
    [1, 5, 1],
    [1, 5, 4],
    [1, 5, 7],
    [2, 1, 3],
    [15, 7, 4],
    [1, 9, 7],
    [2, 7, 6],
    [21, 6, 4],
    [17, 6, 8],
    [2, 3, 5],
    [29, 4, 9],
    [15, 9, 7],
    [1, 5, 1],
    [9, 8, 2],
    [10, 9, 3],
    [8, 2, 6]
]

# for instruction in instructions:
#     for i in range(instruction[0]):
#         stacks[instruction[2] - 1].insert(0, stacks[instruction[1] - 1].pop(0))

for instruction in instructions:
    moved_items = stacks[instruction[1]-1][0:instruction[0]]
    stacks[instruction[1]-1] = stacks[instruction[1]-1][instruction[0]:]
    for item in reversed(moved_items):
        stacks[instruction[2] - 1].insert(0, item)

print(stacks)

tops = []
for stack in stacks:
    tops.append(stack[0])

answer = "".join(tops)

print(tops)
print(answer)
