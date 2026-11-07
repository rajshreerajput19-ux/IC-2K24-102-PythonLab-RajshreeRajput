# Question 1: Hollow Diamond Pattern

n = int(input("Enter an odd number: "))

if n > 0 and n % 2 != 0:
    mid = n // 2

    for i in range(n):
        for j in range(n):
            if j == abs(mid - i) or j == n - 1 - abs(mid - i):
                print("*", end="")
            else:
                print(" ", end="")
        print()

else:
    print("Please enter a positive odd number.")

input("Press Enter to close the program...")