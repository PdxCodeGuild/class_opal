# Lab 7: ROT Cipher

# input_dict = {
#     0: 'a',
#     1: 'b',
#     2: 'c',
#     3: 'd',
#     4: 'e',
#     5: 'f',
#     6: 'g',
#     7: 'h',
#     8: 'i',
#     9: 'j',
#     10: 'k',
#     11: 'l',
#     12: 'm',
#     13: 'n',
#     14: 'o',
#     15: 'p',
#     16: 'q',
#     17: 'r',
#     18: 's',
#     19: 't',
#     20: 'u',
#     21: 'v',
#     22: 'w',
#     23: 'x',
#     24: 'y',
#     25: 'z'
# }

ROT13_dict = {
    'a': 'n',
    'b': 'o',
    'c': 'p',
    'd': 'q',
    'e': 'r',
    'f': 's',
    'g': 't',
    'h': 'u',
    'i': 'v',
    'j': 'w',
    'k': 'x',
    'l': 'y',
    'm': 'z',
    'n': 'a',
    'o': 'b',
    'p': 'c',
    'q': 'd',
    'r': 'e',
    's': 'f',
    't': 'g',
    'u': 'h',
    'v': 'i',
    'w': 'j',
    'x': 'k',
    'y': 'l',
    'z': 'm',
    ' ': ' '
    }

user_input = input("Please enter your message for cipher output: ")
output_string = []

for character in user_input.lower():
    if character in ROT13_dict:
        output_string += ROT13_dict[character]
    else:
        output_string += character

output = ''.join([character for character in output_string])
print(output)


# Index	    0	1	2	3	4	5	6	7	8	9	10	11	12	13	14	15	16	17	18	19	20	21	22	23	24	25
# English	a	b	c	d	e	f	g	h	i	j	k	l	m	n	o	p	q	r	s	t	u	v	w	x	y	z
# ROT+13	n	o	p	q	r	s	t	u	v	w	x	y	z	a	b	c	d	e	f	g	h	i	j	k	l	m


# Version 2
# Allow the user to input the amount of rotation used in the encryption / decryption.

# Git Add, Commit & Push:
# > git add files-to-be-added
# > git commit -m "your commit message goes here"
# > git push -u origin your_name-python-lab7
# Then go to the repository to create a PR.