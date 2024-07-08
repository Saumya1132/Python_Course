# Area of triangle with breath and height

def main():
    breadth = float(input("Enter the breadth of the triangle: "))
    height = float(input("Enter the height of the triangle: "))
    area = area_of_triangle(breadth, height)
    print("The area of the triangle is:", area)
    
def area_of_triangle(breadth, height):
    area = 0.5 * breadth * height
    return area

main()