import string
import random
from .models import Shortened

# code generator to generate a unique
def code_generator():
    # length of code 
    length = 6

    # the charaters to use here we have uppercase and digits 0-9
    characters = string.ascii_uppercase + string.digits

    # 6 digit code generated 
    code =  ''.join(random.choice(characters) for _ in range(length))

    # check if this code already exists in our database
    if Shortened.objects.filter(code=code).exists():
        
        # generate another code
        return code_generator()
    
    return code