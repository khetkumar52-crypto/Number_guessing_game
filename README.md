# 🎯 Number Guessing Game

A beginner-friendly Python command-line game where the computer generates a secret number and the player tries to guess it within a limited number of attempts.

## Features

* 🎲 Random secret number generation
* 🔢 Number range from 1–50
* ✅ Input validation
* ⬆️ Higher/lower hints
* 🔁 Repeated guessing using a `while` loop
* 🔢 Attempt counter
* ⏳ Maximum of 6 attempts
* 🏆 Win detection
* 💀 Game Over system
* 🔐 Reveals the secret number if all attempts are used

## Python Concepts Used

* `print()`
* `input()`
* Variables
* `int()`
* Arithmetic operators
* Comparison operators
* `if / elif / else`
* `while` loops
* `break`
* Boolean variables
* `import`
* Python's `random` module
* `random.randint()`

## How the Game Works

1. The computer randomly chooses a number between 1 and 50.
2. The player enters a guess.
3. The program checks whether the guess is valid.
4. If the guess is too high or too low, the program gives a hint.
5. Each valid guess counts as one attempt.
6. The player has a maximum of 6 attempts.
7. The game ends when the player guesses correctly or runs out of attempts.

## Example

```text
Guess a number between 1 and 50: 25
Your guess is lower than the secret number.

Guess a number between 1 and 50: 40
Your guess is higher than the secret number.

Guess a number between 1 and 50: 34
Congratulations! You guessed it right!
You did it in: 3 attempts
```

## How to Run

Make sure Python 3 is installed, then run:

```bash
python number_guessing_game.py
```

## What I Practiced

This project helped me practice combining variables, conditions, loops, user input, random number generation, and program state into one complete interactive Python program.
