
def number_of_sentences():
    # with open('code/lizzie/python/lab09_files/The_Great_Gatsby.txt', 'r') as file:
    #     contents = file.read()
    contents = "This is for testing my code. It's so scrumptious!"
    num_of_sentences = int(0)
    for character in contents:
        #splitting on punctuation to get number of sentences
        if character in ['.', '?', '!']:
            num_of_sentences += 1
    return num_of_sentences


def number_of_words():
    # with open('code/lizzie/python/lab09_files/The_Great_Gatsby.txt', 'r') as file:
    #     contents = file.read()
    contents = "This is for testing my code. It's so scrumptious!"
    num_of_words = int(0)
    #splitting on empty space to determine how many words there are.
    words = contents.split()
    num_of_words = len(words)
    return num_of_words
# print(number_of_words())


def number_of_characters():
    # with open('code/lizzie/python/lab09_files/The_Great_Gatsby.txt', 'r') as file:
    #     contents = file.read()
    contents = "This is for testing my code. It's so scrumptious!"
    num_of_characters = int(0)
    #Making one long string with only the characters and no spaces so len() can return an integer based on that length.
    contents_no_space = contents.replace(" ","")
    num_of_characters += len(contents_no_space)
    return num_of_characters


def calculate_ari():
    '''
    Function that determines the ARI of a given file. Uses the file as an argument
    '''
    numchars = number_of_characters()
    numwords = number_of_words()
    numsentences = number_of_sentences()
    ari = 4.71 * numchars/numwords + 0.5 * numwords/numsentences - 21.43
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

    # return ari, ari_scale, num_of_characters, num_of_words, num_of_sentences
    print(f"""
The ARI for the file is {ari}. \
This corresponds to a(n) {ari_scale[ari]['grade_level']} \
level of difficulty. That is suitable for an average person\
who is {ari_scale[ari]['ages']} years old. In case you were \
# wondering, there are {number_of_characters()} characters, \
# {number_of_words()} words, and {number_of_sentences()} sentences in the file.""")

    return [ari, numwords, numsentences, numchars]

print(calculate_ari())