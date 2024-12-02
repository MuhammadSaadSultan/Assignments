# 10. Write a program to determine if a given character is a vowel or consonant.

character = input("Enter a character: ")

character = character.lower()

if character in 'aeiou':
    print(f"The character '{character}' is a vowel.")

elif character.isalpha():
    print(f"The character '{character}' is a consonant.")
else:
    print("wrong input! Please enter an alphabetic character.")
