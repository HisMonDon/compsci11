Given the code below, answer the following questions:
How many arguments are sent to the num_chairs function? What are they?
What are the names of the parameter variables? What values are they assigned from running the code below?
What is the output?
What happens when you remove an argument? when you add one?
def num_chairs(tables, chairs_per_table):
    chairs = tables * chairs_per_table
    print(f"You will need {chairs} chairs.")


num_chairs(4, 5)

There are 2 arguments sent to the num_chairs function, which are 4 and 5
THe names of the parameter variables are tables, and chairs_per_table. They are assigned to the arguments, 4 and 5.
The output will be "You will need 20 chairs."
When you remove an argument, it will produce an error, expected 2 arguments
If you add an argument, it will also produce an error, expected 2 arguments.
