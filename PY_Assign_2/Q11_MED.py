# 5. Write a function to calculate the GCD (Greatest Common Divisor) of two numbers.

def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

print(gcd(74, 96))
print(gcd(105, 180))
