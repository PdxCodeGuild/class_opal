# Lab 7 - ROT Cipher, Version 1

# ROT13_dict = {
#     'a': 'n',
#     'b': 'o',
#     'c': 'p',
#     'd': 'q',
#     'e': 'r',
#     'f': 's',
#     'g': 't',
#     'h': 'u',
#     'i': 'v',
#     'j': 'w',
#     'k': 'x',
#     'l': 'y',
#     'm': 'z',
#     'n': 'a',
#     'o': 'b',
#     'p': 'c',
#     'q': 'd',
#     'r': 'e',
#     's': 'f',
#     't': 'g',
#     'u': 'h',
#     'v': 'i',
#     'w': 'j',
#     'x': 'k',
#     'y': 'l',
#     'z': 'm',
#     ' ': ' '
#     }

# user_input = input("Please enter your message for cipher output: ")
# output_string = []

# for character in user_input.lower():
#     if character in ROT13_dict:
#         output_string += ROT13_dict[character]
#     else:
#         output_string += character

# output = ''.join([character for character in output_string])
# print(output)


# Lab 7 - ROT Cipher, Version 2

from string import ascii_lowercase as alphabet, punctuation as punc

user_input = input("Please enter your message for cipher output: ")
user_rot = int(input("Please enter rotation value (0 - 25): "))

# Creates a function that returns user input with choice of encryption rotation and includes punctuation/spacing as entered by user  
def rotation(input, rot_choice):
    output = ''
    for letter in input.lower():
        if letter == ' ':
            output += letter
        elif letter in punc:
            output += letter
        else:
            choices = len(alphabet)
            rotation = (alphabet.index(letter) + rot_choice) % choices
            output_string = alphabet[rotation]
            output += output_string

    return output
        
        
print(rotation(user_input, user_rot))