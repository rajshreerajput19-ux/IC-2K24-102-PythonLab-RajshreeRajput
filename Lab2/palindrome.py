# Part 1: Number Palindrome (Arithmetic operations only)
def is_number_palindrome(n):
    if n < 0:
        return False
    temp = n
    rev = 0
    while temp > 0:
        digit = temp % 10
        rev = rev * 10 + digit
        temp //= 10
    return rev == n

num = int(input("Enter an integer to check palindrome: "))
if is_number_palindrome(num):
    print(f"{num} is a palindrome number.")
else:
    print(f"{num} is not a palindrome number.")

# Part 2: String Palindrome
def is_string_palindrome(s):
    return s == s[::-1]

text = input("\nEnter a string to check palindrome: ")
if is_string_palindrome(text):
    print(f"'{text}' is a palindrome string.")
else:
    print(f"'{text}' is not a palindrome string.")