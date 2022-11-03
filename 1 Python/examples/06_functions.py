'''
Anatomy of a function:
1. keyword 'def'
2. name of the function
3. parentheses
4. OPTIONAL: any number of parameters AKA arguments
5: a colon
6: the function body, indented
7: the return, None by default
'''

'''ARGS AND KWARGS'''

'''positional argument'''


def say_hi(name):
    print(f'hello, {name}')


val = say_hi('DJ')
print(say_hi('Leslie'))

'''keyword arguments'''


def staff_bio(first_name, last_name, role='staff member', status='cool'):
    print(f'{first_name} {last_name} is a {status} {role} at PDX Code Guild')


staff_bio('Danny', 'Burrow', status='awesome', role='instructor')
staff_bio('Gage', 'Lieble', status='totally great')


'''passing args as a list, kwargs as a dictionary'''
staff_kwargs = {
    'status': 'amazing',
    'role': 'director'
}
staff_args = ['Sheri', 'Dover']

staff_bio(*staff_args, **staff_kwargs)


'''defining a function with arbitrary args and kwargs'''


def read_contents(*args, **kwargs):
    for arg in args:
        print(arg)
    for kwarg in kwargs:
        print(kwarg, kwargs[kwarg])


read_contents(1, 2, 'three', 4, keyword2=2, keyword1='one')


def add_to_list(seq, *args, required_kwarg='thing', **kwargs):
    for arg in args:
        seq.append(arg)
    return seq


print(add_to_list([1, 2, 3], 4, 5, 6, 1, 2, 'anything', 4, 5))


'''Returning from a function'''

# tuple unpacking
my_tuple: tuple = ('one', 'two', 'three')
one, two, three = my_tuple
print(three)
print(one)
print(two)


def multiply_recipe(multiplier, ing1, ing2, ing3):
    '''multiplies ingredients by the multiplier'''
    return multiplier*ing1, multiplier * ing2, multiplier*ing3


# returning multiple values
butter, sugar, eggs = multiply_recipe(4, 2, 5, 9)
print(eggs, butter, sugar)


def first_sorted(list_of_strings: list):
    '''
    given a list of strings, 
    sorts that list and returns the first value after sorting
    '''
    print(list_of_strings)
    sorted = list_of_strings.sort()
    print(list_of_strings)
    print(sorted)
    first_in_list = list_of_strings[0]
    return first_in_list


for letter in first_sorted(['barracuda', 'aardvark']):
    print(letter)


is_raining = True
is_cold = False


def is_dan_happy():
    '''returns whether or not Dan is happy based on whether it is raining and/or cold'''
    if not is_raining and not is_cold:
        return True
    else:
        return False


if is_dan_happy():
    print('hooray!')
else:
    print(':( :( :(')
