def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

# Single number check
num = int(input("Enter a number to check Prime: "))
if is_prime(num):
    print(f"{num} is a Prime number.")
else:
    print(f"{num} is not a Prime number.")

# Range limit check
limit = int(input("\nEnter upper limit to print prime numbers: "))
print(f"Prime numbers up to {limit}:")
for i in range(2, limit + 1):
    if is_prime(i):
        print(i, end=" ")
print()