#See if you can change the for loop so that the message starts at 2 and counts by twos, like so:
#Type in a message, and I'll display it ten times.
#Message: qwerty
#2. qwerty
#4. qwerty
#6. qwerty
#8. qwerty
#10. qwerty
#12. qwerty
#14. qwerty
#16. qwerty
#18. qwerty
#20. qwerty


print("Type in a message, and I'll display it five times.")

message = input("Message: ")

for n in range(2, 21, 2):
    print(f"{n}. {message}")
