import random

number_to_guess = random.randint(1, 100)
guess = None
tries = 0
max_tries = 7

print("I'm thinking of a number between 1-100. You have 7 guesses.")

while guess != number_to_guess and tries < max_tries:
    guess = int(input(f"Guess #{tries + 1}: "))
    tries += 1

    if guess < number_to_guess:
        print("Sorry, you are too low.")
    elif guess > number_to_guess:
        print("Sorry, that guess is too high.")
    else:
        print("You guessed it! What are the odds?!?")

if guess != number_to_guess:
    print("Sorry, you didn't guess it in 7 tries. You lose.")
