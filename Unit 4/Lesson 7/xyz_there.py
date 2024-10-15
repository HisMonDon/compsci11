def contains_xyz(s):
    i = 0
    while i < len(s) - 2:
        if s[i:i+3] == 'xyz':
            if i == 0 or s[i-1] != '.':
                return True
        i += 1
    return False

test_case = input(
print(contains_xyz(case))
