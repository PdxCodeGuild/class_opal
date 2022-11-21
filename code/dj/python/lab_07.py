from string import ascii_lowercase


words = []
encrypt = input(f"What would you like to encrypt?: ").lower()
rotation = input(f"Enter rotation amount: ")
rotation = int(rotation)

for letter in encrypt:
    if letter not in ascii_lowercase:
        words.append(letter)
    else:
        index = ascii_lowercase.index(letter) + rotation
        print(index)
        if index >= 26:
            index -= 26
        conv = ascii_lowercase[index]
        words.append(conv)
print("".join(words))
