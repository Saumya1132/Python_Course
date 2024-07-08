# Area of Rectangle
def rectangle_area(l, w):
    area = l * w
    return area

l = float(input("Enter the length of rectangle: "))
w = float(input("Enter the width of rectangle: "))

area = rectangle_area(l, w)

print("The area of the rectangle is:", area)
