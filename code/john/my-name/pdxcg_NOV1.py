'''user_input = input('input the number of feet you want converted: ')
user_input = float(user_input)
result = user_input*(0.3048)

print(result)
'''
'''
Command line: 
ls -a everything includes hidden files 

prompt, command, option, argument


you can extend the command on the command line using quotes

tail shows the most recent part of a process that is currently running

man gives you a manual of what your entering. 

relative path could also start with a ../ which gets me into code guild
'''

# Use keyboard shortcuts 

# actual lesson

# single
'''
multi line comment

''' 

# variable assignment 

'''
variable_name = 'value'
value = variable_name

id(variable_name)

print(id(variable_name))
print(id(value))
'''


'''
variable is a pointer to value. It's not the actual value
You can produce variables w. different names that have the same value. 


'''
# data types

# an_int = 1
# a_string = 'yes'
# a_float = 1.0
# a_boolean = True

# a_list = [1, 2, 3, 'four', [5, 6], {7, 8}]
# a_dict = {1:2, 3:5,
# 'four': 5.6,
# } # they keys can be almost anything their keys 
# # and values can have almost any value yadayadayada
# a_tuple = (1, 2, 3) # They are immutable
# a_set = (1, 2, 3, 1) # They don't have duplicates

# def a_function(): 
#     return 'hello'

# # lITERALS

# msgl = 'this is a literal value'
# # msgl is a literal because it's value is hard coded. 

# msg2 = input('what time is it?')
# # msg2 is not a literal because the value changes. Most things are not literal

# # MUTABILITY 
# '''
# You can reassign a value to any type. 
# '''
# val1 = 1
# val1 = 'one'

# # this does change identity
# value = 1
# print(id(val1))
# val1 = 'one'
# print(id(val1))

# colors =['red', 'green', 'blue']
# colors.append('yellow')
# print(colors)
# the id of the value for this list doesnt change even I added yellow

# the value of the identity changes. 
# lists are mutable but they retain their ID. 


# ordered vs. unordered: lists and tuples are orderd, 
# dict and sets are not ordered
# sometimes dicts are ordered
# print(colors[1])

# dict, you can't have the same key multiple times.

# a_tuple = (1, 2, 3, 7, 0, 4, 5) # They are immutable
# print(a_tuple)

# type coercion

#: int casting- perform the action of changing the type. 

# if you take an int and multiply it by a float, you get a float. 
'''
^This is coercing a type without casting.
'''
'''
this_float = 3 * 1.0
print(type(this_float))
float2 = int(this_float)
print(type(float2))
'''
# You can string cast almost anything. 
# you can even string cast a function

# You can list cast all iterables

# print(list('hello'))
# when you list cast a dict, it only lists keys
# when you list cast a dict you just get the keys. 


# These represent boolean literals 
'''
rain_input = input('is it raining out?: ')
temp_input = input('what is the temp?: ')
is_raining = False
is_cold = False

if rain_input == 'yes' or rain_input == 'y':
    is_raining = True

if int(temp_input) < 60: 
    is_cold = True

if is_cold and is_raining: 
    print('hello sadness')
elif is_cold or is_raining:
    print('meh')
else:
    print('hello sunshine')
'''

# strings are always true

def t_or_f(arg):
    return True

thing = t_or_f()

thing 

