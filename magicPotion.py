'Magic Potion recipe that calculates your ingredients'

recipe = "Magic Potion Recipe Calculator"
print("Welcome to my " + recipe + "\n")

#Ingredient amounts
water = 0.5
dust = 10
sunflower = 3

#User inputs
pot_size = float(input("How many liters do you want for your pot: "))
plants = int(input("How many plants do you want to grow with your potion: "))

#calculate ratio of plants to petals
petals = plants / 2 * 3

print("\n")
print("Crystal Water: " + str(pot_size * 0.5) + " liters")
print("Moon Dust: " + str(plants * 10) + " grams")
print("Sunflower Petals: " + str(petals) + " petals \n")

print("Mix all the ingredients together under a full moon for best results")
