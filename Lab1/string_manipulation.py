# Aim: Take a full name as input and print it in uppercase, lowercase, reversed, and print its length.

# Take full name input from the user
full_name = input("Enter your full name: ")

# String manipulations
upper_name = full_name.upper()
lower_name = full_name.lower()
name_length = len(full_name)
# Slicing used to reverse the string
reversed_name = full_name[::-1] 

# Print the results clearly
print("\n--- String Manipulation Results ---")
print("Uppercase:", upper_name)
print("Lowercase:", lower_name)
print("Length of name:", name_length)
print("Reversed name:", reversed_name)