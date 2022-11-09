from string import ascii_lowercase

letters = list(ascii_lowercase)

user_string = input("Enter a string: ")
rotation = int(input("Enter a rotation amount: "))

letters_rot = []
for i in range(len(letters)):
     letters_rot.append(letters[(i + rotation) % 26])

encoded_list = []
for i in range(len(user_string)):
    encoded_list.append(letters_rot[letters.index(user_string[i])])

encoded_string = ''.join(encoded_list)

print(encoded_string)