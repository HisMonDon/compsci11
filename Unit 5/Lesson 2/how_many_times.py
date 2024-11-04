import random

values = [random.randint(1, 50) for _ in range(10)]

print("List:", ' '.join(map(str, values)))

value_to_find = int(input("Value to find: "))

count = 0
for value in values:
    if value == value_to_find:
        count += 1

print(f"{value_to_find} was found {count} times.")
