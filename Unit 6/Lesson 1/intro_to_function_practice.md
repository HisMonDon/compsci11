# Intro to Functions Practice
For each of the programs below, place them in a `main()` function and use `if __name__ == "__main__"` to call it.

### Hello, Name!
```python
name = input("Enter your name: ")

if name == "":
    name = "User"

print(f"Hello, {name}!")
```

### Area Calculator
```python
print("Welcome to the awesome area calculator!")
print()

length = int(input("Enter a length: "))
width = int(input("Enter a width: "))
print()

area = length * width

print(f"The area is {area} units squared")
```

### Area Calculator `greet()` Function
Modify your solution for the `Area Calculator` program and define another function called `greet()`. Place the first two print statements in there (the welcome), then call `greet()` from the `main()` function. The program should run the same as before.

**Note: Do not define functions within functions**. Define the `greet()` function between  `main` and `if __name__ ...`.

### Ticket Prices

Create a program that will ask how many tickets the user would like, then show them the total cost. Each ticket is `$13.95`. This should be entirely within a `main()` function. Optional: It would be good practice to define the price of each ticket (`$13.95`) as a global constant, outside the function at the top of the code, in `ALL_CAPS`.
