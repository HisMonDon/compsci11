def main():
    name = input("Enter your name: ")
    
    if name == "":
        name = "User"
    
    print(f"Hello, {name}!")
if __name__ == "__main__":
    main()

def main():
    print("Welcome to the awesome area calculator!")
    print()
    
    length = int(input("Enter a length: "))
    width = int(input("Enter a width: "))
    print()
    
    area = length * width
    
    print(f"The area is {area} units squared")
if __name__ == "__main__":
    main()

# Define a global constant for the ticket price
TICKET_PRICE = 13.95

def greet():
    print("Welcome to the awesome area calculator!")
    print()

def main():
    greet()
    length = int(input("Enter a length: "))
    width = int(input("Enter a width: "))
    print()
    
    area = length * width
    print(f"The area is {area} units squared")

if __name__ == "__main__":
    main()

def main():
    num_tickets = int(input("How many tickets would you like? "))
    total_cost = num_tickets * TICKET_PRICE
    print(f"The total cost for {num_tickets} tickets is ${total_cost:.2f}")

if __name__ == "__main__":
    main()
