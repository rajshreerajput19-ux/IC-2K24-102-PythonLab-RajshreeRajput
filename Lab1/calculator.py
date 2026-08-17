# Aim: Build a small menu-driven calculator with at least 4 operations that runs until the user chooses to exit.

while True:
    print("\n--- Menu-Driven Calculator ---")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Exit")
    
    choice = input("Enter your choice (1-5): ")
    
    if choice == '5':
        print("Exiting calculator. Thank you!")
        break
        
    if choice in ('1', '2', '3', '4'):
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        
        if choice == '1':
            print("Result:", num1 + num2)
        elif choice == '2':
            print("Result:", num1 - num2)
        elif choice == '3':
            print("Result:", num1 * num2)
        elif choice == '4':
            if num2 != 0:
                print("Result:", num1 / num2)
            else:
                print("Error: Division by zero is not allowed.")
    else:
        print("Invalid choice! Please select a valid option between 1 and 5.")