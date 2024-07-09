# check two sets having any common elements

def have_common_elements(set1, set2):
    common_elements = set1.intersection(set2)
    
    has_common = len(common_elements) > 0
    
    return has_common, common_elements

# Example usage:
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}
result, common_elements = have_common_elements(set1, set2)
print(f"Do the sets have common elements? {result}")  
print(f"Common elements: {common_elements}")  
