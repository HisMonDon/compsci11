def contains_bob_pattern(s):
    i = 0
    while i < len(s) - 2:
        if s[i] == 'b' and s[i+2] == 'b':
            return True
        i += 1
    return False

scan = input()
print(contains_bob_pattern(scan))
