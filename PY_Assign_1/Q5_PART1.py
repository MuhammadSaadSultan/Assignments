# 5. Ask the user for a grade percentage and display the corresponding letter grade (A, B, C, D, F).



grade_percentage = float(input("Enter your grade percentage: "))

if grade_percentage >= 95:
    letter_grade = 'A'
elif grade_percentage >= 85:
    letter_grade = 'B'
elif grade_percentage >= 70:
    letter_grade = 'C'
elif grade_percentage >= 33:
    letter_grade = 'D'
else:
    letter_grade = 'F'

print(f"Your letter grade is: {letter_grade}")


# Here's examples of what happens with different inputs:

# If you enter a value below 33, the output will be "F".
# If you enter a value between 33 and 59, the output will be "D".
# If you enter a value between 60 and 74, the output will be "C".
# If you enter a value between 75 and 94, the output will be "B".
# If you enter 95 or higher, the output will be "A".