def mix_string(a, b):
    result = []
    i, j = 0, 0
    while i < len(a) and j < len(b):
        result.append(a[i])
        result.append(b[j])
        i += 1
        j += 1
    result.extend(a[i:])
    result.extend(b[j:])
    return ''.join(result)

a = input()
b = input()

print(mix_string(a, b))
