import random
secret_number = random.randint(1, 50)
max_attempts = 6
guess_try = 0
win = False
while guess_try < max_attempts:

    guess = int(input("Guess a number between 1 and 50: "))

    if guess < 1 or guess > 50:
        print("Please enter a valid guess between 1 and 50.")

    elif guess > secret_number:
        print("Your guess is higher than the secret number.")
        guess_try = guess_try + 1

    elif guess == secret_number:
        print("Congratulations! You guessed it right!")
        guess_try = guess_try + 1
        win = True
        print("You did it in:", guess_try, "attempts")
        break

    elif guess < secret_number:
        print("Your guess is lower than the secret number.")
        guess_try = guess_try + 1

if win == False:
    print("Game Over!")
    print("You used all", max_attempts, "attempts.")
    print("The secret number was:", secret_number)