def is_perfect(n):
    if n <= 0:
        return False
    divisors_sum = sum(i for i in range(1, n) if n % i == 0)
    return divisors_sum == n

# Single number check
num = int(input("Enter a number to check Perfect Number: "))
if is_perfect(num):
    print(f"{num} is a Perfect number.")
else:
    print(f"{num} is not a Perfect number.")

# Limit check
limit = int(input("\nEnter upper limit to print perfect numbers: "))
print(f"Perfect numbers up to {limit}:")
for i in range(1, limit + 1):
    if is_perfect(i):
        print(i, end=" ")
print()