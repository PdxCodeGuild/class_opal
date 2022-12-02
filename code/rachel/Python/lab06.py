#ROT Cipher
#ask the user to input a string of characters
#create an index to encrypt / decrypt input
    #make a list of each character & add 13 to index (since there are 26 letters, encryption is same as decryption)
            #use print(input[#]) to get a character at a certain index (see Strings doc)
            #create def so that all the returned letters can be printed out together
        # for every inputted letter from string, add 13 and output that letter
    # make a loop that goes thru every element in the string:
        # while i in input_string != 0, do this
    # make a loop that ensures index / numbers do not go over 26
        # if i > 26, loop back to beginning of index

keys = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
input_phrase = input("Enter a string of letters to encypher: ")

def index_value():
    position1 = keys.index(i)
    return position1


working_string = ""
for i in input_phrase:
    position1 = index_value()
    if position1 >= 13:
        position2 = position1 - 13
        new_letter = keys[position2]
    else:
        positition2 = position1 + 13 
        new_letter = keys[positition2]
    working_string += new_letter

print(working_string)


 
