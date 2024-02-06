if False:
    print("Nik")
    if 2 == 3:
        print("Fick")
    else:
        print("do not print")
        if True:
            print("Always print")
else:
    print("test")

#while loops
#ranges
range(10) #gives values 0 - 9
#range(start, end) - gives range of 5-10
range(5, 10) #5 - 9
range(90, 91) #90
range(90, 100) #90 - 99
# range(start, end, step)
range(5, 25, 5) #starting point, ending point and incrementing
range(5 , 25, 5) #5, 10, 15, 20 (increments by 5s)
range(20, 10, -1) #20, 19, 18, 17, 16, 15, 14, 13, 12, 11

#for loop
for i in range(10):
    print("Nik") #prints Nik 10 times
print("Fick")

for nothing in range(100, 98, -1):
    print(nothing)
'''
Write a program that asks user for two numbers (range) inclusive and 
then prints all the even numbers in that range
'''
start = int(input("Please enter first number "))
end = int(input("Please enter second number "))

for i in range(start, end+1):
    if i % 2 == 0:
        print(i)

#while loops
start = 2
end = 4
while start < end:
    print("2 is less than 4")
    start = start + 1 #increments by 1

'''
Write a program that asks the user for a number and tells
the user if that number is even or odd. Keep asking the 
user for the number. Stop if the user enters -1
'''
while True:
    user_num = int(input("Enter a number "))
    if user_num == -1:
        print("Thank you for using our program, Bye.")
        break
    elif user_num % 2 == 0:
        print(f"{user_num} is even")
    else:
        print(f"{user_num} is odd")

#nested for loops
total = 0
for i in range(1):
    for j in range(2):
        print(f"i = {i}, j = {j}")
        total = total + 1 # total += 1 can also work
        print(f"total = {total}")














