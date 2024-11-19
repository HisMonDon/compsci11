# Arguments and Parameters Practice

1. Given the code below, answer the following questions:
    - How many arguments are sent to the `num_chairs` function? What are they?
    - What are the names of the parameter variables? What values are they assigned from running the code below?
    - What is the output?
    - What happens when you remove an argument? when you add one?
    ```python
    def num_chairs(tables, chairs_per_table):
        chairs = tables * chairs_per_table
        print(f"You will need {chairs} chairs.")


    num_chairs(4, 5)
    ```
2. Create a function that takes one integer argument and simply prints it out. Call this function `print_integer`.
3. Create a function that takes two integer arguments and prints out their difference. You can use `math.abs()` for absolute value.
4. List the two things wrong with the following code and how to fix it.
    ```python
    function subtract(a):
        print(a - b)
       
    
    subtract(5, 7)
    ```
5. How would you *call* the following function? Give two examples.
    ```python
    def activate_thrusters(percent_power):
        pass
    ```
6. What is wrong with how the code below calls a function that takes a name and how many apples that person will eat? Give an example of the correct way to do it.
    ```python
    person_apples
    ```
