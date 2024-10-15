message = input("What is your message? ")
vowels = "aAeEiIoOuU"
count = 0

for char in message:
    if char in vowels:
        count += 1

print("There are", count, "vowels in the message.")
