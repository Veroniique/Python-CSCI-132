'Review - variables/data types'
'input()'
'boolean'
'modulus = %'

name = "123" # String - text/number
print(name)
a = 2 #integer - Whole numbers
b = 2.23 #float = decimal number -.0
converted_name = int(name)
print(converted_name + a)
result = a + b #4.23
print(result)

one = 2
three = 15
two = 25
one = 6 # 2 -> 6
three = one
two = three
three = "123"
four = 7 // two # 7 // 6
four = 11 // two # 11 // 6 = 1
three = "123"
print(int(three) / four)

#Printing out inputs
name = input("What is your name? ")
age = input("What is your age? ")
grade = input("What is your class grade? ")
print(f"My name is {name} and my age is {age} and my grade is {grade}")

#Asking user for two numbers. Add them up and display the result
valueOne = float(input("Please enter the first number: "))
valueTwo = float(input("Please enter the second number: "))
print(f"Results are", valueOne + valueTwo)

#Asking user for age + add 1 year to it
age = int(input("What is your age? "))
print(f"You will be {age + 1} years old next year !")

#Modulus %
#if 2nd number is greater than first, result is always first number
#even number always 0
#odd number always 1
print(5 % 2) #remainder 1
print(5 % 10) #remainder 5

#Booleans - True(yes) and false (no)
#Can be used for math
Happy = True
Sad = False
