# Question 2: Butterfly Star Pattern

n = int(input("Enter the number of rows: "))

if n > 0:

    for i in range(1, n + 1):
        for j in range(i):
            print("*", end="")

        for j in range(2 * (n - i)):
            print(" ", end="")

        for j in range(i):
            print("*", end="")

        print()

    for i in range(n - 1, 0, -1):
        for j in range(i):
            print("*", end="")

        for j in range(2 * (n - i)):
            print(" ", end="")

        for j in range(i):
            print("*", end="")

        print()

else:
    print("Please enter a positive number.")

input("Press Enter to close the program...")