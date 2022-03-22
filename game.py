# Number Guessing Game

import random

# initialize number of guesses counter
num_guesses = 0

# start game with question to generate input
print('Hello! What is your name?')

# collect input of player name
player_name = input()

# generate random number
number = random.randint(1, 20)

# ask player for a guess
print('Well, ' + player_name + ', I am thinking of a number between 1 and 20.')

# start while loop to give player 6 chances to guess the number
while num_guesses < 6:

    print('Take a guess.')  # ask for and collect input
    guess = input()
    guess = int(guess)

    num_guesses = num_guesses + 1 # advance number of guesses

    # respond to user input if guess is incorrect or break from loop
    if guess < number:
        print('Your guess is too low.')
    if guess > number:
        print('Your guess is too high.')
    if guess == number:
        break

# congratulate player if they guessed correctly
if guess == number:
    num_guesses = str(num_guesses)
    print('Good job, ' + player_name + '! You guessed my number in ' + num_guesses + ' guesses!')

# console the player if they did not get the correct guess in 6 tries
if guess != number:
    number = str(number)
    print('Nope. The number I was thinking of was ' + number)