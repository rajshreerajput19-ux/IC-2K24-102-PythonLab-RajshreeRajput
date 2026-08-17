rows = int(input("Enter number of rows n: "))

# 1. Right-angled triangle of stars
print("\n1. Right-angled Triangle of Stars:")
for i in range(1, rows + 1):
    print("*" * i)

# 2. Number pattern (1 up to row number)
print("\n2. Number Pattern:")
for i in range(1, rows + 1):
    for j in range(1, i + 1):
        print(j, end=" ")
    print()

# 3. Simple pyramid pattern centered using spaces
print("\n3. Centered Pyramid Pattern:")
for i in range(1, rows + 1):
    spaces = " " * (rows - i)
    stars = " ".join(["*"] * i)
    print(spaces + stars)