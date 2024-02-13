#Functions Pair Assignment - 2/12/2024
#Question 1
def greet():
    print("Hello! Welcome to Python class.")
greet()

#Question 2
def personal_greet():
    name = input("Please enter your name: ")
    return name
print("Hello", personal_greet())

#Question 3
def calculate_area():
    length = int(input("Enter length: "))
    width = int(input("Enter width: "))
    area = length * width
    return area
print("Area:", calculate_area())

#Question 4
def describe_pet(pet_name, animal_type="dog"):
    message = f"{pet_name} is a fluffy {animal_type}."
    return message
print(describe_pet("Bob"))

#Question 5
def convert_temperature():
    getUserTemp = float(int(input("What temperature do you want to convert from C to F: ")))
    Farhrenheit = (getUserTemp * 9 / 5) + 32
    return Farhrenheit
print(f"Your converted temp is: {convert_temperature()}'F")