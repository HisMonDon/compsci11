def main():
    start = int(input("Count from: "))
    end = int(input("Count to  : "))
    step = int(input("Count by  : "))
    for i in range(start, end + 1, step):
        print(i, end=' ')
    print()

if __name__ == "__main__":
    main()