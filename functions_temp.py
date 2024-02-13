'''
Using functions to convert celsius to fahrenheit and vice versa
Date: 12 February 2024
'''
print("Which conversion would you like to perform? ")
print("1. Celsius to Fahrenheit")
print("2. Fahrenheit to Celsius")
num = int(input("Enter 1 or 2: "))
getUserTemp = float(int(input("Enter temperature: ")))

#converts c to f
def celsius_to_fahrenheit(celsius):
    fahrenheit = (celsius * 9 / 5) + 32
    return fahrenheit

#converts f to c
def fahrenheit_to_celsius(fahrenheit):
    celsius = (fahrenheit / 32) * 59
    return celsius

#conditional checkers to see valid inputs, function then executes
if num == 1:
    result = celsius_to_fahrenheit(getUserTemp)
    print(f"{getUserTemp} is equal to {result}")
elif num == 2:
    result = fahrenheit_to_celsius(getUserTemp)
    print(f"{getUserTemp} is equal to {result}")
else:
    print("Invalid input. Only enter 1 or 2")