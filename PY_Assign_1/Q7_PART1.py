# 7. Write a program to find the largest of three numbers.


num17 = float(input("Enter the first number: "))
num50 = float(input("Enter the second number: "))
num100 = float(input("Enter the third number: "))

if num17 >= num50 and num17 >= num100:
    largest = num17
elif num50 >= num17 and num50 >= num100:
    largest = num50
else:
    largest = num100

print("The largest number is:", largest)


# After running the code, input three numbers when prompted, 
# and the program will display the largest number