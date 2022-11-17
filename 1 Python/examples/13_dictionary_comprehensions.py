dict1 = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}
list1 = ['a', 'b', 'c', 'd', 'e']

'''Dictionary comprehensions
{key:val for item in iterable if condition}
'''

comp1 = {letter: letter*2 for letter in list1}
print(comp1)

# this recreates the dictionary
comp2 = {k: dict1[k] for k in dict1}
print(comp2)

comp3 = {k: dict1[k]**3 for k in dict1}
print(comp3)


zoo_popularity = {
    'alligator': '8%',
    'panda': '15%',
    'hippopotamus': '3%',
    'lion': '7%',
    'rhinocerous': '2%',
    'cheetah': '6%',
    'bat': '25%'
}

long_name_exhibit = {key.capitalize(): int(zoo_popularity[key].rstrip('%'))
                     for key in zoo_popularity if len(key) > 8}

print(long_name_exhibit)
print(type(long_name_exhibit['Alligator']))


labs = {
    'unit converter': 100,
    'number to phrase': 82,
    'blackjack advice': 65,
    'pick 6': 95,
    'cc validator': 92,
    'rot13': 52,
    'peaks and valleys': 75
}


def get_difficulty(num):
    if num > 90:
        return 'easy'
    elif num > 80:
        return 'kinda easy'
    elif num > 70:
        return 'kinda hard'
    else:
        return 'hard'


curriculum = {lab: get_difficulty(score)
              for lab, score in labs.items() if score >= 70}

print(curriculum)
