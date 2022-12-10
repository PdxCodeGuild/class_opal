with open(r'C:\Users\jbrennan\Google Drive\Architecture\Tests\pdx_code_guild\fullstack_bootcamp\class_opal\advent-of-code\jim\crt.txt') as f:
    crt_data: str = f.read()

crt_data = crt_data.split('\n')

new_crt_data = []

cycle = 1
midop = False
register = 1

outcomes = {1: 1}

for instruction in crt_data:
    if instruction == 'noop':
        new_crt_data.append(instruction)
    else:
        new_crt_data.append(instruction)
        new_crt_data.append(instruction)

for instruction in new_crt_data:
    if instruction == 'noop':
        pass
    elif midop == False:
        midop = True
    else:
        midop = False
        register += int(instruction.split(' ')[1])
    cycle += 1
    outcomes[cycle] = register


def signal_strength(cycle, register):
    return cycle * register


answer = signal_strength(20, outcomes[20]) + \
    signal_strength(60, outcomes[60]) + \
    signal_strength(100, outcomes[100]) + \
    signal_strength(140, outcomes[140]) + \
    signal_strength(180, outcomes[180]) + \
    signal_strength(220, outcomes[220])

drawing = ""

position = 0

for cycle in outcomes.keys():
    if position in range(outcomes[cycle] - 1, outcomes[cycle] + 2):
        drawing += "#"
    else:
        drawing += "."

    if position > 0 and position % 39 == 0:
        drawing += "\n"
        position = 0
        continue

    position += 1

print(outcomes)
print(answer)
print(drawing[:-1])
