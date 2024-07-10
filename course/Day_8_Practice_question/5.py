# Average salary calculation from csv file

import csv

def calculate_average_salary(csv_file):
    try:
        total_salary = 0
        employee_count = 0
        
        with open(csv_file, mode='r') as file:
            csv_reader = csv.reader(file)
            
            next(csv_reader)
            
            for row in csv_reader:
                salary = float(row[2]) 
                total_salary += salary
                employee_count += 1
        
        if employee_count == 0:
            print("No employees found in the file.")
        else:
            average_salary = total_salary / employee_count
            print(f"The average salary of all employees is: {average_salary:.2f}")
    except Exception as e:
        print(f"An error occurred: {e}")

csv_file = 'D:\course\Day_8_Practice_question\employees.csv'
calculate_average_salary(csv_file)
