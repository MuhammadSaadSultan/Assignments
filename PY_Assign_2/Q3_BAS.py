# 3. Write a function to find the factorial of a number using recursion.


def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

number = 15
print(f"Factorial of {number} is {factorial(number)}")


# So In this code, the base case is incorrect (it should be 0, not 9), 
# and you're subtracting 9 in the recursion, whereas for factorial, you 
# should subtract 1.