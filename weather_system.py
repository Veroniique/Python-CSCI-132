'''
Weather System Project
Date: 1/30/2024
Names: Gamachu Ahmed
       Veronique Fick
Purpose: Ask user temperature input,
        give recommendation what to wear
'''
#User prompts
current_temp = float(input("Enter the current temperature (in Celsius) "))
raining = input("Is it raining today? (yes/no) ")

#Temp conditions that outputs a recommendation
if current_temp < 10:
    print("Please wear a heavy jacket or sweater")
elif 10 <= current_temp <= 25:
    print("Please wear a light jacket or t-shirt")
elif current_temp > 25:
    print("Wear shorts and a tshirt. Don't forget sunscreen!")
else:
    print("Don't forget your sunscreen!")

if raining.lower() == "yes":
    print("You might need an umbrella")
    print("Wear some waterproof shoes")
else:
    print("Enjoy the sunshine!")
