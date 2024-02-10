'''
2/5/2024
Veronique Fick
Creating a smart energy system for
Home appliances including:
Air Conditioner, TV and Lights
'''

while True:
#inputs
    room_temp = int(input("What is your current room temperature? "))
    people = input("Are there people in the room? (yes or no) ")

    #Air conditioner control
    if room_temp > 75 and people == "yes":
        print("Air conditioner will be turned on")
    elif room_temp < 60 and people == "no":
        print("Air conditioner will be turned off")

    #Television control
    if people.lower() == "yes":
        tv_input = input("Do you want the Television on? (yes or no) ")
        if tv_input.lower() == "yes":
            print("Turning on TV")
        else:
            print("TV staying turned off")
    elif people.lower() == "no":
        print("Turning off TV")

    #Lights control
    if people.lower() == "yes":
        num_people = int(input("How many people are in the room? "))
        if num_people > 1:
            print("Turning on lights")
        elif num_people <= 0:
            print("Turning off lights")
        else:
            print("No one is in the room")
    elif people.lower() == "no":
        print("No one is in the room")

#updating room conditions
    while True:
        update = input("Do you want to update the room conditions?(yes/no) ")
        if update.lower() == "yes":
            #Handles all conditions
            print("Room conditions will be updated.")
            break
        elif update.lower() == "no":
            print("Leaving program. Thank you for your input.")
            break
    if update.lower() == "no":
        break