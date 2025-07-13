# Create a class for the account

import time
import os

def clear_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')

Users = []

class Info:
    def __init__(self, first_name, last_name, email, password, status="inactive"):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.password = password
        self.status = status

    def display(self):
        print(f"The first name: {self.first_name}")
        print(f"The last name: {self.last_name}")
        print(f"The email: {self.email}")
        print(f"The status: {self.status}")

def create_user():
    first_name = input("Enter your first name: ")
    last_name = input("Enter your last name: ")
    email = input("Enter the email: ")
    password = input("Enter the password: ")
    return Info(first_name, last_name, email, password)

def choices():
    while True:
        clear_terminal()
        print("WELCOME TO MANAGEMENT!")
        print("\nChoose an action: ")
        print("""1. Add new user
2. Display all users
3. Exit
""")
        choice = input("Enter your choice: ")
        
        if choice == "1":
            Users.append(create_user())
            print("User added successfully!")
            time.sleep(2)
        
        elif choice == "2":
            clear_terminal()
            print("Displaying all users:")
            if not Users:
                print("No users yet.")
            else:
                for user in Users:
                    user.display()
                    print("_ " * 15)
            input("\nPress Enter to return to the menu...")

        elif choice == "3":
            print("Goodbye! Have a great day!")
            break
            
        else:
            print("Wrong choice, try again!")
            time.sleep(2)

choices()