import json
import os

USER_DATA_DIR = os.path.join(os.path.dirname(__file__), "..", "User_Data")
CREDENTIALS_FILE = os.path.join(USER_DATA_DIR, "customer_credentials.json")

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

def add_customer(credentials_file=CREDENTIALS_FILE):
    name = input("Enter customer name: ").strip()
    email = input("Enter email: ").strip()
    contact = input("Enter contact number: ").strip()
    address = input("Enter address: ").strip()
    username = input("Enter username: ").strip().lower()
    password = input("Enter password: ").strip()
    role = "customer"
    credentials = load_json_file(credentials_file)

    if username in credentials:
        print("Username already exists!")
        return

    credentials[username] = {
        "name": name,
        "email": email,
        "contact_number": contact,
        "address": address,
        "password": password,
        "role": role
    }

    save_json_file(credentials_file, credentials)
    print(f"Customer {username} added successfully! They can now log in.")

def edit_customer(username, credentials_file=CREDENTIALS_FILE):
    credentials = load_json_file(credentials_file)

    if username not in credentials:
        print("Customer not found!")
        return

    print("Leave blank to keep existing value")
    current_data = credentials[username]
    name = input(f"Enter name ({current_data['name']}): ") or current_data['name']
    email = input(f"Enter email ({current_data['email']}): ") or current_data['email']
    contact = input(f"Enter contact ({current_data['contact_number']}): ") or current_data['contact_number']
    address = input(f"Enter address ({current_data['address']}): ") or current_data['address']
    password = input(f"Enter password ({current_data['password']}): ") or current_data['password']

    credentials[username] = {
        "name": name,
        "email": email,
        "contact_number": contact,
        "address": address,
        "password": password,
        "role": "customer" 
    }

    save_json_file(credentials_file, credentials)
    print(f"Customer {username} updated successfully!")

def delete_customer(username, credentials_file=CREDENTIALS_FILE):
    credentials = load_json_file(credentials_file)

    if username not in credentials:
        print("Customer not found!")
        return

    del credentials[username]
    save_json_file(credentials_file, credentials)
    print(f"Customer {username} deleted successfully!")

def display_customers(credentials_file=CREDENTIALS_FILE):
    credentials = load_json_file(credentials_file)
    if not credentials:
        print("No customers found!")
        return
    for username, data in credentials.items():
        print(f"\nUsername: {username}")
        for key, value in data.items():
            print(f"{key}: {value}")

def main():
    print("Customer Management System")
    while True:
        print("\n1. Add Customer")
        print("2. Edit Customer")
        print("3. Delete Customer")
        print("4. Display Customers")
        print("5. Exit")
        
        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            add_customer()
        elif choice == '2':
            username = input("Enter username to edit: ").lower()
            edit_customer(username)
        elif choice == '3':
            username = input("Enter username to delete: ").lower()
            delete_customer(username)
        elif choice == '4':
            display_customers()
        elif choice == '5':
            print("Exiting...")
            break
        else:
            print("Invalid choice! Please try again.")

if __name__ == "__main__":
    main()

#done