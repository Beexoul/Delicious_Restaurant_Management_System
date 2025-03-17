import json

class Manager:
    def __init__(self, name, department, contact_number, bio):
        self.name = name
        self.department = department
        self.contact_number = contact_number
        self.bio = bio

    def update_profile(self):
        print("\n--- Update Manager Profile ---")
        self.name = input(f"Enter new name [{self.name}]: ") or self.name
        self.department = input(f"Enter new department [{self.department}]: ") or self.department
        self.contact_number = input(f"Enter new contact number [{self.contact_number}]: ") or self.contact_number
        self.bio = input(f"Enter new bio [{self.bio}]: ") or self.bio

        self.save_to_file()
        print("\nProfile updated successfully!\n")

    def display_profile(self):
        print("\n--- Manager Profile ---")
        print(f"Name: {self.name}")
        print(f"Department: {self.department}")
        print(f"Contact Number: {self.contact_number}")
        print(f"Bio: {self.bio}")

    def save_to_file(self):
        data = {
            'name': self.name,
            'department': self.department,
            'contact_number': self.contact_number,
            'bio': self.bio
        }
        with open('./User_Data/manager_profile.json', 'w') as file:
            json.dump(data, file, indent=4)

    @classmethod
    def load_from_file(cls):
        try:
            with open('./User_Data/manager_profile.json', 'r') as file:
                data = json.load(file)
                return cls(**data)
        except FileNotFoundError:
            return cls("Saroj Neupane", "Manager", "+977 9871234560", " Living my best life, Always learning.")

manager = Manager.load_from_file()

def main():
    while True:
        print("\n1. View Profile")
        print("2. Update Profile")
        print("3. Back to Main Menu")

        choice = input("Enter your choice: ")

        if choice == "1":
            manager.display_profile()
        elif choice == "2":
            manager.update_profile()
        elif choice == "3":
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()

#done