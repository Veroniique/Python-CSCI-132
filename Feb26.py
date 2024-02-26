'''
Lists + Dictionaries - 26 Feb
'''

#defining a list
colors = ["orange", "red", "yellow", "pink", "blue", "black"]

#printing a list
print(colors)

#adding to a list with append
colors.append("green")
colors.append("purple")
print(colors)

#print in a loop and have spaces in between each other
#for i in colors:
#    print(i, end=' ')

#print colors in a loop that start with a certain letter
for i in colors:
    if i.startswith("b"):
        print(i, end=' ')

#replace colors by index number
colors[4] = "white"
print(colors)

#deletes a color by index
del colors[1]
print(colors)

#new list
chocolates = ["dark","coco"]

#add value in between colors
chocolates.insert(1, "natural")
print(chocolates)

#new list - min, max, len, sum
#len - returns length of list (# of elements)
#min - returns min
#max - returns max
#sum - adds everything together
#sorted - sorts numbers
numbers = [5,2,1,6,5,4,8,9,7,8,6,9,8,1,2,-1,5,6,98]

#stores sorted number list
numbers = sorted(numbers)
print(max(numbers))
print(sorted(numbers))

#searches for number, if it exists, it will print the statement
if 2 in numbers:
    print("Number 2 exists in the list")

colorz = ["red", "Yellow", "Black"]
for item in colorz:
    if "black".lower() in item.lower():
        print("Black in colors")

#combining lists together
colorsOne = ["red","Yellow","Black"]
colorsTwo = ["Blue","Grey","purple"]
colorsThree = colorsOne + colorsTwo
print(colorsThree)

#takes length of colorsOne, takes away 1 (which equals to 2)
#then it prints the 2nd index in the list which is Black
print(colorsOne[len(colorsOne) - 1])

#slicing
colorsFour = ["red", "Yellow", "Black", "grey", "green", "Blue"]
newColors = colors[1:]
print(newColors)