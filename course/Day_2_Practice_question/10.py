# Area and the circumference of the circle

def main():
    radius = float(input("Enter the radius of the circle: "))
    area = area_of_circle(radius)
    circumference = circumference_of_circle(radius)
    print("The area of the circle is:", area)
    print("The circumference of the circle is:", circumference)

def area_of_circle(radius):
    area = 3.14 * radius * radius
    return area

def circumference_of_circle(radius):
    circumference = 2 * 3.14 * radius
    return circumference

main()
