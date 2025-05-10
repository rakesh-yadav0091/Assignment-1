# This program is a number guessing game where the user has 5 chances to guess a random number.

import random

# Generate a random number between 1 and 50
secret = random.randint(1, 50)
attempts = 5

print("Guess a number between 1 and 50. you have 5 attempts.")

for i in range(attempts):
    try:
        guess = int(input(f"Attempt {i + 1}: "))

        if guess == secret:
            print("Correct! you guessed the number!")
            break
        elif guess < secret:
            print("Too low.")
        else:
            print("Too high.")

    except ValueError:
        print("Invalid input! Please enter a valid number.")
else:
    print("Game Over! The number was:", secret)