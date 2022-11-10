'''Escape Characters'''

s_literal = 'this "is" a string'
s_literal = "this 'is' a string"
# escape quotes using a backslash
s_literal = 'this quote has "multiple" \'quote\' types'

multi_line_string = f"""
this string

        preserves white space

        and ' you can " use
        any quote marks inside it
        {10 * 3}

"""
# print(multi_line_string)


'''Escaped whitespace characters'''
# \n for new line
# \t for tab
# print('\t Welcome to Class Opal \n\n It\'s nice in here')


'''Raw string'''
raw_string = r'\n\n\tthis is now \'a raw string\t'
# print(raw_string)

'''Unicode characters'''

print('\u1234') # ሴ
print('\u0123') # ģ
print('\u1998') # ᦘ
print('\u1997') # ᦘ
print('\u9999') # ᦘ
print('"\u0001"') # ""

'''ASCII codes'''
# ord() takes in a one-character string and returns its ascii code
print(ord('A')) #65
print(ord('B')) #66
print(ord('a')) #97

print(chr(67))

# for i in range(200):
#     print(f'ASCII code {i}: {chr(i)}')


'''Concatenation
use the + operator to combine strings'''

message = '\nhello' + ' ' + '\"world"'
print(message)
print(len(message))


'''String methods
.upper()
.lower()
.capitalize() just the first char
.title() capitalize the first char after every whitespace
'''

# .find(substring) returns the index of the beginning of a substring
print(message.find('world')) #6 
print(message.find('w')) #6
print(message.find('l')) #2

print(id(message))

'''Split and Join'''
# .split(separator) returns a list of substrings separated by the given separator
sentence = 'Danny has a new donkey painting'

# splits on and removes whitespace by default
print(sentence.split())
# you can split on any substring
print(sentence.split('a'))
# if you use a separator that is not present, it will return the whole string in a list
print(sentence.split('x'))


words = sentence.split()

for i in range(len(words)):
    if words[i] == 'donkey':
        words[i] = words[i].upper()
    else: 
        words[i] = words[i].capitalize()
print(words)


# .join(iterable) returns a string with the items from the iterable
# joined by the string that the method is called on

# print(words.join('-')) # AttributeError: 'list' object has no attribute 'join'
print('-'.join(words))


silly_string = "! ! ! ! !"
exclamation_points = silly_string.split(' ')
print(exclamation_points)

new_string = '$'.join(exclamation_points)
print(new_string)


'''Strip
removes all of a given character (or set of characters)
from the beginning and end of a string
'''

message = '---!--!---hello--!--world-----!-!-!---------------'
print(message.strip('-'))
print(message.strip('-!'))

long_message = '''


        this is a long message


        with other stuff in it


'''

print(message.strip('-'))
print(message.lstrip('-')) 
print(message.rstrip('-'))

'''Replace
finds every incidence of a substring and replaces it
'''

replaced = message.replace('-', '@') # @@@@@@@@hello@@@@world@@@@@@@@@@@@@@@@@@@@@@
replaced = message.replace('-', '') # helloworld

print(replaced)


'''String library'''

import string

print(string.ascii_letters)
print(string.hexdigits)
print(string.punctuation)
print(string.whitespace)

message = ')(*&^%$^%$%^&here is the message*#&#*%(@$%^'
print(message.strip(string.punctuation))
