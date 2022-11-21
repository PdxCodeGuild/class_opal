from string import ascii_letters
import lab07_art

alphabet = ascii_letters.lower()


def caesar(start_text, shift_amount, cipher_direction):
    end_text = ""
    while shift_amount >= 26:
        shift_amount = shift_amount % 26
    if cipher_direction == "decode":
        shift_amount *= -1
    for char in start_text:
        if char in alphabet:
            position = alphabet.index(char)
            new_position = position + shift_amount
            new_char = alphabet[new_position]
        else:
            new_char = char
        end_text += new_char

    # print(f"Here's the {cipher_direction}d result: {end_text}")
    return cipher_direction, end_text


print(lab07_art.logo)

end_program = False
while not end_program:
    valid_choices = ['encode', 'decode']
    while True:
        direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
        if direction in valid_choices:
            break
        else:
            print('This ia an invalid input.')

    text = input("Type your message:\n").lower()
    while True:
        try:
            shift = int(input("Type the shift number:\n"))
            break
        except ValueError:
            print('This ia an invalid input.')

    cipher_direction, end_text = caesar(text, shift, direction)
    print(f'Your {cipher_direction}d message is {end_text}')
    answer = input("Would you like to run the program again? Type yes or no\n")
    if answer == "yes":
        end_program = False
    else:
        break
print("Goodbye")
