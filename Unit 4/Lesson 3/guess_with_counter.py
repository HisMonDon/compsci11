import random

number_to_guess = random.randint(1, 10)
guess = None
tries = 0

print("I have chosen a number between 1 and 10. Try to guess it.")

while guess != number_to_guess:
    guess = int(input("Your guess: "))
    tries += 1

    if guess < number_to_guess:
        print("That is incorrect. Guess again.")
    elif guess > number_to_guess:
        print("That is incorrect. Guess again.")
    else:
        print("That's right! You're a good guesser.")
        print(f"It only took you {tries} tries.")
