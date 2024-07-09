# common element between two lists and stores them in new lists

l1 = [1, 2, 3, 4,9]
l2 = [1,3,5,6,7,8,9]

common_elements = []

for num in l1:
    if num in l2:
        common_elements.append(num)
        
print("Common elements:", common_elements)