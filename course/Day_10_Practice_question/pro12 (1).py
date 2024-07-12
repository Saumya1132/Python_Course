# write a python program that uses inheritance to represent a hierarchy of shapes (Tringle,Rectangle etc)
class Shape:
    def __init__(self, color):
        self.color = color
    
    def display_color(self):
        print(f"Color: {self.color}")


class Triangle(Shape):
    def __init__(self, color, base, height):
        super().__init__(color)
        self.base = base
        self.height = height
    
    def area(self):
        return 0.5 * self.base * self.height

# Derived class for Rectangle
class Rectangle(Shape):
    def __init__(self, color, width, height):
        super().__init__(color)
        self.width = width
        self.height = height
    
    def area(self):
        return self.width * self.height

if __name__ == "__main__":
    triangle = Triangle("Red", 4, 7)
    triangle.display_color()
    print(f"Triangle Area: {triangle.area()}")

    rectangle = Rectangle("Blue", 2, 9)
    rectangle.display_color()
    print(f"Rectangle Area: {rectangle.area()}")
