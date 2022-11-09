relative_path = 'code/lizzie/python/lab09_files/The_Great_Gatsby.txt'

with open(relative_path, 'r') as file:
    contents = file.read()

#defining empty variables so we can assign ints to them later.
num_of_sentences = 0
num_of_characters = 0

for character in contents:
    #splitting on punctuation to get number of sentences
    if character in ['.', '?', '!']:
        num_of_sentences += 1

#splitting on empty space to determine how many words there are.
words = contents.split()
num_of_words = len(words)

#Making one long string with only the characters and no spaces so len() can return an integer based on that length.
contents_no_space = contents.replace(" ","")
num_of_characters += len(contents_no_space)

ari = 4.71 * (num_of_characters/num_of_words) + 0.5 * (num_of_words/num_of_sentences) - 21.43
#Must round the int of the ari so it's possible to use it to access keys in the dictionary.
ari = round(ari)

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


print(f"""
The ARI for the file is {ari}.
This corresponds to a(n) {ari_scale[ari]['grade_level']} level of difficulty.
That is suitable for an average person who is {ari_scale[ari]['ages']} years old.
In case you were wondering, there are {num_of_characters} characters, {num_of_words} words, and {num_of_sentences} sentences in the file.
""")