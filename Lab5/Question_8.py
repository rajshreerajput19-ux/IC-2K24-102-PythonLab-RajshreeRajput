# Question 8: Set Operations

A = {1, 2, 3, 4}
B = {2, 3, 5}

# Intersection
print(A & B)

# Union
print(A | B)

# Difference
print(A - B)

# Symmetric Difference
print(A ^ B)

# Subset
print({1, 2} <= {1, 2, 3})

# Dictionary with tuple key
my_dict = {(1, 2, 3): 'abc'}
print(my_dict)

# A list cannot be used as a dictionary key
# my_dict = {[1, 2, 3]: 'abc'}  # TypeError
input("Press Enter to close the program...")