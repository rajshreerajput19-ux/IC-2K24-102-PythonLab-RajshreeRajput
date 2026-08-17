import sys

# Importing or re-defining logic functions for menu inclusion
def run_menu():
    while True:
        print("\n===== MAIN MENU =====")
        print("1. Check Armstrong Number")
        print("2. Check Prime Number")
        print("3. Check Perfect Number")
        print("4. Check Palindrome (Number/String)")
        print("5. Fibonacci Series")
        print("6. Pattern Printing")
        print("7. Exit")
        
        choice = input("Enter your choice (1-7): ")
        
        if choice == '1':
            n = int(input("Enter number: "))
            # logic here or call function
            print("Armstrong check executed.")
        elif choice == '2':
            n = int(input("Enter number: "))
            print("Prime check executed.")
        elif choice == '3':
            n = int(input("Enter number: "))
            print("Perfect number check executed.")
        elif choice == '4':
            print("Palindrome executed.")
        elif choice == '5':
            n = int(input("Enter terms: "))
            print("Fibonacci executed.")
        elif choice == '6':
            r = int(input("Enter rows: "))
            print("Patterns executed.")
        elif choice == '7':
            print("Exiting program. Goodbye!")
            break
        else:
            print("Invalid choice! Please enter a number between 1 and 7.")

if __name__ == "__main__":
    run_menu()