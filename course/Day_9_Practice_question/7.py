# using class calculate area and perimeter of the rectangle

class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width
        
    def calculate_area(self):
        return self.length * self.width
    
    def calculate_perimeter(self):
        return 2 * (self.length + self.width)
    
rectangle = Rectangle(5, 10)

area = rectangle.calculate_area()
perimeter = rectangle.calculate_perimeter()

print("Area:", area)
print("Perimeter:", perimeter)