# Largest number of list

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
largest = numbers[0]

for number in numbers:
    if number > largest:
        largest = number

print(largest)