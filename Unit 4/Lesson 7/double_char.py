# Get any string from the user, output a string where for every char in the original, there are two chars.
string = input()
for x in string:
    print(f"{x}{x}", end = '')
