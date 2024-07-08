# Initial list of fruits
fruits = ["apple", "orange", "banana", "mango", "blueberries","strawberry", "kiwi", "pineapple"]

try:
    index = int(input("Enter the index of the fruit you want to access: "))

    # Accessing and printing the fruit at the specified index
    if -len(fruits) <= index < len(fruits):
        print("The fruit at index", index, "is", fruits[index])
    else:
        print("Index out of range.")
except ValueError:
    print("Please enter a valid integer index.")
