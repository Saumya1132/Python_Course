# find union , intersection and difference between them of the two sets 

set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}

union_set = set1.union(set2)
print("Union:", union_set)   

intersection_set = set1.intersection(set2)
print("Intersection:", intersection_set)  

difference_set = set1.difference(set2)
print("Difference (set1 - set2):", difference_set)  

difference_set = set2.difference(set1)
print("Difference (set2 - set1):", difference_set)  