from string import ascii_lowercase

alphabet = list(ascii_lowercase)

user_input = input("Please enter your key here: ").lower()
user_rotate = int(input("Please enter your rotation amount: "))

rotated_letters = []
for i in range(len(alphabet)):
    rotated_letters.append(alphabet[(i + user_rotate) % 21])

encoded_letters = []
for i in range(len(user_input)):
    encoded_letters.append(rotated_letters[alphabet.index(user_input[i])])

encoded_message = ''.join(encoded_letters)
print(encoded_message)