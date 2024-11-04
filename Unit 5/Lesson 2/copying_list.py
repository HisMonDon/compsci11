
import random

list1 = [random.randint(1, 100) for _ in range(10)]
list2 = list1[:] 
list1[-1] = -7
print("List 1:", ' '.join(map(str, list1)))
print("List 2:", ' '.join(map(str, list2)))

# Explanation of why you can't copy a list by doing list2 = list1
# If you do list2 = list1, both list1 and list2 will reference the same object.
# Changes in one will affect the other because they are not independent copies.
