'''
2/5/2024
Veronique Fick
Creating a smart energy system for
Home appliances including:
Air Conditioner, TV and Lights
'''
#inputs
room_temp = int(input("What is your current room temperature? "))
people = input("Are there people in the room? (yes or no) ")

#Air conditioner control
if room_temp > 75 and people == "yes":
    print("Air conditioner will be turned on")
elif room_temp < 60 and people == "no":
    print("Air conditioner will be turned off")

#Television control
if people == "yes":
    input("Do you want the Television on? (yes or no) ")
elif people == "no":
    print("Turning off TV")

#Lights control
if people == "yes":
    num_people = int(input("How many people are in the room? "))
elif num_people > 1:
    print("Turning on lights")
elif num_people <= 0:
    print("Turning off lights")


