# given csv file with employee details(name,position,salary)create an Employee class with private attributes.
import csv

class Employee:
    def __init__(self, name, position, salary):
        self.__name = name
        self.__position = position
        self.__salary = salary

    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name
    def get_position(self):
        return self.__position


    def set_position(self, position):
        self.__position = position

    def get_salary(self):
        return self.__salary
    def set_salary(self, salary):
        self.__salary = salary
    def display_info(self):
        print(f"Name: {self.__name}")
        print(f"Position: {self.__position}")
        print(f"Salary: ${self.__salary}")

def read_employees_from_csv(file_path):
    employees = []
    with open(file_path, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            employee = Employee(row['name'], row['position'], float(row['salary']))
            employees.append(employee)
    return employees

# Example usage
if __name__ == "__main__":

    employees = read_employees_from_csv('C:\python\Day-10\employee.csv')
    for employee in employees:
        employee.display_info()
        print()
