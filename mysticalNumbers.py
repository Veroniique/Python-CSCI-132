print("Welcome to the mystical land of Pythoria!")

#Task1
magic_number = int(input("Enter your favorite integer number: "))
magic_word = str(input("Enter a secret word: "))

#Task2
spell_one = magic_word * magic_number
print("The first spell creates: ", spell_one)

#Task3
spell_two = str(magic_number) + str(len(magic_word))
print("The second spell creates: ", spell_two)

#Task 4
secret_message = spell_one + spell_two
print("The secret message is: ", secret_message)