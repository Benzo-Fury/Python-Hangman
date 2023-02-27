import os
import sys
import random

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
    word_to_guess = random.choice(['monkeys', 'chicken', 'banana', 'jazz'])
guessed_letters = ["_"] * len(word_to_guess)
correctly_guessed_letters = []

while "_" in guessed_letters:
    guess = input("Guess a letter: ")
    if len(guess) != 1:  # fixed the if statement
        print('You may only guess one letter at a time.')
        sys.exit()
    if guess in correctly_guessed_letters:
        print('You have already guessed this letter.')
        continue  # continue the while loop if letter was already guessed
    if guess in word_to_guess:
        correctly_guessed_letters.append(guess)
        for i in range(len(word_to_guess)):
            if word_to_guess[i] == guess:
                guessed_letters[i] = guess
        print(types[turn])
        print('Correct guess.')
        print('Correctly guessed letters: ' + ''.join(correctly_guessed_letters))
    else:
        turn = turn + 1
        if turn == 6:
            print(types[6])
            print('You guessed wrong too many times!')
            sys.exit()
        else:
            print(types[turn])
            print("Incorrect guess.")
            print('Correctly guessed letters: ' + ''.join(correctly_guessed_letters))
    os.system('cls')  # clear the screen after each guess

print("Congratulations! You guessed the word:", "".join(guessed_letters))
