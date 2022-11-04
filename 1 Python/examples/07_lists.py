seasons = ['spring', 'summer', 'fall', 'winter']

# access by index
print(seasons[2])


"""Nested List Access"""
spring = ['march', 'april', 'may']
summer = ['june', 'july', 'august']
fall = ['september', 'october', 'november']
winter = ['december', 'january', 'febuary']

seasons2d = [spring, summer, fall, winter]

july = seasons2d[1][1]
print(july)  # 'july'
print(seasons2d[2][0][3])  # 't'

# find the index inside a list by its value
# list.index() returns the index of the FIRST instance of whatever you search for
summer_list = seasons2d.index(summer)
print(summer_list)
july = seasons2d[seasons2d.index(summer)][1]


# reassign value by index
seasons2d[3][2] = 'february'
# print(seasons2d[3])

# looping over a list
for season in seasons2d:
    # print(season)
    ...

# looping over a list with its index
for i in range(len(seasons2d) - 1):
    # print("*" * 10)
    # print(seasons2d[i])
    ...

# nested loop
for season in seasons2d:
    for month in season:
        # print(month)
        ...

# nested loop with index
for i in range(len(seasons2d)):
    for j in range(len(seasons2d[i])):
        # print(seasons2d[i][j])
        ...


'''Inclusion
this_element in this_list
'''
grocery_list = ['apples', 'cheese', 'beans',
                'cheese', 'cheese', 'cheese', 'cheese']
items_to_add = ['milk', 'bread', 'beans']
for item in items_to_add:
    if item not in grocery_list:
        grocery_list.append(item)
# print(grocery_list)


'''List methods'''

# # extend
# grocery_list.extend(items_to_add)
# print("*" * 10)
# print(grocery_list)

# # insert
# grocery_list.insert(2, 'kale')
# grocery_list.insert(2, ['beans again'])
# # print(grocery_list)

# # remove (only removes first instance it finds)
# output = grocery_list.remove('cheese')
# # grocery_list.remove('cheese')
# # print(output)
# print(grocery_list)

# index (returns index of first instance)
beans_index = grocery_list.index('beans')
# print(beans_index)

# # pop (removes AND returns the element at a given index)
# last_thing = grocery_list.pop()
# print(last_thing)
# fourth_thing = grocery_list.pop(3)
# print(fourth_thing)
# print(grocery_list)

# kale_index = grocery_list.index('kale')
# kale = grocery_list.pop(kale_index-1)
# print(grocery_list)

# count
cheese_count = grocery_list.count('cheese')
# print(cheese_count)

# remove all instances
while 'cheese' in grocery_list:
    grocery_list.remove('cheese')
# print(grocery_list)


"""Slicing"""

first_four = grocery_list[0:4]
# print(first_four)
# print(grocery_list[:4])
# print(grocery_list[-1])
# print(grocery_list[-1:1:-1])

languages_frameworks_engines_etc = [
    'Unity',
    'Angular',
    'French',
    'Django Rest Framework',
    'Russian',
    'Lua',
    'Vue',
    'Pascal',
    'Godot',
    'JavaScript',
    'Korean',
    'PHP',
    'Django',
    'Perl',
    'Dutch',
    'CSS',
    'Express',
    'HLSL',
    'HTML',
    'Unreal Engine',
    'Dothraki',
    'Flask',
    'Elvish',
    'Doggo-Speak',
    'Python',
    'High Valyrian',
    'Morse Code',
    'C++'
]

print(languages_frameworks_engines_etc[4:10])
print(languages_frameworks_engines_etc[9:3:-1])
print(languages_frameworks_engines_etc[9:3])  # []
print(languages_frameworks_engines_etc[-1:10:-2])
# print all of the course sections in the order we will cover them
print(languages_frameworks_engines_etc[-4:2:-3])
