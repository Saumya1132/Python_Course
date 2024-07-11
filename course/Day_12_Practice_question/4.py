# read csv file of the students and find average age of students

import csv

def find_average_age(csv_file):
    total_age = 0
    count = 0
    
    with open(csv_file, 'r') as file:
        reader = csv.DictReader(file)
        next(reader)
        
        for row in reader:
            age = int(row['age'])
            total_age += age
            count += 1
    
    if count == 0:
        return 0
    
    average_age = total_age / count
    return average_age

csv_file = 'students.csv'

average_age = find_average_age(csv_file)

print(f"The average age of students in the file {csv_file} is: {average_age:.2f}")

# sample students.csv content:

# name,age,grade

# John,18,A

# Jane,19,B

