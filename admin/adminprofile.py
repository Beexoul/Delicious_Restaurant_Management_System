class Admin:
    def __init__(self, name, address, contact_number, bio):
        self.name = name
        self.address = address
        self.contact_number = contact_number
        self.bio = bio

    def update_profile(self):
        print("\n--- Update Admin Profile ---")
        name = input(f"Enter new name [{self.name}]: ") or self.name
        address = input(f"Enter new address [{self.address}]: ") or self.address
        contact_number = input(f"Enter new contact number [{self.contact_number}]: ") or self.contact_number
        bio = input(f"Enter new bio [{self.bio}]: ") or self.bio

        self.name = name
        self.address = address
        self.contact_number = contact_number
        self.bio = bio

        print("\nProfile updated successfully!\n")

    def display_profile(self):
        print("\n--- Admin Profile ---")
        print(f"Name: {self.name}")
        print(f"Address: {self.address}")
        print(f"Contact Number: {self.contact_number}")
        print(f"Bio: {self.bio}")

# Initialize Admin profile with some default values
admin = Admin("Beexoul", "Butwal", "+977980000000", "Not every closed door is closed. Push")

def main():
    while True:
        print("\n1. View Profile")
        print("2. Update Profile")
        print("3. Back to Main Menu")

        choice = input("Enter your choice: ")

        if choice == "1":
            admin.display_profile()
        elif choice == "2":
            admin.update_profile()
        elif choice == "3":
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
