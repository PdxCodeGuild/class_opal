'''
In the data folder, you'll find english.txt which contains a list of several thousand english words. Write a function load_words(path) which reads the text from this file and return a list of strings which are greater than 5 letters.

Randomly pick a word from that list and begin the game. Allow the user 10 tries to guess the letters of the word. Keep track of the letters the user has already guessed.

Show them a list of 'blanks' and ask them for a letter.

If they guess a letter which is in the word, show the blanks with the letters filled in.
If they guess a letter which is not in the word, tell them and subtract 1 from their remaining guesses.
If they guess a letter they've guessed before, tell them and do not subtract 1 from their guesses.

Be kind, if the user can't guess the word in the number of allotted guesses, print the word and ask them if they'd like to play again
'''
import lab10_art
from random import choice


path = 'class_opal/1 Python/data/english.txt'


def load_words(path):
    game_words = []

    with open(path, "r") as f:
        words = f.read()

    game_words = words.split('\n')
    # print(game_words)
    for word in game_words:
        if len(word) <= 5:
            game_words.remove(word)
    return game_words


def game_word(words):
    return choice(words)

def hangman():
    print(lab10_art.logo)
    word = game_word(load_words(path))
    # print(word)
    tries = 7
    letters_guessed = []
    correct_letters = list('_' * len(word))
    while tries:
        if '_' not in correct_letters:
            print("You win!")
            break
        if tries < 7:
            print(lab10_art.stages[tries])
        print(''.join(correct_letters))
        print("Letters guessed: ", " ".join(letters_guessed))
        user_input = input("Enter a letter: ").lower()
        if user_input in letters_guessed:
            print("You've already guessed this letter!")
            continue
        elif user_input in word:
            for i, letter in enumerate(word):
                if letter == user_input:
                    correct_letters[i] = letter
        else:
            tries -= 1
        letters_guessed += user_input
    if tries == 0:
        print("You suck. Womp womp.")
    again = input("Would you like to play again? Enter yes or no: ")
    if again == 'yes':
        hangman()

hangman()
        
