import math

print("SQUARE ROOT!")
while True:
    number = float(input("Enter a number: "))
    if number < 0:
        print("You can't take the square root of a negative number, silly.")
        continue
    else:
        sqrt_number = math.sqrt(number)
        print(f"The square root of {number} is {sqrt_number}.")
        break
