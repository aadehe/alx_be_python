# FAHRENHEIT_TO_CELSIUS_FACTOR = 5 / 9
# CELSIUS_TO_FAHRENHEIT_FACTOR = 9 / 5
#
# def convert_to_celsius(fahrenheit):
#     return (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR
#
# def convert_to_fahrenheit(celsius):
#     return (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32
#
# try:
#     temperature_input = input("Enter the temperature to convert: ")
#     temperature = float(temperature_input)
# except ValueError:
#     raise ValueError("Invalid temperature. Please enter a numeric value.")
#
# unit = input("Is this temperature in Celsius or Fahrenheit? (F/C): ").strip().upper()
#
# if unit == 'F':
#     celsius = convert_to_celsius(temperature)
#     print(f"{temperature}°{unit} is {celsius}°C")
# elif unit == 'C':
#     fahrenheit = convert_to_fahrenheit(temperature)
#     print(f"{temperature}°{unit} is {fahrenheit}°F")
# else:
#     print("Invalid unit. Please enter 'F' for Fahrenheit or 'C' for Celsius.")

FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5

def convert_to_celsius(fahrenheit):
    return (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR

def convert_to_fahrenheit(celsius):
    return (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32

while True:
    try:
        temp = float(input("Enter the temperature to convert: "))
        unit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").strip().upper()
        if unit == "F":
            result = convert_to_celsius(temp)
            print(f"{temp}°{unit} is {result:.2f}°C")
        elif unit == "C":
            result = convert_to_fahrenheit(temp)
            print(f"{temp}°{unit} is {result:.2f}°F")
        else:
            print("Invalid. Enter C or F.")
    except ValueError:
        print("Invalid temperature. Please enter a numeric value.")
        break