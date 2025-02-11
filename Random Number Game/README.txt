
# Random Number Game

This is a simple number guessing game where the user is prompted to guess a random number between 1 and 10. The game will notify you if you win, or shut down your computer if you guess incorrectly!

## Requirements

- Python 3.x

## Installation

To download the game and run it on your system, follow the steps below.

### Windows

1. **Download Python:**
   - If you don't already have Python installed, [download Python from the official website](https://www.python.org/downloads/) and install it. Make sure to check the option to add Python to your system's PATH during installation.

2. **Download the Game Script:**
   - Download the Python script `import_random.py` and save it to a folder on your computer.

3. **Run the Game:**
   - Open the Command Prompt (type `cmd` in the search bar and press Enter).
   - Navigate to the folder where you saved the script using the `cd` command (e.g., `cd C:\path\to\your\folder`).
   - Run the game by typing:
     ```bash
     python import_random.py
     ```

4. **Play the Game:**
   - The game will ask you to guess a number. Enter a number between 1 and 10 to try to win!

### macOS

1. **Download Python:**
   - Python usually comes pre-installed on macOS. If not, you can download and install it from [python.org](https://www.python.org/downloads/).

2. **Download the Game Script:**
   - Download the Python script `import_random.py` and save it to a folder on your computer.

3. **Run the Game:**
   - Open the Terminal application (you can find it in Applications > Utilities).
   - Navigate to the folder where you saved the script using the `cd` command (e.g., `cd /path/to/your/folder`).
   - Run the game by typing:
     ```bash
     python3 import_random.py
     ```

4. **Play the Game:**
   - The game will prompt you to guess a number. Enter a number between 1 and 10 to try to win!

## Features

- **Number Guessing:** Guess the number between 1 and 10.
- **Win Notification:** If you guess correctly, you win!
- **Shutdown Feature:** If you guess incorrectly, your computer will shut down.

## Troubleshooting

- If you encounter errors about Python not being recognized, ensure you have Python installed and added to your PATH.
- If the game closes unexpectedly, check if the Python script is correct and if your system has any restrictions on running commands like `os.system('shutdown')`.
