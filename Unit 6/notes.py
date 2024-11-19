
# FUNCTIONS
# Why? Simplify code. Make it easier to read. Hide a lot of complexity.
# When? Repeating the same lines of code with slight changes


# to define a function:
#def keyword
#|
#v
def name_of_function():
    print("hello")

#call/invoke/run/execute the function
name_of_function()
name_of_function()

#sending arguments, defining parameters
#parameters are rules, defined when you make the function (a and b)
#arguments are the specific data you send when you call the function(e.g. line 23, 5 and 7 are the arguments)
def add(a: int, b: int) -> int  :
    print(a + b)
add(5, 7)
#or:
def add2(a, b):
    print(a + b)
add2(5, 7)
#this only takes arguments, but doesnt return anything
#we can RETURN values
#                             Return type
#                             v
def multiply(a: int, b: int) -> int:
    print("multiply ran")
    return a * b

#need to save in a variable
result = multiply(5, 10)
print(result)
#-------------------------------------------------------------
#Create a function that takes a number, adds 5 to the number, and returns the result. Store this in a variable and print it out.
#Create another function that takes a name, creates a string greeting with the name int it, stores it in a variable, and prints it out
#My solution:
def addfive(number : int) -> int:
    return number+5
mynumber = addfive(3)
print(mynumber)


def greeter(name : str) -> str:
    return f'Hello {name}!'
greetstring = greeter("Eric")
print(greetstring)

#FUNCTIONS SHOULD NOT HAVE INPUT OR PRINT (except for main)
#Main function:
def addfive(number):
    return number+5
mynumber = addfive(3)
print(mynumber)


def greeter(name : str) -> str:
    return f'Hello {name}!'
def main():
    greetstring = greeter("Eric")
    print(greetstring)
if __name__ == "__main__":
    main()
