'''
Week 6: Functions Lecture
'''

#prints numbers from 9 to 1
for i in range(9,0, -1):
    print(i)

#printing function
def printThis():
    print("Nik")
    print("Fick")
printThis()

#print 5 times
def printFiveTimes(collegeName):#parameter - holds value
    for i in range(5):
        print(collegeName)
printFiveTimes("Highline College")

#Printing 2 times with values and parameters written different
def printTwoTimes(value, number):
    for i in range(number):
        print(value)
printTwoTimes("Des Moines", 2)

def defaultPrinter(value = "West Seattle", number="2"): #default values
    print(value, number)
defaultPrinter("West Seattle", 2024)#if no number is added the default number is used

#Functions that adds two values together and prints result
def add(numberOne, numberTwo):
    result = numberOne + numberTwo
    print(result)
add(5, 10)


#Ask user for 3 numbers, take the avg of all three using a function
#return the value back to the user

def average(x, y, z):
    result = (x + y + z) / 3
    return result
number1 = float(int(input("Please enter first number: ")))
number2 = float(int(input("Please enter first number: ")))
number3 = float(int(input("Please enter first number: ")))

returnedResult = average(number1, number2, number3)
print("Average is:",returnedResult)