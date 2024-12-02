# 1. Create a function that takes a list of numbers and returns the largest number.


def find_largest_number(numbers):
    return max(numbers)

numbers = [95, 60, 6, 17, 9, 38, 10, 150, 400, 980]
largest_number = find_largest_number(numbers)
print("The largest number is:", largest_number)
