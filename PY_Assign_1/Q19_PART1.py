# 19. Check if a string input is uppercase, lowercase, or a mix.


input = input("Enter a string: ")


if input.isupper():
    print("The string is uppercase.")
elif input.islower():
    print("The string is lowercase.")
else:
    print("The string is a mix of uppercase and lowercase.")
