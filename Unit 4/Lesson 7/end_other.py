first = input()
second = input()
split_index = len(first)-1
first = (first[split_index:]).lower()
split_index = len(second)-1
second = (second[split_index:]).lower()
print(first == second)
