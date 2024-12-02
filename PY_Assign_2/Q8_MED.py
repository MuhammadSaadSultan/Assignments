# 2. Write a function to find the nth Fibonacci number using recursion.


def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

# Example usage
n = 17
print(f"The {n}th Fibonacci number is: {fibonacci(n)}")
