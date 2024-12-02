# 12. Write a program that takes a temperature in Celsius and checks if it’s freezing, moderate, or hot.


temp = float(input("Enter the temp in Celsius: "))

if temp <= 0:
    print("It's freezing!")
elif 1 <= temp <=25:
    print("The weather is moderate.")
else:
    print("It's hot!")
