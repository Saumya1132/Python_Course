# Find even number in the list and store all of them in new list

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
even_numbers = []

for number in numbers:
    if number % 2 == 0:
        even_numbers.append(number)
print(even_numbers)