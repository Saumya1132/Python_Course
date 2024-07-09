# most frequent in list

def find_most_frequent(lst):
    frequency_dict = {}
    
    for item in lst:
        if item in frequency_dict:
            frequency_dict[item] += 1
        else:
            frequency_dict[item] = 1
    
    most_frequent_element = max(frequency_dict, key=frequency_dict.get)
    count = frequency_dict[most_frequent_element]
    
    return (most_frequent_element, count)

# Example usage:
my_list = [1, 2, 3, 2, 1, 4, 2, 5, 2]
most_frequent_element, count = find_most_frequent(my_list)
print(f"Element '{most_frequent_element}' is the most frequent with a count of {count}")
