import os
import sys

types = ["""
 ____ 
|     |
|     
|    
|
|_______
""", """
 ____ 
|     |
|     O
|    
|
|_______
""", """
 ____ 
|     |
|     O
|     |
|
|_______
""", """
 ____ 
|     |
|     O
|    /|
|
|_______
""", """
 ____ 
|     |
|     O
|    /|\\
|
|_______
""", """
 ____ 
|     |
|     O
|    /|\\
|    / 
|_______
""", """
 ____ 
|     |
|     O
|    /|\\
|    / \\
|_______
"""]

turn = 1

print('Welcome to scramble hangman.')
word_to_guess = input('Input the guessing word or type 1 for random word: ')
if word_to_guess == '1':
    # TODO make random word generator
    word_to_guess = 'monkeys'
guessed_letters = ["_"] * len(word_to_guess)
correctly_guessed_letters = []

while "_" in guessed_letters:
    guess = input("Guess a letter: ")
    if len(guess) > 1:
        print('You may only guess one letter at a time.')
        sys.exit()
    if guess in word_to_guess:
        for i in range(len(word_to_guess)):
            if word_to_guess[i] == guess:
                correctly_guessed_letters.append(guess)
                print('Correctly guessed letters: ' + ''.join(correctly_guessed_letters))
    else:
        turn = turn + 1
        if turn == 6:
            print(types[6])
            print('You guessed wrong to many times!')
            sys.exit()
        else:
            print(types[turn])
            print("Incorrect guess.")
        os.system('cls')

print("Congratulations! You guessed the word:", "".join(guessed_letters))
