# a csv file with product details manage the such as name price and quantity using product classs

import csv

class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity
        
    def update_quantity(self, new_quantity):
        self.quantity = new_quantity
    
    def calculate_total_cost(self):
        return self.price * self.quantity
    
    def __str__(self):
        return f"Product Name: {self.name}, Price: {self.price}, Quantity: {self.quantity}"
    
    @staticmethod
    def from_csv_row(row):
        name, price, quantity = row
        return Product(name, float(price), int(quantity))
    
    def to_csv_row(self):
        return [self.name, self.price, self.quantity]

# Read product data from a CSV file
products = []

filename = "D:\course\Day_9_Practice_question\products.csv"
with open(filename, mode='r') as file:
    csv_reader = csv.reader(file)
    next(csv_reader)  # Skip header row
    for row in csv_reader:
        products.append(Product.from_csv_row(row))

# Update quantity of a specific product
for product in products:
    if product.name == "ProductA":
        product.update_quantity(50)
        break

# Write updated product data back to CSV file
with open(filename, mode='w', newline='') as file:
    csv_writer = csv.writer(file)
    csv_writer.writerow(["name", "price", "quantity"])  # Write header row
    for product in products:
        csv_writer.writerow(product.to_csv_row())

print("Product data updated successfully!")
