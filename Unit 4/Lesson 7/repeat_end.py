def repeat_end(s, n):
    end_part = s[-n:]
    result = end_part * n
    return result

s = input()
n = int(input())

print(repeat_end(s, n))
