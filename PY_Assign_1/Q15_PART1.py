# 15. Write a program to check if a number is within a specified range.



number = float(input("Enter a number: "))
min_value = float(input("Enter the min value of the range: "))
max_value = float(input("Enter the max value of the range: "))


if min_value <= number <= max_value:
    print(f"The number {number} is within the range {min_value} to {max_value}.")
else:
    print(f"The number {number} is outside the range {min_value} to {max_value}.")


# Once you run the code, you will be prompted to enter:

# -> The number you want to check.
# -> The minimum value of the range.
# -> The maximum value of the range.

# ->>> You don't need to do anything else, just enter the values when prompted, and the result will be shown.
