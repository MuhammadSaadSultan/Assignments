# 3. Write a program that checks if a given year is a leap year.


year = int(input("Enter a year: "))

if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(f"{year} is a leap year.")
else:
    print(f"{year} is not a leap year.")

# When you run this code and give the input like ( Year: 2024, 1900, 2000, 2023...), 
# it will display whether that year is a "leap year" or "not a leap year" 
# according to the leap year rules.