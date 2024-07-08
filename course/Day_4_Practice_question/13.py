# Table

def print_table(number):
    print(f"Table of {number}")
    for i in range(1, 11):
        print(f"{number} x {i} = {number * i}")

number = int(input("Enter a number: "))
print_table(number)