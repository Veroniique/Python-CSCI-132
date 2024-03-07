'''
Assignment - File Diary
6 February 2024
Group: Naweed Karimi and Veronique Fick

TODO: - Error handling for all files
      - Add everything into a loop to keep repeating until program exists
      - Add an exit message for the end of the program
'''
#Imported date/time library
from datetime import datetime

#Task 1+2 - User options to pick from
print("Welcome to your Personal Diary Management System!\n")

print("1. Write a new diary entry")
print("2. Read the latest diary entry")
print("3. Read all diary entries")
print("4. Delete the latest diary entry")
print("5. Exit\n")
user_input = int(input("Choose an option between 1-5: "))

#Task 3 - Prompt user to enter date and an entry
#using datetime library functions for formatting
if user_input == 1:
    while True:
        user_date = input("Enter today's date (e.g., 2024-03-06): ")
        current_date = datetime.now()
        formatted_date = current_date.strftime("%Y-%m-%d")

        #loop that checks if date has been added correctly
        if user_date == formatted_date:
            print("Today's date has been added")
            # User adds detail for their entry
            user_entry = input("Make a diary entry for today: ")
            # Format to use for diary entry
            formatted_entry = f"Date: {user_date}\n{user_entry}\n"
            # Save entry to diary.txt file
            with open("diary.txt", "a") as diary_file:
                diary_file.write(formatted_entry)
            break
        else:
            try:
                datetime.strptime(user_date, "%Y-%m-%d")
                print("Date was added")
                # User adds detail for their entry
                user_entry = input("Make a diary entry for today: ")
                # Format to use for diary entry
                formatted_entry = f"Date: {user_date}\n{user_entry}\n"
                # Save entry to diary.txt file
                with open("diary.txt", "a") as diary_file:
                    diary_file.write(formatted_entry)
                break
            except ValueError:
                print("Invalid date format. Please use the YYYY-MM-DD format")

#Task 4 -Reading latest entry
if user_input == 2:
    #read all entries in diary.txt
    with open("diary.txt", "r") as diary_file:
        entries = diary_file.readlines()

    #Check for entries
    if entries:
        print("Latest entry: ")
        print(entries[-1])
    else:
        print("There are no entries")

#Task 5 - Reading all entries from diary.txt
if user_input == 3:
    content=open("diary.txt", "r")
    file=content.read()
    print(file)
    content.close()

#Task 6 - Deleting latest entry
if user_input == 4:
    #Read all entries from file
    with open("diary.txt", "r") as diary_file:
        entries = diary_file.readlines()

    #Check if there are entries
    if entries:
        #Remove entry if found
        entries.pop()

        #Rewrite left over entries back to file
        with open("diary.txt", "w") as diary_file:
            for entry in entries:
                diary_file.write(entry)

        print("Latest entry has been deleted")
    else:
        print("No entry was found")

#Task 7 - Error handling for files

#Task 8 - Exit Program
