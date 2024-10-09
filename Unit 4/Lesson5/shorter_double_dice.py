import random

print("HERE COMES THE DICE!")

roll_number = 1
while True:
    roll1 = random.randint(1, 6)
    roll2 = random.randint(1, 6)
    total = roll1 + roll2
    
    print(f"\nRoll #{roll_number}: {roll1}")
    print(f"Roll #{roll_number + 1}: {roll2}")
    print(f"The total is {total}!")
    
    if roll1 == roll2:
        break
    
    roll_number += 2
