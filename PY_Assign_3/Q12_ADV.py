# Merge the following two dictionaries and print the result:
# - dict1 = {'a': 1, 'b': 2}  
# - dict2 = {'c': 3, 'd': 4}


# Method-1
dict1 = {'a': 1, 'b': 2}
dict2 = {'c': 3, 'd': 4}

merged_dict = dict1.copy()
merged_dict.update(dict2)

print(merged_dict)

# Method-2
dict1 = {'a': 1, 'b': 2}
dict2 = {'c': 3, 'd': 4}

merged_dict = dict1 | dict2

print(merged_dict)

