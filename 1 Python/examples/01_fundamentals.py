# single-line comment
'''
multi-line comment
'''

# variable assignment

variable_name = 'value'
value = variable_name
value2 = 'value'

# print(id(variable_name))
# print(id(value))
# print(id(value2))


# data types in Python

an_int = 1
a_float = 1.0
a_string = 'yes'
a_boolean = True

a_list = [1, 2, 3, 'four', [5, 6], {7: 8}]
a_dict = {
    1: 2,
    3: 5,
    'four': 5.6,
    7.0: 8,
    a_string: a_boolean,
    True: False,
    1: 'what is going on??'
}
a_tuple = (1, 2, 3)  # immutable
a_set = {1, 2, 3, 1, 1, 2, 5}


def a_function():
    return "hello"


# LITERALS

msg1 = 'this is a literal value'
# msg1 is a literal because its value is hard-coded into the program
# msg2 = input('what time is it?')
# msg2 is not literal, the value will vary based on user input


# MUTABILITY
'''
Mutability means that when you change the value of a variable, it retains the same identity
lists, dictionaries, and sets are mutable
everything else is immutable
'''

val1 = 1
print(id(val1))
val1 = 'one'
print(id(val1))

colors = ['red', 'green', 'blue']
print(id(colors))
blue = colors.pop()
colors.append('yellow')
print(colors)
print(id(colors))


# ORDERED VS UNORDERED
'''
Ordered types have an order built in, the order is an inherent part of the value.
Ordered types can be accessed by index
Lists, tuples, and strings are ordered, nothing else is
'''

print(colors[1])
# print(a_dict[10])
# KeyError: 10
# dictionaries don't have indices, only keys
print(a_tuple[0])
# print(a_set[0])  # TypeError: 'set' object is not subscriptable
# subscriptable means you can loop over it
print('hello'[0])


# TYPE CONVERSION
'''
Type conversion is changing something from one type to another
It can be explicit, using casting, or an implicit result of an operation
'''

# int casting

# num = input('type a number')
# print(type(num))
# num2 = int(num)
# print(type(num2))

this_float = 3 * 1.0
print(type(this_float))
float2 = int(this_float)
print(type(float2))
print(int(False))

# float casting
print(float(1))
print(float('1'))
# print(float(input('give a number with a decimal')))


# string casting
# almost anything can be string cast!
print(type(str(1)))
print(str(1.0))
print(str([1, 2]))
print(str({1, 2, 1, 3}))
print(str({1: 2, 3: 4}))
print(str(True).upper())
print(str(a_function).upper())
# print(a_function.upper()) #AttributeError: 'function' object has no attribute 'upper'

# list casting
# only types that are iterable/subscriptable can be list cast
print(list((1, 2)))
print(list('hello'))
print(list({1: 2, 3: 4, 5: 6}))  # this gives us only the keys [1, 3, 5]
print(list({1, 2, 3, 2, 2, 2, 6}))
