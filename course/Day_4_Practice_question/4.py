# Sum of positive numbers

def sum_of_positive_numbers(numbers):
    return sum(number for number in numbers if number > 0)

numbers = [1, -2, 3, 4, -5, 6]
print(sum_of_positive_numbers(numbers))  