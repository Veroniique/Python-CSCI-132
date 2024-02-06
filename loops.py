import time
import random

#number 1 - countdown timer
time.sleep(1)
x = 10
while x > 0:
    print(x, "\nLiftoff")
    x -= 1

#number 2 - multiplication table
start = int(input("What's the start of the range: "))
end = int(input("What's the end of the range: "))

for i in range(start, end):
    print("Results are:")
    for j in range(start, end):
        x = i * j
        print(f"{i}*{j}={x}")

#number 3 - guess the number game
secret_number = random.randint(1, 100)

while True:
    guessed_num = int(input("Enter a number between 1 - 100: "))
    if guessed_num < secret_number:
        print("Too low. Do it again")
    elif guessed_num > secret_number:
        print("Too high. Go again.")
    else:
        print("You guessed it")
        break
'''
#number 4 - interest calculator
amount = int(input())
rate 
num_years
'''