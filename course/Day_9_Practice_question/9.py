import json

class Customer:
    
    def __init__(self, name, age, address):
        self.name = name
        self.age = age
        self.address = address
    
    def __str__(self):
        return f"Name: {self.name}, Age: {self.age}, Address: {self.address}"
    
    def update_address(self, new_address):
        self.address = new_address
    
    def get_info(self):
        return {"name": self.name, "age": self.age, "address": self.address}
    
    @staticmethod
    def from_json(json_data):
        return Customer(json_data["name"], json_data["age"], json_data["address"])
    
    def to_json(self):
        return self.get_info()

# Store customer data in a list
customers = []

# Read customer data from json file
with open("D:/course/Day_9_Practice_question/customers.json", "r") as file:
    customer_data = json.load(file)
    for customer_info in customer_data:
        customers.append(Customer.from_json(customer_info))

for customer in customers:
    if customer.name == "John Doe":
        customer.update_address("123 Main St")
        break

filename = "D:/course/Day_9_Practice_question/customers.json"
with open(filename, "w") as file:
    json.dump([customer.to_json() for customer in customers], file, indent=4)
    print("Customer data updated successfully!")
