# Take a bit from password generator

import random
import string

def convert_url(length):
    '''
    Converts given url to string of five random letters 
    '''
    # Combination of lower and upper case letters and numbers
    characters = string.ascii_letters + string.digits
    # Join all those characters together!
    new_url = ''.join(random.choice(characters) for i in range(length))
    return new_url