# text file with list of the numbers with function find the sum of all the numbers

def sum_numbers_from_file(filename):
    try:
        with open(filename, 'r') as file:
            numbers = [int(num) for num in file.read().split()]
            return sum(numbers)
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
        return None
    except ValueError:
        print("Error: File contains non-numeric data.")
        return None

filename = 'D:\\course\\Day_8_Practice_question\\numbers.txt'
total_sum = sum_numbers_from_file(filename)
if total_sum is not None:
    print(f"The sum of numbers in '{filename}' is: {total_sum}")
