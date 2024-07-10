# cricle class to calculate the area and circumference for multiple circles
class Circle:
    def __init__(self, radius):
        self.radius = radius
        
    def calculate_area(self):
        return 3.14 * self.radius ** 2
    
    def calculate_circumference(self):
        return 2 * 3.14 * self.radius

# Creating instances of the Circle class
circles = [Circle(5), Circle(10), Circle(15)]

# Calculating area and circumference for each circle

for circle in circles:
    area = circle.calculate_area()
    circumference = circle.calculate_circumference()
    print(f"Circle with radius {circle.radius}:")
    print(f"  Area: {area}")
    print(f"  Circumference: {circumference}")
