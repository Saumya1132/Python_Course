# min max values

def find_max_min(numbers):
    if not numbers:
        return None, None

    max_value = max(numbers)
    min_value = min(numbers)

    return max_value, min_value

numbers = [3, 5, 7, 2, 8, -1, 4, 10, 12]
max_value, min_value = find_max_min(numbers)

print(f"The maximum value is: {max_value}")
print(f"The minimum value is: {min_value}")
