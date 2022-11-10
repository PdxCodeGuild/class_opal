from random import random, choice
import string
'''Reading a file'''

absolute_path = '/home/dan/code-guild/class_opal/1 Python/examples/data/frankenstein.txt'
relative_path = '1 Python/examples/data/fire-and-ice.txt'

with open(relative_path, 'r', encoding='utf-8') as file:
    contents = file.read()


'''Working with file contents'''

lines = contents.split('\n')

phrases = ['fr fr', 'no cap', 'mood']

# new_list = []
# for i in range(len(lines)):
#     new_list[i] = lines[i].lower

for i, line in enumerate(lines):
    line = line.lower()
    line = line.replace('fire', 'fire🔥')
    line = line.replace(' ice', ' ice🧊')

    line = line.replace('’', '')
    for char in string.punctuation:
        line = line.replace(char, '')

    if random() < 0.333:
        line += ' ' + choice(phrases)

    lines[i] = line

for l in lines:
    print(l)


'''Writing to a file'''

out_path = '1 Python/examples/data/fire-and-ice-frfr.txt'

output_content = '\n'.join(lines)

with open(out_path, 'w') as f:
    f.write(output_content)
