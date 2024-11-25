"""
Create a function that takes a percent values from 0.0 to 1.0 and converts it to a string from "0%" to "100%". Use the round() function to make it appear with no decimal places.

Create a docstring for this function and write type annotations.

Create a main function that will make use of the percent conversion function.

Raise an exception in your function when it recieves a value outside its defined range (0.0 to 1.0). This is a reasonable check to perform.
"""

def convert_to_percent(value: float) -> str:
    if value > 1.0 or value < 0.0:
        raise ValueError("Value must be between 0 and 1")
    return str(round(value*100))
print(convert_to_percent(0.5))

def main():
    number = float(input("Enter your number (between 0.0 and 1.0): "))
    print(f"Your percentage will be {convert_to_percent(number)}%")
if __name__ == "__main__":
    main()
