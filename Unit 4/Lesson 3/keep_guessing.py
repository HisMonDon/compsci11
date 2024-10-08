import random

# The number to guess
number_to_guess = random.randint(1, 10)
guess = None

print("I have chosen a number between 1 and 10. Try to guess it.")

# Keep guessing until the correct number is guessed
while guess != number_to_guess:
    guess = int(input("Your guess: "))

    if guess < number_to_guess:
        print("That is incorrect. Guess again.")
    elif guess > number_to_guess:
        print("That is incorrect. Guess again.")
    else:
        print("That's right! You're a good guesser.")
