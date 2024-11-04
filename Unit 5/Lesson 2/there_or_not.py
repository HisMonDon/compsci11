import random

values = [random.randint(1, 50) for _ in range(10)]

print("List:", ' '.join(map(str, values)))

value_to_find = int(input("Value to find: "))

found = False
for value in values:
    if value == value_to_find:
        found = True
        print(f"{value_to_find} is in the list.")

if not found:
    print(f"{value_to_find} is not in the list.")
