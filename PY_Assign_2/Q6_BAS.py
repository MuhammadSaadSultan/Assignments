# 6. Write a function to count the vowels in a given string.


def count_vowel_occurrences(text):
    vowel_set = "aeiouAEIOU"
    
    vowel_count = 0
    
    for char in text:
        if char in vowel_set:
            vowel_count += 1
    
input_string = "I Love Coding"
result = count_vowel_occurrences(input_string)
print(f"The number of vowels in the string: {result}")

