# Enter list of number and return square

def square_numbers(numbers):
    return [num ** 2 for num in numbers]

input_numbers = input("Enter numbers separated by spaces: ")

numbers = [float(num) for num in input_numbers.split()]

squared_numbers = square_numbers(numbers)

print("Squared numbers:", squared_numbers)

