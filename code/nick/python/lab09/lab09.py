import string
from math import ceil


def title(path):
    '''
    extracts title of a file in title case
    '''
    # extract name of book to be analyzed for later use
    path_list = path.split('/')
    path_list = path_list[-1].split('.')
    book_name = path_list[0].replace('_', ' ').title()
    return book_name


def sentence_counter(book):
    '''
    counts sentences in book
    '''
    # end all sentences in a period for simplicity
    sentence_end = ['!', '?']
    for punc in sentence_end:
        if punc in book:
            book = book.replace(punc, '.')

    # count sentences
    list_of_sentences = book.split('.')
    if '' in list_of_sentences:
        list_of_sentences.remove('')
    number_of_sentences = len(list_of_sentences)
    return number_of_sentences


def word_counter(book):
    '''
    counts words in a book
    '''
    # count words
    list_of_words = book.split(' ')
    number_of_words = len(list_of_words)
    return number_of_words


def char_counter(book):
    '''
    counts letter and number characters in a book
    '''
    # isolate letter characters
    for punc in string.punctuation:
        book = book.replace(punc, '')

    for white in string.whitespace:
        book = book.replace(white, '')

    number_of_characters = len(book)
    return number_of_characters


def ari_calculator(book):
    sentences = sentence_counter(book)
    words = word_counter(book)
    characters = char_counter(book)
    ari_score = ceil(4.71*(characters/words) + .5 * (words/sentences) - 21.43)
    if ari_score > 14:
        ari_score = 14
    return ari_score


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

# file name MUST use underscores as separators
relative_path = 'code/nick/python/lab09/myth_of_sisyphus.txt'

if __name__ == '__main__':
    with open(relative_path) as file:
        book = file.read()
    ari = ari_calculator(book)

    print(f'''
    The ARI for {title(relative_path)} is {ari}.
    This corresponds to a {ari_scale[ari]['grade_level']} level of difficulty
    that is suitable for an average person {ari_scale[ari]['ages']} years old.
    ''')
