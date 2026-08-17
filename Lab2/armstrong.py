def is_armstrong(num):
    temp = num
    n = len(str(num))
    total = 0
    while temp > 0:
        digit = temp % 10
        total += digit ** n
        temp //= 10
    return total == num

# Single number check
num = int(input("Enter a number to check Armstrong: "))
if is_armstrong(num):
    print(f"{num} is an Armstrong number.")
else:
    print(f"{num} is not an Armstrong number.")

# Range check
print("\n--- Find Armstrong Numbers in a Range ---")
start = int(input("Enter start of range: "))
end = int(input("Enter end of range: "))

print(f"Armstrong numbers between {start} and {end}:")
for i in range(start, end + 1):
    if is_armstrong(i):
        print(i, end=" ")
print()