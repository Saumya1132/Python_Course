# class to represent student with attributes name ,age and grade

class Student:
    def __init__(self,name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade
        
student1 = Student("John Doe", 18, 85)
student2 = Student("Jane Smith", 19, 90)

print(f"Name: {student1.name}, Age: {student1.age}, Grade: {student1.grade}")
print(f"Name: {student2.name}, Age: {student2.age}, Grade: {student2.grade}")