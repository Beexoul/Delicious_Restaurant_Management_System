import admin
import chef
import manager
import customer

users = {
    "admin": {"password": "admin123", "role": "admin"},
    "chef": {"password": "chef123", "role": "chef"},
    "manager": {"password": "manager123", "role": "manager"},
    "customer": {"password": "customer123", "role": "customer"}
}

def authenticate(username, password):
    username = username.lower() 
    if username in users and users[username]["password"] == password:
        return users[username]["role"]
    return None

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

def main():
    print(" ")
    print(" ")
    print("--------------------------------------")
    print("Welcome to the Food Ordering System!")
    print("--------------------------------------")
    while True:
        print("\n1. Login")
        print("2. Forgot Password")
        print("3. Exit")
        print(" ")
        print(" ")
        choice = input("Enter your choice: ")
        
        if choice == "1":
            print("\n______Login Menu_______")
            print(" ")
            username = input("Enter your username: ")
            password = input("Enter your password: ")
            role = authenticate(username, password)
            
            if role:
                print(" ")
                print(f"Login successful! ")
                print("Redirecting to the", role, "menu...")
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
            print("Exiting program. Goodbye!")
            break
        else:
            print("Invalid choice! Please try again.")

if __name__ == "__main__":
    main()