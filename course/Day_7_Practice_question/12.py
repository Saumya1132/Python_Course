# average value of all elements in a list of dictionaries

def calculate_average(list_of_dicts):
    total_sum = 0
    total_count = 0

    for dictionary in list_of_dicts:
        for value in dictionary.values():
            total_sum += value
            total_count += 1

    average = total_sum / total_count if total_count > 0 else 0
    return average

list_of_dicts = [{'a': 1, 'b': 2}, {'c': 3, 'd': 4}, {'e': 5, 'f': 6}]
average_value = calculate_average(list_of_dicts)
print(average_value)
