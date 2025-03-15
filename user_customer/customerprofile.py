import json

class Customer:
    def __init__(self, name, email, contact_number, address):
        self.name = name
        self.email = email
        self.contact_number = contact_number
        self.address = address

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
        print(f"Name: {self.name}")
        print(f"Email: {self.email}")
        print(f"Contact Number: {self.contact_number}")
        print(f"Address: {self.address}")

    def save_to_file(self):
        data = {
            'name': self.name,
            'email': self.email,
            'contact_number': self.contact_number,
            'address': self.address
        }
        with open('customer_profile.json', 'w') as file:
            json.dump(data, file, indent=4)

    @classmethod
    def load_from_file(cls):
        try:
            with open('customer_profile.json', 'r') as file:
                data = json.load(file)
                return cls(**data)
        except FileNotFoundError:
            return cls("Jane Doe", "jane@example.com", "+1234567890", "123 Main Street")

# Load profile from file or create a new one
customer = Customer.load_from_file()

def main():
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
    main()