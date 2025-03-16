import sys
import os
import json

# Add current directory to system path
sys.path.append(os.path.abspath(os.path.dirname(__file__)))

# Import modules
from user_admin import admin
from user_chef import chef
from user_manager import manager
from user_customer import customer

USER_DATA_DIR = r"./User_Data"
USERS_FILE = os.path.join(USER_DATA_DIR, "users.json")
CUSTOMER_CREDENTIALS_FILE = os.path.join(USER_DATA_DIR, "customer_credentials.json")

if not os.path.exists(USER_DATA_DIR):
    os.makedirs(USER_DATA_DIR)

def load_users():
    if os.path.exists(USERS_FILE):
        with open(USERS_FILE, 'r') as file:
            return json.load(file)
    return [
        {"username": "beexoul", "role": "admin", "password": "dev@beexoul"},
    ]

# Load customer credentials from customer_credentials.json
def load_customer_credentials():
    """Load customer data from customer_credentials.json."""
    if os.path.exists(CUSTOMER_CREDENTIALS_FILE):
        with open(CUSTOMER_CREDENTIALS_FILE, 'r') as file:
            return json.load(file)
    return {}

# Save customer credentials to customer_credentials.json
def save_customer_credentials(credentials):
    """Save customer data to customer_credentials.json."""
    with open(CUSTOMER_CREDENTIALS_FILE, "w") as file:
        json.dump(credentials, file, indent=4)

# Authentication function
def authenticate(username, password):
    """Authenticate user against users.json and customer_credentials.json."""
    if not username.strip() or not password.strip():
        return None
    
    username = username.lower()
    
    # Check users.json (staff)
    users = load_users()
    for user in users:
        if user["username"].lower() == username and user["password"] == password:
            return user["role"]
    
    # Check customer_credentials.json (customers)
    customer_credentials = load_customer_credentials()
    if username in customer_credentials and customer_credentials[username]["password"] == password:
        return customer_credentials[username]["role"]
    
    return None

# Forgot password function
def forgot_password():
    """Retrieve password from users.json or customer_credentials.json."""
    attempts = 3
    while attempts > 0:
        username = input("Enter your username: ").lower()
        
        # Check users.json (staff)
        users = load_users()
        for user in users:
            if user["username"].lower() == username:
                print(f"Your password is: {user['password']}")
                return
        
        # Check customer_credentials.json (customers)
        customer_credentials = load_customer_credentials()
        if username in customer_credentials:
            print(f"Your password is: {customer_credentials[username]['password']}")
            return
        
        attempts -= 1
        print(f"Username not found. Attempts left: {attempts}")
    
    print("Too many failed attempts. Try again later.")

# Register customer function
def register_customer():
    """Register a new customer into customer_credentials.json."""
    print("\n--- Customer Registration ---")
    customer_credentials = load_customer_credentials()
    users = load_users()  # Check against staff to avoid duplicates
    
    while True:
        username = input("Enter a new username: ").lower().strip()
        if not username:
            print("Username cannot be empty!")
        elif username in customer_credentials or any(user["username"].lower() == username for user in users):
            print("Username already taken! Please choose another.")
        else:
            break
    
    while True:
        password = input("Enter a password: ").strip()
        if not password:
            print("Password cannot be empty!")
        else:
            break
    
    customer_credentials[username] = {"password": password, "role": "customer"}
    save_customer_credentials(customer_credentials)
    print(f"Registration successful! You can now log in as '{username}'.")

# Main function
def main():
    print("\n--------------------------------------")
    print("Welcome to the Delicious Restaurant!")
    print("--------------------------------------")
    
    while True:
        print("\n1. Login")
        print("2. Register (Customer Only)")
        print("3. Forgot Password")
        print("4. Exit")

        choice = input("\nEnter your choice: ").strip()
        
        if choice == "1":
            print("\n______Login Menu_______")
            username = input("Enter your username: ").strip()
            password = input("Enter your password: ").strip()
            role = authenticate(username, password)
            
            if role:
                print(f"\nLogin successful! Redirecting to the {role} menu...\n")
                if role == "admin":
                    admin.main()
                elif role == "chef":
                    chef.main()
                elif role == "manager":
                    manager.main()
                elif role == "customer":
                    customer.main(username)
            else:
                print("Invalid credentials! Please try again.")
        
        elif choice == "2":
            register_customer()
        
        elif choice == "3":
            forgot_password()
        
        elif choice == "4":
            print("\nExiting program. Goodbye!\n")
            break
        
        else:
            print("\nInvalid choice! Please try again.")

if __name__ == "__main__":
    main()