# 9. Take three sides of a triangle as input and check if they form a valid triangle.


x = float(input("Enter a side 1: "))
y = float(input("Enter a side 2: "))
z = float(input("Enter a side 3: "))

if x + y > z and x + z > y and y + z > x:
    print("Valid Triangle")
else:
    print("Invalid Triangle")
