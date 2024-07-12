import math

class Shape:
    def area(self):
        pass 
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    def area(self):
        return math.pi * self.radius ** 2

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

if __name__ == "__main__":
    circle = Circle(4)
    print(f"Circle Area: {circle.area():.2f}")

    rectangle = Rectangle(5, 7)
    print(f"Rectangle Area: {rectangle.area()}")
