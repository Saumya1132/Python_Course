# given  a json file with product details(name,price,quantity),create a product class with encapsulated attributes.
import json

class Product:
    def __init__(self, name, price, quantity):
        self.name = name        
        self.price = price       
        self.quantity = quantity 

    def display_info(self):
        print(f"Name: {self.name}")
        print(f"Price: ${self.price}")
        print(f"Quantity: {self.quantity}")

def read_products_from_json(file_path):
    products = []
    with open(file_path, 'r') as json_file:
        data = json.load(json_file)
        for item in data['products']:
            product = Product(item['name'], item['price'], item['quantity'])
            products.append(product)
    return products
if __name__ == "__main__":

    products = read_products_from_json('C:\python\Day-10\product.json')
    for product in products:
        product.display_info()
        print()
