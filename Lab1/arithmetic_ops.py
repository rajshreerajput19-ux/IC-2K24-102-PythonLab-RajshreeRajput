# Aim: Take two numbers as input and print their sum, difference, product, quotient, and remainder.

# Take input from the user and convert them to float for division support
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

# Calculate arithmetic operations
sum_result = num1 + num2
diff_result = num1 - num2
product_result = num1 * num2

# Handle division by zero just in case
if num2 != 0:
    quotient_result = num1 / num2
    remainder_result = num1 % num2
else:
    quotient_result = "Undefined (Division by zero)"
    remainder_result = "Undefined (Division by zero)"

# Print the labeled outputs
print("\n--- Arithmetic Results ---")
print("Sum:", sum_result)
print("Difference:", diff_result)
print("Product:", product_result)
print("Quotient:", quotient_result)
print("Remainder:", remainder_result)