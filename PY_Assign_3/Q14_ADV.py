# Sort the keys of the dictionary {'z': 1, 'a': 2, 'c': 3} in ascending order and 
# print the sorted dictionary.


original_dict = {'z': 1, 'a': 2, 'c': 3}

sorted_dict2 = {k: original_dict[k] for k in sorted(original_dict)}

print("Method 2:", sorted_dict2)