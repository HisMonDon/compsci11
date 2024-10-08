
start = int(input("Enter the starting number: "))
end = int(input("Enter the ending number: "))

total = 0

for number in range(start, end + 1):
    if number == 13 or number == 31:
        break
    total += number

print(f"The sum of numbers from {start} to {end}, stopping if 13 or 31 is encountered, is: {total}")
