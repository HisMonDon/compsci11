# 1. Calculate the sum of the numbers from 1 to 10

sum = 0
i = 1
while i <= 10:
    sum +=i
    i+=1

print(f"The sum is {sum}.")

# 2. Calculate the sum of the numbers from 10 to 20

sum = 0
i = 10
while i <= 20:
    sum += i
    i+=1

print(f"The sum is {sum}.")

# 3. Calculate the difference between the sum of the numbers from 100 to 200 and the sum of the numbers from 200 to 300.

firstsum = 0
secondsum = 0
i = 100
while i <= 200:
    firstsum += i
    i+=1
        # No need to set i to 200, as it is already at 200
while i <=300:
    secondsum+=i
    i+=1

difference = secondsum - firstsum

print(f"The difference is {difference}.")

# 4. Calculate the sum of the multiples of 5 between the numbers 1000 and 10000.

sum = 0
i = 1005
    # The first multiple of 5 between the two numbers is 1005
while i <= 10000:
    sum += i
    i+=5

print(f"The sum is {sum}.")

# 5. Calculate the sum of the multiples of 5 between 1 and 100, but do not include numbers that are multiples of 3. Modulus (%) will come in handy here.
