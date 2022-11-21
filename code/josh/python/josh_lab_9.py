# Lab 9: Compute the Automated Readability Index (ARI) for a given body of text loaded in from a file

from math import ceil as round_up

relative_path = 'class_opal\code\josh\python\shelleysfrankenstein.txt'

with open(relative_path, 'r', encoding = 'utf-8') as file:
    contents = file.read()

characters = len(contents)
words = len(contents.split())
statements = len(contents.split('.'))
questions = len(contents.split('?'))
exclamations = len(contents.split('!'))
sentences = statements + questions + exclamations
ari_formula = (4.71 * (characters/words)) + (0.5 * (words/sentences)) - 21.43
filename = relative_path.split('\\').pop()

ari_scale = {
     1: {'ages': '5-6', 'grade_level': ' Kindergarten'},
     2: {'ages': '6-7', 'grade_level': ' 1st Grade'},
     3: {'ages': '7-8', 'grade_level': ' 2nd Grade'},
     4: {'ages': '8-9', 'grade_level': ' 3rd Grade'},
     5: {'ages': '9-10', 'grade_level': ' 4th Grade'},
     6: {'ages': '10-11', 'grade_level': ' 5th Grade'},
     7: {'ages': '11-12', 'grade_level': ' 6th Grade'},
     8: {'ages': '12-13', 'grade_level': ' 7th Grade'},
     9: {'ages': '13-14', 'grade_level': ' 8th Grade'},
    10: {'ages': '14-15', 'grade_level': ' 9th Grade'},
    11: {'ages': '15-16', 'grade_level': ' 10th Grade'},
    12: {'ages': '16-17', 'grade_level': 'n 11th Grade'},
    13: {'ages': '17-18', 'grade_level': ' 12th Grade'},
    14: {'ages': '18-22', 'grade_level': ' college'}
}

if ari_formula >= 14:
    ari_formula = 14
elif ari_formula == float:
    round_up(ari_formula)

print(f'''
The ARI for {filename} is {ari_formula}.
This corresponds to a{ari_scale[ari_formula]['grade_level']} level of difficulty.
That is suitable for an average person {ari_scale[ari_formula]['ages']} years old.
''')