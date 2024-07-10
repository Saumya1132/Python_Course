# Find the students with the highest score

import csv

def find_top_student(csv_file):
    try:
        with open(csv_file, mode='r') as file:
            csv_reader = csv.reader(file)
            
            next(csv_reader)
            
            top_student = None
            top_score = -1
            
            for row in csv_reader:
                name = row[0]
                score = int(row[1])
                
                if score > top_score:
                    top_student = name
                    top_score = score
            
            print(f"The top student is {top_student} with a score of {top_score}")
    except Exception as e:
        print(f"An error occurred: {e}")

csv_file = 'D:\course\Day_8_Practice_question\students.csv'
find_top_student(csv_file)
