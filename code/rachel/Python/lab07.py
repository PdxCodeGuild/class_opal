#Compute Automated Readability Index
# Save a text file containing the Gettysburg Address (copied from internet); copy just text into a .txt file
# Open the file in python
# Seperate the file into a few different lists:
    # Characters
    # Words
    # Sentences (find & count periods)
# Compute the ARI using the formula in the lab instructions
# Copy dicitonary into code and compare ARI output against it
# Print output message

filename = 'gettysburg.txt'

with open(filename) as gettysburg_file:
    lines = gettysburg_file.readlines()

def lines_of_text():
    for line in lines:
        text_string = line.rstrip()
    return text_string

def words():
    total_words = 0
    for line in lines:
        #text_string = line.rstrip()
        words = line.split()
        word_count = len(words) 
        total_words += word_count
    return total_words

def letter():
    letter_count = 0
    text_string = lines_of_text()
    for char in text_string:
        if char.isalpha():
            letter_count += 1
    return letter_count

def sentence():
    total_sentences = 0
    for line in lines:
        #text_string = line.rstrip()
        sentences = line.split(". ")
        sentence_count = len(sentences)
        total_sentences += sentence_count
    return total_sentences

# print(words())
# print(letter())
# print(sentence())

def ARI():
    total_words = words()
    letter_count = letter()
    total_sentences = sentence()
    char_words = (letter_count / total_words) * 4.71
    word_sent = (total_words / total_sentences) * 0.5
    final_number = (char_words + word_sent) -21.43
    round_number = round(final_number)
    return round_number

# print(ARI())

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

ARI_grade = ari_scale[ARI()].get('grade_level')
ARI_age = ari_scale[ARI()].get('ages')
# print(ARI_level)

print(f'The ARI for the gettysburg address is {ARI()}.')
#print(f'This corresponds to a {ari_scale[ARI()].get('grade_level')}level of diffitculty') >> can this be turned into one line so that the variables "ÄRI_grade" and "ARI_age" are needed?
print(f'This corresponds to a {ARI_grade} level of diffitculty that is suitable for an average person {ARI_age} years old.')

