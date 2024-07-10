# function to calculate the area and the circumference of the circle

class Circle:
    def __init__(self, radius):
        self.radius = radius
        
    def calculate_area(self):
        return 3.14 * self.radius ** 2
    
    def calculate_circumference(self):
        return 2 * 3.14 * self.radius
    
circle = Circle(5)

area = circle.calculate_area()
circumference = circle.calculate_circumference()

print("The area of the circle is:", area)
print("The circumference of the circle is:", circumference)