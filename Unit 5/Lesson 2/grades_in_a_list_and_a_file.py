import random

first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")
filename = input("Enter the name for the file: ")

grades = [random.randint(1, 100) for _ in range(5)]

print("\nHere are your randomly-selected grades (hope you pass):")
for i, grade in enumerate(grades, 1):
    print(f"Grade {i}: {grade}")

with open(filename, 'w') as file:
    file.write(f"{first_name} {last_name}\n")
    file.write(' '.join(map(str, grades)) + '\n')

print(f"\nData saved in \"{filename}\".")
