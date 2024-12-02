# 1. Write a function to calculate the area of a circle given its radius.


import math

def calculate_area_of_circle(radius):

    area = math.pi * radius ** 2
    return area

radius = 17
area = calculate_area_of_circle(radius)
print("The area of the circle with radius", radius, "is:", area)

# In this code a function calculate_area_of_circle(radius) to calculate 
# the area of a circle using the formula 𝐴 = 𝜋 𝑟 2 A=πr 2 , and then 
# prints the area for a circle with a radius of 17.

