print("I will add up the numbers you give me.")

total = 0
number = None

while number != 0:
    number = int(input("Number: "))
    total += number
    if number != 0:
        print(f"The total so far is {total}")

print(f"The total is {total}")
