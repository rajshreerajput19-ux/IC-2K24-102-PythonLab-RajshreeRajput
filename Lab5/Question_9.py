# Question 9: Decorators and wraps

from functools import wraps


def log_function(func):

    @wraps(func)
    def wrapper(*args, **kwargs):
        print("Entering", func.__name__)

        result = func(*args, **kwargs)

        print("Exiting", func.__name__)

        return result

    return wrapper


@log_function
def my_function(x, y):
    '''Adds two numbers together.'''
    return x + y


my_function(1, 2)

print(my_function.__name__)
print(my_function.__doc__)
input("Press Enter to close the program...")