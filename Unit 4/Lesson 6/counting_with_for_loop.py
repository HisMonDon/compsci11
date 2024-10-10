print("Type in a message, and I'll display it five times.")

message = input("Message: ")

for n in range(2, 20, 2):
    print(f"{n}. {message}")
