def find_unique_elements(list1, list2):
    unique_list1 = list(set(list1) - set(list2))
    unique_list2 = list(set(list2) - set(list1))
    return unique_list1, unique_list2

list1 = [1, 2, 3, 4, 5]
list2 = [4, 5, 6, 7, 8]
unique_list1, unique_list2 = find_unique_elements(list1, list2)
print("Unique elements in list1:", unique_list1)
print("Unique elements in list2:", unique_list2)