import random

# Create a list with ten random values from 1-50
values = [random.randint(1, 50) for _ in range(10)]

# Display the list
print("List:", ' '.join(map(str, values)))

# Prompt the user for an integer
value_to_find = int(input("Value to find: "))

# Search through the list manually
for value in values:
    if value == value_to_find:
        print(f"{value_to_find} is in the list.")
