import random

number_to_guess = random.randint(1, 10)
number_of_guesses = 0

print("I have chosen a number between 1 and 10. Try to guess it.")

while True:
    guess = int(input("Your guess: "))
    number_of_guesses += 1
    
    if guess == number_to_guess:
        print(f"That's right! You're a good guesser.")
        print(f"It only took you {number_of_guesses} tries.")
        break
    else:
        print("That is incorrect. Guess again.")
