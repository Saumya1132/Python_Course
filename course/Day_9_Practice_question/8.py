# class representing car with attributes like make ,model and year

class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
    
    def get_car_info(self):
        return f"Make: {self.make}, Model: {self.model}, Year: {self.year}"
    
car = Car("Toyota", "Camry", 2020)
print(car.get_car_info()) 
    
