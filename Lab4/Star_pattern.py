n = int(input("Enter a number: "))

if n > 0:
    for i in range(1, n + 1):
        for j in range(i):
            print("*", end="")
        print()
else:
    print("Please enter a positive number.")

input("Press Enter to close the program...")