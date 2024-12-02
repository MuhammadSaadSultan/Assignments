# 3. Write a function to check whether a string is a palindrome.


def is_palindrome(s):
    s = s.replace(" ", "").lower()
    
    return s == s[::-1]

input_string = "A man a plan a canal Panama"
if is_palindrome(input_string):
    print("The string is a palindrome.")
else:
    print("The string is not a palindrome.")
