# create a class hierarchy to represent different types of electonics(phone,laptop)with their attributes.
class Electronics:
    def __init__(self, brand, price):
        self.brand = brand
        self.price = price

    def display_info(self):
        print(f"Brand: {self.brand}")
        print(f"Price: ${self.price}")

class Phone(Electronics):
    def __init__(self, brand, price, screen_size, battery_capacity):
        super().__init__(brand, price)
        self.screen_size = screen_size
        self.battery_capacity = battery_capacity

    def display_info(self):
        super().display_info()
        print(f"Screen Size: {self.screen_size} inches")
        print(f"Battery Capacity: {self.battery_capacity} mAh")

class Laptop(Electronics):
    def __init__(self, brand, price, ram, storage):
        super().__init__(brand, price)
        self.ram = ram
        self.storage = storage

    def display_info(self):
        super().display_info()
        print(f"RAM: {self.ram} GB")
        print(f"Storage: {self.storage} GB")

# Example usage
if __name__ == "__main__":
    phone = Phone("oppo", 999, 6.4, 4000)
    laptop = Laptop("Dell", 1200, 16, 512)

    print("Phone Details:")
    phone.display_info()

    print("\nLaptop Details:")
    laptop.display_info()
