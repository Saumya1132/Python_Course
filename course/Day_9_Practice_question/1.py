# using class create basic calculator functions 

class calculator:
    
    def add(self, num1, num2):
        self.num1 = num1
        self.num2 = num2
        addition = self.num1 + self.num2
        return addition
    def subtract(self, num1, num2):
        self.num1 = num1
        self.num2 = num2
        subtraction = self.num1 - self.num2
        return subtraction
    def multiply(self, num1, num2):
        self.num1 = num1
        self.num2 = num2
        multiplication = self.num1 * self.num2
        return multiplication
    def divide(self, num1, num2):
        self.num1 = num1
        self.num2 = num2
        if self.num2 == 0:
            return "Error: Division by zero"
        division = self.num1 / self.num2
        return division

calc = calculator()
print(calc.add(5, 7))
print(calc.subtract(10, 3))
print(calc.multiply(2, 8))
print(calc.divide(16, 4))
    
        
        