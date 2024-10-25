import random


mylist = []
mylist.append(random.randint(1, 100))
mylist.append(random.randint(1, 100))
mylist.append(random.randint(1, 100))
mylist.append(random.randint(1, 100))
mylist.append(random.randint(1, 100))
mylist.append(random.randint(1, 100))
mylist.append(random.randint(1, 100))
mylist.append(random.randint(1, 100))
mylist.append(random.randint(1, 100))
mylist.append(random.randint(1, 100))

for x in range(len(mylist)):
    print(f"Slot {x} contains a {mylist[x]}")
