# 1. Write a function that calculates the power of a number without using the ** operator.


def pow(base, exponent):
    if exponent == 0:
        return 1
    elif exponent < 0:
        base = 1 / base
        exponent = -exponent
    
    result = 1
    for _ in range(exponent):
        result *= base
        
    return result

print(pow(4, 6))
print(pow(5, -4))
print(pow(9, 0))
