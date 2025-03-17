import json
import os

class Customer:
    def __init__(self, name, email, contact_number, address, username):
        self.name = name
        self.email = email
        self.contact_number = contact_number
        self.address = address
        self.username = username.lower() 

    def update_profile(self):
        print("\n--- Update Customer Profile ---")
        self.name = input(f"Enter new name [{self.name}]: ") or self.name
        self.email = input(f"Enter new email [{self.email}]: ") or self.email
        self.contact_number = input(f"Enter new contact number [{self.contact_number}]: ") or self.contact_number
        self.address = input(f"Enter new address [{self.address}]: ") or self.address

        self.save_to_credentials()
        print("\nProfile updated successfully!\n")

    def display_profile(self):
        print("\n--- Customer Profile ---")
        print(f"Username: {self.username}")
        print(f"Name: {self.name}")
        print(f"Email: {self.email}")
        print(f"Contact Number: {self.contact_number}")
        print(f"Address: {self.address}")

    def save_to_credentials(self):
        credentials_file = os.path.join("./User_Data", "customer_credentials.json")
        credentials = load_json_file(credentials_file)
        credentials[self.username] = {
            "name": self.name,
            "email": self.email,
            "contact_number": self.contact_number,
            "address": self.address,
            "password": credentials.get(self.username, {}).get("password", ""),
            "role": "customer"
        }
        save_json_file(credentials_file, credentials)

    @classmethod
    def load_from_file(cls, username):
        credentials_file = os.path.join("./User_Data", "customer_credentials.json")
        credentials = load_json_file(credentials_file)
        username = username.lower()
        
        if username in credentials:
            data = credentials[username]
            return cls(data["name"], data["email"], data["contact_number"], data["address"], username)
        else:
            print("\n--- Set Up Your Profile ---")
            name = input("Enter your name: ").strip()
            while not name:
                print("Name cannot be empty!")
                name = input("Enter your name: ").strip()
            
            email = input("Enter your email: ").strip()
            while not email:
                print("Email cannot be empty!")
                email = input("Enter your email: ").strip()
            
            contact_number = input("Enter your contact number: ").strip()
            while not contact_number:
                print("Contact number cannot be empty!")
                contact_number = input("Enter your contact number: ").strip()
            
            address = input("Enter your address: ").strip()
            while not address:
                print("Address cannot be empty!")
                address = input("Enter your address: ").strip()
            
            customer = cls(name, email, contact_number, address, username)
            customer.save_to_credentials()
            print("Profile created successfully!")
            return customer

def load_json_file(filename):
    try:
        with open(filename, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return {}

def save_json_file(filename, data):
    os.makedirs(os.path.dirname(filename), exist_ok=True)
    with open(filename, 'w') as file:
        json.dump(data, file, indent=4)

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

if __name__ == "__main__":
    print("This module is intended to be imported by main.py. Please run main.py instead.")

#done