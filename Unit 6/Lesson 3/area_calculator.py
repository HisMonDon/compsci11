import math

def area_triangle(base, height):
    return 0.5 * base * height

def area_square(side):
    return side * side

def area_rectangle(length, width):
    return length * width

def area_circle(radius):
    return math.pi * radius * radius

def main():
    while True:
        print("\nShape Area Calculator version 0.1 (c) 2005 Mitchell Sample Output, Inc.")
        print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-\n")
        print("1) Triangle")
        print("2) Rectangle")
        print("3) Square")
        print("4) Circle")
        print("5) Quit")
        
        choice = int(input("Which shape: "))
        
        if choice == 1:
            base = float(input("Base: "))
            height = float(input("Height: "))
            print(f"The area is {area_triangle(base, height)}.")
        elif choice == 2:
            length = float(input("Length: "))
            width = float(input("Width: "))
            print(f"The area is {area_rectangle(length, width)}.")
        elif choice == 3:
            side = float(input("Side length: "))
            print(f"The area is {area_square(side)}.")
        elif choice == 4:
            radius = float(input("Radius: "))
            print(f"The area is {area_circle(radius):.4f}.")
        elif choice == 5:
            print("Goodbye.")
            break
        else:
            print("Invalid choice, please select a number from 1 to 5.")

if __name__ == "__main__":
    main()
