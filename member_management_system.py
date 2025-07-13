# Member Management System

import time
import os

def clear_terminal():
    """Clears the terminal screen based on the operating system."""
    os.system('cls' if os.name == 'nt' else 'clear')

class Member:
    """Represents a member with personal information and status."""
    
    def _init_(self, first_name, last_name, id, status="Inactive"):
        """
        Initialize a new member.
        
        Args:
            first_name (str): Member's first name
            last_name (str): Member's last name
            id (str): Unique identifier
            status (str): 'Active' or 'Inactive' (default: 'Inactive')
        """
        self.first_name = first_name
        self.last_name = last_name
        self.id = id
        self.status = status

    def display(self):
        """Displays the member's information in a formatted way."""
        print("\n=== Member Information ===")
        print(f"First Name: {self.first_name}")
        print(f"Last Name: {self.last_name}")
        print(f"ID: {self.id}")
        print(f"Status: {self.status}")
        print("=" * 25)

def create_member():
    """Creates a new member by gathering user input."""
    print("\n=== Add New Member ===")
    first_name = input("Enter the first name: ").strip()
    last_name = input("Enter the last name: ").strip()
    id = input("Enter the ID: ").strip()
    
    while True:
        status = input("Enter the status: \n1. Active \n2. Inactive \nChoice: ").strip()
        if status in ("1", "2"):
            status = "Active" if status == "1" else "Inactive"
            break
        print("Invalid input. Please enter 1 or 2.")
    
    return Member(first_name, last_name, id, status)

def search_members(members):
    """Searches members based on different criteria."""
    clear_terminal()
    print("\n=== Search Members ===")
    print("Search by:")
    print("1. ID")
    print("2. First name")
    print("3. Status")

    while True:
        search_choice = input("Enter your choice (1-3): ").strip()
        if search_choice in ("1", "2", "3"):
            break
        print("Invalid choice. Please enter 1, 2, or 3.")

    found_members = []

    if search_choice == "1":
        search_id = input("Enter the ID to search: ").strip()
        for member in members:
            if member.id == search_id:
                found_members.append(member)
    elif search_choice == "2":
        search_name = input("Enter the first name to search: ").strip().lower()
        for member in members:
            if member.first_name.lower() == search_name:
                found_members.append(member)
    elif search_choice == "3":
        while True:
            search_status = input("Enter the status to search (Active/Inactive): ").strip().capitalize()
            if search_status in ("Active", "Inactive"):
                break
            print("Invalid status. Please enter 'Active' or 'Inactive'.")
        
        for member in members:
            if member.status == search_status:
                found_members.append(member)

    display_search_results(found_members)

def display_search_results(members):
    """Displays search results with appropriate messaging."""
    clear_terminal()
    if members:
        print(f"\n=== Found {len(members)} Member(s) ===")
        for member in members:
            member.display()
    else:
        print("\nNo members found matching your criteria.")
    time.sleep(3)

def main_menu():
    """Displays the main menu and handles user choices."""
    members = []
    
    while True:
        clear_terminal()
        print("\n=== Member Management System ===")
        print("1. Add a member")
        print("2. View all members")
        print("3. Search for a member")
        print("4. Exit")
        
        choice = input("\nEnter your choice (1-4): ").strip()
        
        if choice == "1":
            clear_terminal()
            members.append(create_member())
            print("\nMember added successfully!")
            time.sleep(2)
        
        elif choice == "2":
            clear_terminal()
            if members:
                print("\n=== All Members ===")
                for member in members:
                    member.display()
            else:
                print("\nNo members in the system yet.")
            input("\nPress Enter to continue...")
            
        elif choice == "3":
            if members:
                search_members(members)
            else:
                clear_terminal()
                print("\nNo members to search. Please add members first.")
                time.sleep(2)
                
        elif choice == "4":
            print("\nThank you for using the Member Management System. Goodbye!")
            time.sleep(2)
            break
            
        else:
            print("\nInvalid choice. Please enter a number between 1 and 4.")
            time.sleep(2)

if __name__ == "__main__":
    main_menu()