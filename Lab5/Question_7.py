# Question 7: *args and **kwargs

def all_the_args(*args, **kwargs):
    print(args)
    print(kwargs)


args = (1, 2, 3, 4)
kwargs = {'a': 3, 'b': 4}

# Call 1
print("Call 1:")
all_the_args(*args)

# Call 2
print("Call 2:")
all_the_args(**kwargs)

# Call 3
print("Call 3:")
all_the_args(*args, **kwargs)
input("Press Enter to close the program...")