from string import ascii_lowercase

letters = list(ascii_lowercase)

letters_rot13 = []

for i in range(len(letters)):
     letters_rot13.append(letters[(i + 13) % 26])

user_string = input("Enter a string: ")

encoded_list = []
for i in range(len(user_string)):
    encoded_list.append(letters_rot13[letters.index(user_string[i])])

encoded_string = ''.join(encoded_list)

print(encoded_string)