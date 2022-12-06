'''
Programing languages are either interpreted or compiled
Python is both
'''

'''Compilation Errors (thrown by the compiler)'''
'''SyntaxError'''

# print('hello) #SyntaxError: unterminated string literal

# print('hello' #SyntaxError: '(' was never closed

# 1.upper() #SyntaxError: invalid decimal literal

'''IndentationError'''
# IndentationError: expected an indented block
# def hello():
#     print('hello')
#     # inside the function
# # outside the function


'''Runtime Errors (thrown by the interpreter'''

'''NameError'''
# print(hello) #NameError: name 'hello' is not defined.


'''AttribueError'''
import math
blue = 'blue'
colors = ['red']
colors.append(blue)
# blue.append(colors) #AttributeError: 'str' object has no attribute 'append'

'''TypeError'''
# print(1 + '1')  # TypeError: unsupported operand type(s) for +: 'int' and 'str'

# {1, 2, 1}[1] #TypeError: 'set' object is not subscriptable

# len(123) #TypeError: object of type 'int' has no len()


def hello(name):
    print('hello ' + name)


# hello()  # TypeError: hello() missing 1 required positional argument: 'name'

'''IndexError'''

# colors[2]  # IndexError: list index out of range

# print(colors)

'''side tangent about range'''
# for i in range(20, 40, 5):
#     print(i)

# for i in range(len(colors)):
#     print(colors[i])


'''KeyError'''
staff = {
    'instructor': 'Danny',
    'TA': 'Gage'
}

print(staff['TA'])
# print(staff['chef']) #KeyError: 'chef'
print(staff.get('HR'))

'''ValueError'''
# print(int('beans'))  # ValueError: invalid literal for int() with base 10: 'beans'
# print(math.sqrt(-1)) #ValueError: math domain error


'''UnboundLocalError'''
counter = 0


def show_count():
    print(counter)
    # counter += 1


show_count()  # UnboundLocalError: local variable 'counter' referenced before assignment

'''RecursionError'''


def break_python():
    print('wheeee!')
    break_python()


break_python()  # RecursionError: maximum recursion depth exceeded


'''Raising errors'''

# for i in range(20):
#     if i is 13:
#         raise ValueError('this number is unlucky')
#     print(i)


'''Catching errors'''

for i in range(20):
    try:
        if i is 7:
            raise TypeError('my religion says 7 is not a real number')
        if i is 13:
            raise ValueError('oops!')
        print(i)
    except ValueError as e:
        print(e)
    except:
        print('something went wrong')
