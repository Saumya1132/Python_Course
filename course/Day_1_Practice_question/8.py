# sum of all the positive values

def sum_of_positive_numbers(numbers):
    total = 0
    for number in numbers:
        if number > 0:
            total += number
    return total

numbers = [1, -2, 3, -4, 5]  
result = sum_of_positive_numbers(numbers)
print("Sum of positive numbers:", result)