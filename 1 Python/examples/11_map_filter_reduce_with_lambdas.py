from functools import reduce

'''Lambdas
anonymous function!
can any take any number of arguments, but can have only one expression

syntax:
lambda arg1, arg2, arg3: expression
lambda arg: expression if condition else expression2
'''

lambda1 = lambda x: x + 10

print(lambda1(5))
print(lambda1(68))

lambda2 = lambda x: x * 2 if x > 3 else None

print(lambda2(2))
print(lambda2(200))


'''Map, Filter, Reduce
these functions can sometimes be used in place of loops or comprehensions
they take a function as an argument
'''

'''Map
produces a new copy with 1 new value for each original value
it takes a function as the first argument
the function must take one parameter
the function must return one thing
'''

nums: list = [1, 2, 3, 4, 5]


def square(num):
    return num ** 2


squared_nums = map(square, nums)
print(squared_nums)

# The map output is a generator object
# Generators are consumed as they are looped over
squared_list = list(squared_nums)
# list casting preserves the map object in list form

for num in squared_list:
    print(num)


# map with lambda
squared_nums2 = map(lambda x: x**2, nums)
print("*" * 10, list(squared_nums2))

'''Filter
returns a new generator with ONLY the items that meet a condition
(are returned by the function)

takes a function as the first argument
the function must take one parameter
the function must return True or False
'''


def find_odd(num):
    # if num % 2 == 1:
    #     return True
    # else:
    #     return False
    return num % 2 == 1


odd_nums = filter(find_odd, nums)
print(list(odd_nums))


# filter with lambda
odd_nums2 = filter(lambda num: num % 2 == 1, nums)
print("*" * 10, list(odd_nums2))



'''Reduce
returns a single value that gets built using the helper function
no longer part of the standard library, now import using functools

takes a function as the first argument
the function takes TWO arguments
arg1 is the reduced value (the value returned by the previous iteration)
arg2 is the next element in the iterable
'''


def sum_odds(num1, num2):
    '''first item in list must be 0 or odd'''
    if num2 % 2 == 1:
        return num1 + num2
    else:
        return num1


sum_of_nums = reduce(sum_odds, nums)
print(sum_of_nums)

# reduce with lambda
sum_of_odds = reduce(lambda num1, num2: num1 + num2 if num2 % 2 == 1 else num1, nums)
print("*" *10, sum_of_odds)



def make_sentence(a, b):
    return a + ' ' + b


words = ['I', 'love', 'Python', 'especially', 'reduce']
sentence = reduce(make_sentence, words)
print(sentence)


# reduce with lambda
sentence2 = reduce(lambda a, b: a + ' ' + b, words)
print('*' *10, sentence2)