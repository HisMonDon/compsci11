import random

print("HERE COMES THE DICE!")

roll1 = roll2 = 0

while roll1 != roll2:
    roll1 = random.randint(1, 6)
    roll2 = random.randint(1, 6)

    print(f"Roll #1: {roll1}")
    print(f"Roll #2: {roll2}")
    total = roll1 + roll2
    print(f"The total is {total}!\n")
