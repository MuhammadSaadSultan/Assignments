# 6. Create a function that takes a string and counts the frequency of each character.


from collections import Counter

def count_char_frequency_with_counter(input_string):
    return dict(Counter(input_string))

input_string = "dear coders"
frequency_counter = count_char_frequency_with_counter(input_string)
print(frequency_counter)

def count_char_frequency_with_dict(input_string):
    frequency_dict = {}
    for char in input_string:
        if char in frequency_dict:
            frequency_dict[char] += 1
        else:
            frequency_dict[char] = 1
    return frequency_dict

frequency_dict = count_char_frequency_with_dict(input_string)
print(frequency_dict)

