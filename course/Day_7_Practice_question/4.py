# merge dictionaries

dict1 = {"name": "saumya", "age": "22", "city": "ahmedabad"}
dict2 = {"college": "indus", "passout": "2024"}

merged_dict = dict1.copy()

merged_dict.update(dict2)

print("Merged dictionary using update method:", merged_dict)
