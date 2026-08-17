# Version 1: Loop-based
def fibonacci_loop(n):
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    fib = [0, 1]
    for _ in range(2, n):
        fib.append(fib[-1] + fib[-2])
    return fib

n_terms = int(input("Enter number of terms for Fibonacci: "))
print(f"Fibonacci series (Loop): {fibonacci_loop(n_terms)}")

# Version 2: Recursive with call count tracking
call_count = 0

def fibonacci_recursive(n):
    global call_count
    call_count += 1
    if n <= 1:
        return n
    return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)

call_count = 0
n_rec = 10  # small n as specified
print(f"Fibonacci({n_rec}) using recursion = {fibonacci_recursive(n_rec)}")
print(f"Total function calls made by recursive version: {call_count}")