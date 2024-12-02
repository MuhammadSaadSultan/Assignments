# 6. Create a function that accepts a dictionary and returns the key with the highest value.


def key_with_highest_value(d):
    if not d:
        return None
    
    return max(d, key=d.get)

my_dict = {"a": 50, "b": 70, "c": 90}

result = key_with_highest_value(my_dict)

print(result)
