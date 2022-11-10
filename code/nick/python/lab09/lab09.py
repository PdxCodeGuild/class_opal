import string
from math import ceil
ari_scale = {
     1: {'ages':   '5-6', 'grade_level': 'Kindergarten'},
     2: {'ages':   '6-7', 'grade_level':    '1st Grade'},
     3: {'ages':   '7-8', 'grade_level':    '2nd Grade'},
     4: {'ages':   '8-9', 'grade_level':    '3rd Grade'},
     5: {'ages':  '9-10', 'grade_level':    '4th Grade'},
     6: {'ages': '10-11', 'grade_level':    '5th Grade'},
     7: {'ages': '11-12', 'grade_level':    '6th Grade'},
     8: {'ages': '12-13', 'grade_level':    '7th Grade'},
     9: {'ages': '13-14', 'grade_level':    '8th Grade'},
    10: {'ages': '14-15', 'grade_level':    '9th Grade'},
    11: {'ages': '15-16', 'grade_level':   '10th Grade'},
    12: {'ages': '16-17', 'grade_level':   '11th Grade'},
    13: {'ages': '17-18', 'grade_level':   '12th Grade'},
    14: {'ages': '18-22', 'grade_level':      'College'}
}

relative_path = 'class_opal/code/nick/python/lab09/myth_of_sisyphus.txt'
# extract name of book to be analyzed for later use
path_list = relative_path.split('/')
path_list = path_list[-1].split('.')
book_name = path_list[0].replace('_', ' ').title()

with open(relative_path) as file:
    book = file.read()

# print(book) #test

# end all sentences in a period for simplicity
sentence_end = ['!', '?']
for p in sentence_end:
    if p in book:
        book = book.replace(p, '.')

#count sentences
list_of_sentences = book.split('.')
number_of_sentences = len(list_of_sentences)
# print(number_of_sentences) #test

#count words
list_of_words = book.split(' ')
number_of_words = len(list_of_words)
# print(number_of_words) #test

#isolate letter characters
book_without_punctuation = '' 
for punc in string.punctuation:
    book = book.replace(punc, '')
# print(book) # test

for white in string.whitespace:
    book = book.replace(white, '')
# print(book) #

number_of_characters = len(book)
# print(number_of_characters) #test

ari_score = ceil(4.71*(number_of_characters/number_of_words) + .5*(number_of_words/number_of_sentences) - 21.43)
if ari_score > 14:
    ari_score = 14

print(f'''
The ARI for {book_name} is {ari_score}.
This corresponds to a {ari_scale[9]['grade_level']} level of difficulty
that is suitable for an average person {ari_scale[9]['ages']} years old.
''')
