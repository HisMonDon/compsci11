
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
