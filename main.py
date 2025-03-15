import sys
import os

sys.path.append(os.path.abspath(os.path.dirname(__file__)))

from user_admin import admin
from user_chef import chef
from user_manager import manager
from user_customer import customer

users = {
    "admin": {"password": "admin123", "role": "admin"},
    "chef": {"password": "chef123", "role": "chef"},
    "manager": {"password": "manager123", "role": "manager"},
    "customer": {"password": "customer123", "role": "customer"}
}

# Function to authenticate user
def authenticate(username, password):
    username = username.lower() 
    if username in users and users[username]["password"] == password:
        return users[username]["role"]
    return None

# Function for password recovery
def forgot_password():
    attempts = 3
    while attempts > 0:
        username = input("Enter your username: ").lower()
        if username in users:
            print(f"Your password is: {users[username]['password']}")
            return
        else:
            attempts -= 1
            print(f"Username not found. Attempts left: {attempts}")
    print("Too many failed attempts. Try again later.")

# Main function
def main():
    print("\n--------------------------------------")
    print("Welcome to the Delicious Restaurant!")
    print("--------------------------------------")
    
    while True:
        print("\n1. Login")
        print("2. Forgot Password")
        print("3. Exit")

        choice = input("\nEnter your choice: ")
        if choice == "1":
            print("\n______Login Menu_______")
            username = input("Enter your username: ")
            password = input("Enter your password: ")
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
                    customer.main()
            else:
                print("Invalid credentials! Please try again.")
        
        elif choice == "2":
            forgot_password()
        
        elif choice == "3":
            print("\nExiting program. Goodbye!\n")
            break
        
        else:
            print("\nInvalid choice! Please try again.")

# Run main
if __name__ == "__main__":
    main()
