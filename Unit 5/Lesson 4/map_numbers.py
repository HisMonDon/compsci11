number_string = "one,two,three,four"
number_map = {"zero": 0, "one": 1, "two": 2, "three": 3, "four": 4, "five": 5}
numbers = [number_map[num] for num in number_string.split(',')]
print(numbers)
