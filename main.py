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

# Predefined staff users
staff_users = {
    "admin": {"password": "admin123", "role": "admin"},
    "chef": {"password": "chef123", "role": "chef"},
    "manager": {"password": "manager123", "role": "manager"}
}

# Ensure User_Data directory exists
USER_DATA_DIR = "./User_Data"
CUSTOMER_CREDENTIALS_FILE = os.path.join(USER_DATA_DIR, "customer_credentials.json")

if not os.path.exists(USER_DATA_DIR):
    os.makedirs(USER_DATA_DIR)

# Load customer credentials from file
def load_customer_credentials():
    try:
        with open(CUSTOMER_CREDENTIALS_FILE, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return {}

# Save customer credentials to file
def save_customer_credentials(credentials):
    with open(CUSTOMER_CREDENTIALS_FILE, "w") as file:
        json.dump(credentials, file, indent=4)

# Authentication function
def authenticate(username, password):
    if not username.strip() or not password.strip():
        return None
    
    username = username.lower()
    
    # Check staff users
    if username in staff_users and staff_users[username]["password"] == password:
        return staff_users[username]["role"]
    
    # Check customer credentials
    customer_credentials = load_customer_credentials()
    if username in customer_credentials and customer_credentials[username]["password"] == password:
        return "customer"
    
    return None

# Forgot password function
def forgot_password():
    attempts = 3
    while attempts > 0:
        username = input("Enter your username: ").lower()
        
        if username in staff_users:
            print(f"Your password is: {staff_users[username]['password']}")
            return
        
        customer_credentials = load_customer_credentials()
        if username in customer_credentials:
            print(f"Your password is: {customer_credentials[username]['password']}")
            return
        
        attempts -= 1
        print(f"Username not found. Attempts left: {attempts}")
    
    print("Too many failed attempts. Try again later.")

# Register customer function
def register_customer():
    print("\n--- Customer Registration ---")
    customer_credentials = load_customer_credentials()
    
    while True:
        username = input("Enter a new username: ").lower().strip()
        if not username:
            print("Username cannot be empty!")
        elif username in staff_users or username in customer_credentials:
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

# Run main
if __name__ == "__main__":
    main()
