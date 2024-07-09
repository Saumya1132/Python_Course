# sort the list

def sort_by_length(strings):
    return sorted(strings, key=len)

strings = ["apple", "banana", "cherry", "date"]
sorted_strings = sort_by_length(strings)

print("Sorted strings by length:", sorted_strings)
