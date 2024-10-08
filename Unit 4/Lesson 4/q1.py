#Create a loop that counts from 0 to 10, but skip the number 7.
x = 0
while x <= 10:
    if x == 7:
        x += 1
        continue
    print(x)
    x += 1
