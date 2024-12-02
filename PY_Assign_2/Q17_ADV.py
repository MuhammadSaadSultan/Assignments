# 5. Write a function that takes a list and removes all duplicate elements.


def remove_duplicates_with_set(input_list):
    return list(set(input_list))

my_list1 = [1, 2, 2, 3, 4, 4, 5]
result1 = remove_duplicates_with_set(my_list1)

print(result1) 
def remove_duplicates_preserve_order(input_list):
    seen = set()
    result = []
    for item in input_list:
        if item not in seen:
            seen.add(item)
            result.append(item)
    return result

my_list2 = [1, 2, 2, 3, 4, 4, 5]
result2 = remove_duplicates_preserve_order(my_list2)
print(result2)
