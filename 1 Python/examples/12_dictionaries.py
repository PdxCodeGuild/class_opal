'''
Dictionaries
'''

'''Keys must be immutable types
strings and ints are most common
bool and float are also valid
tuples can be dict keys, but they MUST contain ONLY immutable types
technically a range object is immutable but what are you doing??
'''

variable1 = '8'

valid_dict = {
    'string': 1,
    123: 2,
    4.5: 3,
    True: 4,
    (1, 2): 6,
    ('a', 'b'): 7,
    variable1: 8
}

# print(valid_dict)

invalid_dict = {
    # [1, 2]: 1
    # {1: 2}: 1
    # {1}: 1
}

'''Accessing values'''

class_opal_pets = {
    'Lizzie': 'Ricky',
    'Nick': 'Remy',
    'Leslie': 'Pickle',
    'Walter': 'Fido'
}

# access by key with square brackets
print(class_opal_pets['Nick'])
# print(class_opal_pets['Danny']) #KeyError: 'Danny'

# access by key with dict.get()
print(class_opal_pets.get('Lizzie'))
print(class_opal_pets.get('Danny'))  # None


'''Adding new values and updating old values'''

# print(class_opal_pets)
class_opal_pets['Gage'] = 'Chaka'
class_opal_pets['Walter'] = 'Spot'

class_opal_pets.update({'Hayato': 'Joker'})
class_opal_pets.update({'Walter': 'Mittens'})

more_pets = {
    'Baby Lizzie': 'Spirit',
    'Walter': 'Snowball'
}

class_opal_pets.update(more_pets)
# print(class_opal_pets)


'''Iterating over a dictionary'''

for key in class_opal_pets:
    val = class_opal_pets[key]
    # print(key, val)

# exactly the same thing
# for key in class_opal_pets.keys():
#     print(key, class_opal_pets[key])

# print(class_opal_pets.values())
for val in class_opal_pets.values():
    # print(val)
    ...

# print(class_opal_pets.items())
for key, val in class_opal_pets.items():
    # print(key, val)
    ...


'''Dict Methods
.get() returns the value of a key, or None
.update() merges two dictionaries
.items() returns a list-like object of tuples (key, val)
.values() returns a list-like of the values
.keys() returns a list-like of the keys

.clear() empties a dict
.copy() returns a copy
'''

# .popitem() returns a tuple of the most recently added (key, val)
# and removes from the dict
pop_return = class_opal_pets.popitem()
# print(pop_return)
# print(class_opal_pets)

# .pop() takes a key, returns the value
# and removes from the dict
pop_return = class_opal_pets.pop('Walter')
# print(pop_return)
# print(class_opal_pets)


students = (
    'Lizzie',
    'Hayato',
    'Leslie',
    'Nick'
)

student_pets: dict = dict.fromkeys(students, None)
# print(student_pets)

for student in students:
    pet_name = class_opal_pets.get(student)
    student_pets[student] = {'name': pet_name}


'''Accessing and updating nested dictionaries'''

print(student_pets['Leslie']['name'])

student_pets['Lizzie']['species'] = 'cat'
student_pets['Nick']['special skill'] = 'cooking'

# student_pets['Danny']['name'] = 'Hiccup' # KeyError: 'Danny'
student_pets['Danny'] = {'name': 'Hiccup'}
student_pets['Danny']['color'] = 'gray'

print(student_pets)


'''Navigating complex data structures'''

dans_pets = [
    {'turkey': {
        'fullname': 'Admiral Turkey Sandwich',
        'personality': 'rude',
    }},
    {'barney': {
        'named_after': 'a basset hound from a kids movie',
        'was_smart': False
    }}
]

student_pets['Danny'] = dans_pets

turkey = student_pets['Danny'][0]['turkey']['fullname'].lower()
print(turkey)

if not student_pets['Danny'][1]['barney']['was_smart']:
    print('Barney was the best dog ever')
else:
    print(':( :( :( ')


# print(student_pets)