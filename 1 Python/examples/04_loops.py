from random import choice

'''
You can loop over any iterable type
iterables: list, tuple, string, dictionary
(and some other weird things like file objects and non-native types)
'''

# looping over a list
colors = ['red', 'green', 'blue']
for color in colors:
    print(f'my favorite color is {color}')

# looping over a dictionary
class_opal = {
    'instructor': 'Danny',
    'TA': 'Gage',
    'student_count': 7,
    'grad_date': 'Feb 15'
}

for key in class_opal:
    print(f'{key} -- {class_opal[key]}')

# looping over a string
greeting = 'Hello from Class Opal'
output = ''

flag = False
for letter in greeting:
    if flag is True:
        output += letter.upper()
    else:
        output += letter.lower()
    flag = not flag

print(output)

# MAXIMUM CHAOS
greeting = 'Hello from Class Opal'
output = ''

for letter in greeting:
    if choice((True, False)):
        output += letter.upper()
    else:
        output += letter.lower()

print(output)


# nested loop

students = ["Jim",
            "Lizzie",
            "DJ",
            "Hayato",
            "Nick",
            "Josh",
            "Leslie",
            ]

for student in students:
    output = ''
    # this is just a repeat of maximum chaos
    for letter in student:
        if choice((True, False)):
            output += letter.upper()
        else:
            output += letter.lower()
    print(output)


# looping over a nested dictionary

students = {"Jim": {'name0': '0pretend your full name is here'},
            "Lizzie": {'name1': '1pretend your full name is here'},
            "DJ": {'name2': '2pretend your full name is here'},
            "Hayato": {'name3': '3pretend your full name is here'},
            "Nick": {'name4': '4pretend your full name is here'},
            "Josh": {'name5': '5pretend your full name is here'},
            "Leslie": {'name6': '6pretend your full name is here'},
            }

for name in students:
    for key in students[name]:
        student_name = students[name][key]
        print(student_name)
