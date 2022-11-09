"""
The score is computed by multiplying the number of characters 
divided by the number of words by 4.71, adding the number of words 
divided by the number of sentences multiplied by 0.5, and 
subtracting 21.43. If the result is a decimal, always round up. 
Scores greater than 14 should be presented as having the same age 
and grade level as scores of 14.
"""
import math
relative_path = 'code\leslie\python\christmas_carol.txt'

with open('christmas_carol.txt', 'r', encoding = 'utf-8') as file:
    contents = file.read()
    words = contents.split() #Splits into words
    chars = contents.replace(' ', '') #reads content and replaces spaces with NO spaces to get accurate character count
    sentences = contents.split('.') #splits at periods

word_count = len(words)
print("Number of words: ", word_count)

char_count = len(chars)
print("Number of characters: ", char_count)

sentence_count = len(sentences)
print("Number of sentences: ", sentence_count)

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


def find_ari(char_count, word_count, sentence_count):
    ari_num = math.ceil(((char_count/word_count) * 4.71) + ((word_count/sentence_count) * 0.5) -21.43)
    print(ari_num)

    if ari_num == 1:
        age = ari_scale['1']['ages']
        grade_level = ari_scale['1']['grade_level']
    elif ari_num == 2:
        age = ari_scale[2]['ages']
        grade_level = ari_scale[2]['grade_level']
    elif ari_num == 3:
        age = ari_scale[3]['ages']
        grade_level = ari_scale[3]['grade_level']
    elif ari_num == 4:
        age = ari_scale[4]['ages']
        grade_level = ari_scale[4]['grade_level']
    elif ari_num == 5:
        age = ari_scale[5]['ages']
        grade_level = ari_scale[5]['grade_level']
    elif ari_num == 6:
        age = ari_scale[6]['ages']
        grade_level = ari_scale[6]['grade_level']
    elif ari_num == 7:
        age = ari_scale[7]['ages']
        grade_level = ari_scale[7]['grade_level']
    elif ari_num == 8:
        age = ari_scale[8]['ages']
        grade_level = ari_scale[8]['grade_level']
    elif ari_num == 9:
        age = ari_scale[9]['ages']
        grade_level = ari_scale[9]['grade_level']
    elif ari_num == 10:
        age = ari_scale[10]['ages']
        grade_level = ari_scale[10]['grade_level']
    elif ari_num == 11:
        age = ari_scale[11]['ages']
        grade_level = ari_scale[11]['grade_level']
    elif ari_num == 12:
        age = ari_scale[12]['ages']
        grade_level = ari_scale[12]['grade_level']

    print(f"""
    The ARI of 'A Christmas Carol' is {ari_num}.
    This corresponds to a(n) {grade_level} level of difficulty
    that is suitable for an average person {age} years old.
    """) 
find_ari(char_count, word_count, sentence_count)