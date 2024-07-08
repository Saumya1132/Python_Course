# Area the circle

def main():
    radius = float(input("Enter the radius of the circle: "))
    area = area_of_circle(radius)
    print("The area of the circle is:", area)

def area_of_circle(radius):
    area = 3.14 * radius * radius
    return area

main()
