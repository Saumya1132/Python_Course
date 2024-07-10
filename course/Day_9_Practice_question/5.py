# create class to represent employee name position and salary from a csv file
import csv

class Employee:
    def __init__(self, name, position, salary):
        self.name = name
        self.position = position
        self.salary = salary

def create_employee_list(csv_file):
    employee_list = []

    with open(csv_file, 'r') as file:
        reader = csv.reader(file)
        next(reader)  # Skip the header row

        for row in reader:
            if len(row) != 3:
                print(f"Skipping malformed row: {row}")
                continue
            name, position, salary = row
            employee_list.append(Employee(name, position, float(salary)))

    return employee_list

csv_file = 'D:\\course\\Day_8_Practice_question\\employees.csv'

employee_list = create_employee_list(csv_file)

for employee in employee_list:
    print(f"{employee.name}: {employee.position}, {employee.salary}")

employee_list.sort(key=lambda x: x.salary, reverse=True)
