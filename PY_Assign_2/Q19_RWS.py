# Real-world Scenarios QUESTION:
# 1. Write a function that takes a list of employee salaries and calculates the average salary.


def calculate_average_salary(salaries):
    if len(salaries) == 0:
        return 0 
    return sum(salaries) / len(salaries)

salaries = [90000, 160000, 301000, 3170000, 35000]
average_salary = calculate_average_salary(salaries)

print("The average salary is:", average_salary)
