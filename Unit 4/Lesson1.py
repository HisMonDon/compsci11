print("Type in a message, and I'll display it five times.")

message = input("Message: ")
times = int(input("How many times? "))
print()
n = 1
while n <= times:
    print(f"{n*10}. {message}")
    n += 1
