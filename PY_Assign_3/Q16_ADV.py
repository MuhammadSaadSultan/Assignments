# Write a Python function to check if two dictionaries are identical (contain the same key-value pairs).

def are_dicts_identical(dict1, dict2):
    return dict1 == dict2

dict1 = {'a': 1, 'b': 2, 'c': 3}
dict2 = {'a': 1, 'b': 2, 'c': 3}
dict3 = {'a': 1, 'b': 2, 'c': 4}

print(are_dicts_identical(dict1, dict2))
print(are_dicts_identical(dict1, dict3))
