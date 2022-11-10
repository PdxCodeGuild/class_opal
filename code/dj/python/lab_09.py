import re
from math import ceil
with open("Alice-Wonder.txt", "r", encoding="utf-8") as file:
    book = file.read()

# print(book)
ari_scale = {
    1: {'ages':   '5-6', 'grade_level': 'Kindergarten'},
    2: {'ages':   '6-7', 'grade_level':    '1st Grade'},
    3: {'ages':   '7-8', 'grade_level':    '2nd Grade'},
    4: {'ages':   '8-9', 'grade_level':    '3rd Grade'},
    5: {'ages':  '9-10', 'grade_level':    '4th Grade'},
    6: {'ages': '10-11', 'grade_level':    '5th Grade'},
    7: {'ages': '11-12', 'grade_level':    '6th Grade'},
    8: {'ages': '12-13', 'grade_level':    '7th Grade'},
    9: {'ages': '13-14', 'grade_level':    '8th Grade'},
    10: {'ages': '14-15', 'grade_level':    '9th Grade'},
    11: {'ages': '15-16', 'grade_level':   '10th Grade'},
    12: {'ages': '16-17', 'grade_level':   '11th Grade'},
    13: {'ages': '17-18', 'grade_level':   '12th Grade'},
    14: {'ages': '18-22', 'grade_level':      'College'}
}

char = list(book)
print(len(char))

words = book.split()
print(len(words))

sentence = re.split(".?!", book)
print(len(sentence))


ari_eq = ceil(4.71 * len(char) / len(words) +
              0.5 * len(words) / len(sentence) - 21.43)
print(ari_eq)

if ari_eq >= 14:
    ari_eq = 14

print(f'''
The ARI for Alice-Wonder.txt is {ari_eq}
This corresponds to a {ari_scale[ari_eq]["grade_level"]} level of difficulty
that is suitable for an average person {ari_scale[ari_eq]["ages"]} years old.
''')
