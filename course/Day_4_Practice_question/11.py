# list_intersection

def list_intersection(list1, list2):
    return list(set(list1) & set(list2))

list1 = [1, 2, 3, 4]
list2 = [3, 4, 5, 6]
print(list_intersection(list1, list2)) 
