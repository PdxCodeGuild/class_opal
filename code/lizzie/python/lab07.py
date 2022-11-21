from string import ascii_lowercase

alphabet = list(ascii_lowercase)

user_input:str = input("Please enter a message here: ").lower()
user_rotate = int(input("Please enter your rotation amount: "))

# insert empty string to append translated characters
rotated_letters:list = []

#specify range as length of whole list
for i in range(len(alphabet)):
    #execute number of specified rotations on the alphabet, then append to rotated letters.
    rotated_letters.append(alphabet[(i + user_rotate) % 26])

encoded_letters:list = []
for i in range(len(user_input)):
    #take user's message and encode the letters
    encoded_letters.append(rotated_letters[alphabet.index(user_input[i])])

encoded_message:str = ''.join(encoded_letters)
print(encoded_message)