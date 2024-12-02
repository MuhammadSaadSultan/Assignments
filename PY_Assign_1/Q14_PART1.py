# 14. Check if a year input by the user is a century year.


year = int(input("write a year: "))

if year % 100 == 0:
    print(f"{year} is a century year.")
else:
    print(f"{year} is not a century year.")
