integer_string = "65, 75, 32, 22"
integers = [int(x) for x in integer_string.split(", ")]
for index, value in enumerate(integers):
    print(f"{index}: {value}")
