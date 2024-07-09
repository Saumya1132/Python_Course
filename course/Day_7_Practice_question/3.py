# create a set of unique numbers from a list of numbers

def unique_numbers(numbers):
    unique_set = set(numbers)
    return unique_set

numbers = [1, 2, 3, 4, 5, 1, 2, 3, 4, 3, 2]

unique_numbers_set = unique_numbers(numbers)

print(unique_numbers_set)