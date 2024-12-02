# 8. Create a program that checks if a given string is a palindrome.

 #Q What is palindrome?

 #> A palindrome is a word, phrase, or number that reads the same forward 
    # and backward, ignoring spaces, punctuation, and capitalization 
    # (e.g., "madam", "racecar", "civic", "saas").

input_str = "level"

input_str = input_str.replace(" ", "").lower()


if input_str == input_str[::-1]:
    print(f"'{input_str}' is a palindrome!")

elif input_str == "":
    print("The string is empty, it is a palindrome.")

elif len(input_str) == 1:
    print(f"'{input_str}' is a palindrome!")

else:
    print(f"'{input_str}' is not a palindrome.")


# The string "runinng" is not a palindrome because it doesn't read 
# the same forwards and backwards.

input_str = "runinng"

input_str = input_str.replace(" ", "").lower()


if input_str == input_str[::-1]:
    print(f"'{input_str}' is a palindrome!")

elif input_str == "":
    print("The string is empty, it is a palindrome.")

elif len(input_str) == 1:
    print(f"'{input_str}' is a palindrome!")

else:
    print(f"'{input_str}' is not a palindrome.")




