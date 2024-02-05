print("You are in a mysterious forest.")
print("Do you take the path to the dark cave or walk towards the old bridge?")
option1 = input("cave or bridge? ")
if option1.lower() == "cave":
    print("You cautiously enter the cave."
          "It's dark and eerie."
          "Do you proceed further or go back?"
          "proceed or back")
    option2 = input("proceed or go back ")
    if option2.lower() == "proceed":
        option2 = True
        print("You found the treasure")
    else:
        print("Go back to the start")
elif option1.lower() == "bridge":
        print("You approach the old bridge."
              "It looks fragile."
              "Do you cross it or return to the forest"
              "cross or return?")
        option3 = input("cross or return ")
        if option3.lower() == "cross":
            option3 = True
            print("You made it to the end!")
        else:
            print("Go back to the start")



