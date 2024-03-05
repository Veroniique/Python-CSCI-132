#Pair Assignment: Files 3/4/2024

#Task 1: Reading from a file
content=open("sample.txt", "r")
file=content.read()
print(file)
content.close()

#Task 2: Writing to a file
user_input = input("Enter your new sentence: ")
string = "\n" + user_input
content2 = open("sample.txt","a")
file2 = content2.write(string)
print(file2)
content2.close()

#Task 3: Appending to a File
user_new_sentence = input("Enter your new sentences: ")
string = "\n" + user_new_sentence
content2 = open("sample.txt","a")
file2 = content2.write(string)
print(file2)
content2.close()

#Task 4: Line-by-line reading
variable = open("sample.txt", "r")
new_variable = variable.readlines()

for i, line in enumerate(new_variable, 1):
    print(f"Line {i}: {line}", end="")
variable.close()

#Task 5: counting words
with open("sample.txt", "r") as file:
    content = file.read()
    words = content.split()
    print(f"\nTotal words: {len(words)}")

#Task 6: Make a copy
with open("sample.txt", "r") as original_file:
    with open("sample_copy.txt", "w") as copy_file:
        copy_file.write(original_file.read())

#Task 7: Deleting Lines
del_num = int(input("Enter line number you want to delete: "))
with open("sample.txt", "r") as file:
    lines = file.readlines()
with open("sample.txt", "w") as file:
    for index, line in enumerate(lines, 1):
        if index != del_num:
            file.write(line)

#Task 8: Word lookup
word_search = input("Enter a word you want to search for: ")
with open("sample.txt", "r") as file:
    for line_number, line in enumerate(file, 1):
        if word_search in line:
            print(f"Line {line_number}: {line}", end="")