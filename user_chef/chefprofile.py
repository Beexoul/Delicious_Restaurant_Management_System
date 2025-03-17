import json

class Chef:
    def __init__(self, name, specialty, contact_number, experience):
        self.name = name
        self.specialty = specialty
        self.contact_number = contact_number
        self.experience = experience

    def update_profile(self):
        print("\n--- Update Chef Profile ---")
        self.name = input(f"Enter new name [{self.name}]: ") or self.name
        self.specialty = input(f"Enter new specialty [{self.specialty}]: ") or self.specialty
        self.contact_number = input(f"Enter new contact number [{self.contact_number}]: ") or self.contact_number
        self.experience = input(f"Enter new experience (in years) [{self.experience}]: ") or self.experience

        self.save_to_file()
        print("\nProfile updated successfully!\n")

    def display_profile(self):
        print("\n--- Chef Profile ---")
        print(f"Name: {self.name}")
        print(f"Specialty: {self.specialty}")
        print(f"Contact Number: {self.contact_number}")
        print(f"Experience: {self.experience} years")

    def save_to_file(self):
        data = {
            'name': self.name,
            'specialty': self.specialty,
            'contact_number': self.contact_number,
            'experience': self.experience
        }
        with open('./User_Data/chef_profile.json', 'w') as file:
            json.dump(data, file, indent=4)

    @classmethod
    def load_from_file(cls):
        try:
            with open('./User_Data/chef_profile.json', 'r') as file:
                data = json.load(file)
                return cls(**data)
        except FileNotFoundError:
            return cls("Santosh Shah", "Chicken Keema Noodles", "+977 9876540123", "23")

chef = Chef.load_from_file()

def main():
    while True:
        print("\n1. View Profile")
        print("2. Update Profile")
        print("3. Back to Main Menu")

        choice = input("Enter your choice: ")

        if choice == "1":
            chef.display_profile()
        elif choice == "2":
            chef.update_profile()
        elif choice == "3":
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()

#done