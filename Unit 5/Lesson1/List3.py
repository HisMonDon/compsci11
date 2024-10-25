import random


mylist = []
for x in range(1000):
    mylist.append(random.randrange(10, 100))

for x in range(len(mylist)):
    print(mylist[x], end = ' ')
