# Chapter10_01
# Hangman Mini Game
# Basic Program Development and Test

import time
import csv
import random
import winsound

# First Greetings
name = input('What is your name? : ')

print('Hi ,'+name, 'Time to play hangman game!')

print()

time.sleep(1)

print('Start Loading...')
print()
time.sleep(0.5)

# CSV Word List
words = []

# Questions CSV File Load
with open('./resource/word_list.csv', 'r') as f:
    reader = csv.reader(f)
    # Header Skip
    next(reader)
    for c in reader:
        words.append(c)

# Mix Lists
random.shuffle(words)
q = random.choice(words)

# Answer
word = q[0].strip()

# Guessing Words
guesses = ''

# Chance
turns = 10

# While Loop
# If Chance count left
while turns > 0:
    # Fail Count
    failed = 0

    # Repeat the correct word
    for char in word:
        # The correct answer contains a guessing character.
        if char in guesses:
            # guess word output
            print(char, end=' ')
        else:
            # Process as _ if incorrect
            print('_', end=' ')
            failed += 1
    # a case of successful word guess
    if failed == 0:
        print()
        print()
        # Win Sound
        winsound.PlaySound('./sound/good.wav', winsound.SND_FILENAME)
        print('Congratulations ! The Guesses is correct')
        # Stop
        break
    print()

    # Enter guessing word character units
    print()
    print('Hint : {}'.format(q[1].strip()))
    guess = input('guess a charater : ')

    # Add words
    guesses += guess

    # The correct word does not contain any guessing characters.
    if guess not in word:
        turns -= 1
        # Error Message
        print('Oops! Wront')
        # Print left Chances
        print('You have', turns, 'more guesses!')

        if turns == 0:
            # Fail Message
            # Fail Sound
            winsound.PlaySound('./sound/bad.wav', winsound.SND_FILENAME)
            print('Your hangman game failed. Bye!')
