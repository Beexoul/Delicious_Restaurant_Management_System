import json
import os

class Customer:
    def __init__(self, name, email, contact_number, address, username):
        self.name = name
        self.email = email
        self.contact_number = contact_number
        self.address = address
        self.username = username 

    def update_profile(self):
        print("\n--- Update Customer Profile ---")
        self.name = input(f"Enter new name [{self.name}]: ") or self.name
        self.email = input(f"Enter new email [{self.email}]: ") or self.email
        self.contact_number = input(f"Enter new contact number [{self.contact_number}]: ") or self.contact_number
        self.address = input(f"Enter new address [{self.address}]: ") or self.address

        self.save_to_file()
        print("\nProfile updated successfully!\n")

    def display_profile(self):
        print("\n--- Customer Profile ---")
        print(f"Username: {self.username}")
        print(f"Name: {self.name}")
        print(f"Email: {self.email}")
        print(f"Contact Number: {self.contact_number}")
        print(f"Address: {self.address}")

    def save_to_file(self):
        data = {
            'name': self.name,
            'email': self.email,
            'contact_number': self.contact_number,
            'address': self.address,
            'username': self.username
        }
        filename = f"./User_Data/customer_profile_{self.username}.json"
        with open(filename, 'w') as file:
            json.dump(data, file, indent=4)

    @classmethod
    def load_from_file(cls, username):
        filename = f"./User_Data/customer_profile_{username}.json"
        if os.path.exists(filename):
            with open(filename, 'r') as file:
                data = json.load(file)
                return cls(**data)
        else:
            print("\n--- Set Up Your Profile ---")
            name = input("Enter your name: ")
            while not name.strip():
                print("Name cannot be empty!")
                name = input("Enter your name: ")
            
            email = input("Enter your email: ")
            while not email.strip():
                print("Email cannot be empty!")
                email = input("Enter your email: ")
            
            contact_number = input("Enter your contact number: ")
            while not contact_number.strip():
                print("Contact number cannot be empty!")
                contact_number = input("Enter your contact number: ")
            
            address = input("Enter your address: ")
            while not address.strip():
                print("Address cannot be empty!")
                address = input("Enter your address: ")
            
            customer = cls(name, email, contact_number, address, username)
            customer.save_to_file()
            print("Profile created successfully!")
            return customer

def main(logged_in_username):
    customer = Customer.load_from_file(logged_in_username)
    
    while True:
        print("\n1. View Profile")
        print("2. Update Profile")
        print("3. Back to Main Menu")

        choice = input("Enter your choice: ")

        if choice == "1":
            customer.display_profile()
        elif choice == "2":
            customer.update_profile()
        elif choice == "3":
            break
        else:
            print("Invalid choice. Please try again.")