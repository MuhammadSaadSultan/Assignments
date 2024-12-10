# Reverse the dictionary {'a': 1, 'b': 2, 'c': 3} so that keys become values and values become keys.

original_dict = {'a': 1, 'b': 2, 'c': 3}

reversed_dict = {value: key for key, value in original_dict.items()}

print("Original Dictionary:", original_dict)
print("Reversed Dictionary (Method 1):", reversed_dict)
