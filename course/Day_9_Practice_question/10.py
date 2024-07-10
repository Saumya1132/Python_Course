# Person class to keep track of name age and address

class Person:
    def __init__(self, name, age, address):
        self.name = name
        self.age = age
        self.address = address
        
    def display_info(self):
        print(f"Name: {self.name}, Age: {self.age}, Address: {self.address}")
        
    def __str__(self):
        return f"Name: {self.name}, Age: {self.age}, Address: {self.address}"
    
    def to_json(self):
        return f'{{"name": "{self.name}", "age": {self.age}, "address": "{self.address}" }}'
        
    def update_address(self, new_address):
        self.address = new_address

# Example usage:
person = Person("Alice", 28, "456 Elm St")
person.display_info()  
print(person)  
print(person.to_json()) 

        
    