# 16. Take the length of three sides and classify the triangle (equilateral, isosceles, or scalene).


side1 = float(input("write the length of the first side: "))
side2 = float(input("write the length of the second side: "))
side3 = float(input("write the length of the third side: "))


if side1 == side2 == side3:
    print("The triangle is Equilateral.")
elif side1 == side2 or side2 == side3 or side1 == side3:
    print("The triangle is Isosceles.")
else:
    print("The triangle is Scalene.")



