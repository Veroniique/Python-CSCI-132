'''
Assignment - File Diary
6 February 2024
Group: Naweed Karimi and Veronique Fick
'''
#Imported date/time library
from datetime import datetime

while True:
    #Task 1+2 - User options to pick from
    print("Welcome to your Personal Diary Management System!\n")

    print("1. Write a new diary entry")
    print("2. Read the latest diary entry")
    print("3. Read all diary entries")
    print("4. Delete the latest diary entry")
    print("5. Exit\n")

    try:
        user_input = int(input("Choose an option between 1-5: "))

        #Task 3 - Prompt user to enter date and an entry
        #using datetime library functions for formatting
        if user_input == 1:
            user_date = input("Enter today's date (e.g., 2024-03-06): ")
            try:
                #imported date format
                datetime.strptime(user_date, "%Y-%m-%d")
                user_entry = input("Add your entry for today: ")
                #prints diary entry to diary.txt
                formatted_entry = f"Date: {user_date}\n{user_entry}\n"
                with open("diary.txt", "a") as diary_file:
                    diary_file.write(formatted_entry)
                print("Your entry has been added!")
            except ValueError:
                print("Invalid format. Use the YYYY-MM-DD format for the date")

        #Task 4 -Reading latest entry
        elif user_input == 2:
            try:
                #read all entries in diary.txt
                with open("diary.txt", "r") as diary_file:
                    entries = diary_file.readlines()
                #Check for entries
                if entries:
                    print("Latest entry: ")
                    print(entries[-1])
                else:
                    print("There are no entries. Please use numbers 1 - 5")
            except FileNotFoundError:
                print("No entry has been found. Try a new entry.")

        #Task 5 - Reading all entries from diary.txt
        elif user_input == 3:
            try:
                with open("diary.txt", "r") as diary_file:
                    entries = diary_file.read()
                if entries:
                    print("Here's all your diary entries: ")
                    print(entries)
                else:
                    print("There are no entries.")
            except FileNotFoundError:
                print("No entries found. Please add a new entry.")

        #Task 6 - Deleting latest entry
        elif user_input == 4:
            try:
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
                    print("No entry was found. Please use numbers 1 - 5")
            except FileNotFoundError:
                print("No entries found. Please add a new entry.")

        #Task 7 - Exit Program
        elif user_input == 5:
            print("Thank you for using your Daily Diary! Keep journaling!")
            break
        else:
            ("Invalid input. Please use numbers 1 - 5")
    except ValueError:
        print("Invalid input. Please use numbers 1 - 5")
