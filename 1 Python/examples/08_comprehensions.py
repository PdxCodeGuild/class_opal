'''List Comprehensions'''

numbers = []
for x in range(10):
    numbers.append(x ** 2)

# new_list = [appended_value for thing in things]
numbers = [x ** 2 for x in range(10)]

print(numbers)


# comprehension with conditions
numbers = [1, 2, 3, 4, 5]
evens = []
for num in numbers:
    if num % 2 == 0:
        evens.append(num)

evens = [num for num in numbers if num % 2 == 0]


'''Practice 1'''

hats = ['baseball cap', 'fedora', 'derby', 'panama']

for hat in hats:
    print(hat)

print_returns = [print(hat) for hat in hats]
print(print_returns)

# [get_value(key) for key in val_list]

'''Practice 2'''

dogs = ['lassie', 'fido', 'pickle', 'jack-jack', 'clifford']

dog_facts = []
for dog in dogs:
    dog_facts.append(f'{dog.capitalize()} is a good boy')

dog_facts = [f'{dog.capitalize()} is a good boy' for dog in dogs]
print(dog_facts)


'''Practice 3'''
numbers = [1, 238, 74, 364, 65, 23, 765]

evens = []
odds = []
for num in numbers:
    if num % 2 == 0:
        evens.append(num)
    else:
        odds.append(num)


evens = [num for num in numbers if num % 2 == 0]
odds = [num for num in numbers if num % 2 == 1]

print(evens, odds)

'''Nested List Comprehension'''
spring = ['march', 'april', 'may']
summer = ['june', 'july', 'august']
fall = ['september', 'october', 'november']
winter = ['december', 'january', 'february']

seasons2d = [spring, summer, fall, winter]

months = []
for season in seasons2d:
    for month in season:
        months.append(month)


seasons = [[print(month) for month in season] for season in seasons2d]
print(seasons)
print(months)
