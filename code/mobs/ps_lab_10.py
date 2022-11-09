# Let's write a program to play a game of hangman. In the data folder, you'll find english.txt which contains a list of several thousand english words. Write a function load_words(path) which reads the text from this file and return a list of strings which are greater than 5 letters.

# Randomly pick a word from that list and begin the game. Allow the user 10 tries to guess the letters of the word. Keep track of the letters the user has already guessed.

# Show them a list of 'blanks' and ask them for a letter.

# If they guess a letter which is in the word, show the blanks with the letters filled in.
# If they guess a letter which is not in the word, tell them and subtract 1 from their remaining guesses.
# If they guess a letter they've guessed before, tell them and do not subtract 1 from their guesses.
# Be kind, if the user can't guess the word in the remaining_guessesber of allotted guesses, print the word and ask them if they'd like to play again.

# Feel free to customize the user interface, but provide these minimum features. Below is an example run of the program.

# _ _ _ _ _ _ _ _ _
# # of guesses remaining: 10
# already guessed: 

# Guess a letter: a
# _ a _ _ _ _ a _ _
# # of guesses remaining: 10
# already guessed: a

# Guess a letter: a
# You've already guessed that
# _ a _ _ _ _ a _ _
# # of guesses remaining: 10
# already guessed: a

# Guess a letter: k
# _ a _ _ _ _ a _ _
# # of guesses remaining: 9
# already guessed: a, k
# Guess a letter: 
from random import choice

path = '1 Python\data\english.txt'


def load_words(path):
    with open(path, 'r', encoding='utf-8') as file:
        contents = file.read()
    words = contents.split("\n")
    return list(filter(lambda x: x if len(x) > 5 else None, words))


words = load_words(path)
answer = list(choice(words))


def hangman(answer: list):
    remaining_guesses = 10
    display = list('_' * len(answer))
    guesses = []
    while remaining_guesses > 0 :
        guess = input("Guess a letter: ")
        if guess in answer and guess not in guesses:
            for i in range(len(answer)):
                if answer[i] == guess:
                    display[i] = guess
        elif guess in guesses:
            print("You have already guessed this letter.")
        else:
            remaining_guesses -= 1
            print(f"Letter is not in word. You have {remaining_guesses} remaining guesses.")
        guesses.append(guess)
        feedback = ''.join(display)
        print(feedback)
        
        if display == answer:
            print("Congratulations.  You win!!!")
            play_again = input("Would you like to play again (y or n)? ")
            if play_again == 'y':
                answer = list(choice(words))
                hangman(answer)
            else:
                print("Goodbye.")
                break
           
        if remaining_guesses == 0:
            print(f"You have run out of guesses.  The word was {''.join(answer)}.")
            play_again = input("Would you like to play again (y or n)? ")
            if play_again == 'y':
                answer = list(choice(words))
                hangman(answer)
            else:
                print("Goodbye.")
                break


hangman(answer)
