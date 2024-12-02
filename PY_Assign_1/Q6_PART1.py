# 6. Write a program to find the largest of two numbers.


num17 = float(input("Enter the first number: "))
num60 = float(input("Enter the second number: "))


if num17 > num60:
    print(f"The largest number is {num17}")
elif num60 > num17:
    print(f"The largest number is {num60}")
else:
    print("Both numbers are equal.")


# -> Enter two numbers when you run this code.
# -> The program will compare them and print the largest number.
# -> If both numbers are equal, it will print "Both numbers are equal."
