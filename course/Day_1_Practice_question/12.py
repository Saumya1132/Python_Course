# celcius to fahrenheit

def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

celsius = float(input("Enter temperature in Celsius: "))
fahrenheit = celsius_to_fahrenheit(celsius)
print(f"{celsius} degrees Celsius is equal to {fahrenheit} degrees Fahrenheit.")