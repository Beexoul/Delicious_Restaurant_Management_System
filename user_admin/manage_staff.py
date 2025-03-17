import json
import os

USER_FILE = r".\User_Data\users.json"

def load_users():
    if os.path.exists(USER_FILE):
        with open(USER_FILE, 'r') as file:
            return json.load(file)
    # Default users if file doesn't exist
    return [
        {"username": "chef", "role": "chef", "password": "chef123"},
        {"username": "manager", "role": "manager", "password": "manager123"}
    ]

def save_users(users):
    with open(USER_FILE, 'w') as file:
        json.dump(users, file, indent=4)

def list_users(users):
    staff = [user for user in users if user['role'] in ['chef', 'manager']]
    if not staff:
        print("\nNo staff found!")
        return
    
    print("\n--- Staff List ---")
    print("Username".ljust(15) + "Role".ljust(10) + "Password")
    print("-" * 40)
    for user in staff:
        username = user['username']
        role = user['role']
        password_mask = '*' * len(user['password'])
        print(f"{username.ljust(15)} {role.ljust(10)} {password_mask}")

def add_user(users):
    print("\n--- Add New Staff ---")
    username = input("Enter username: ").strip()
    for user in users:
        if user['username'].lower() == username.lower():
            print("Username already exists!")
            return
    
    role = input("Enter role (chef/manager): ").strip().lower()
    
    valid_roles = ["chef", "manager"]
    if role not in valid_roles:
        print(f"Invalid role! Must be one of: {', '.join(valid_roles)}")
        return
    
    password = input("Enter password: ").strip()
    if not password:
        print("Password cannot be empty!")
        return
    
    new_user = {
        "username": username,
        "role": role,
        "password": password
    }
    users.append(new_user)
    save_users(users)
    print(f"Staff '{username}' added successfully!")

def edit_user(users):
    print("\n--- Edit Staff ---")
    username = input("Enter username to edit: ").strip()
    
    found_user = None
    for user in users:
        if user['username'].lower() == username.lower() and user['role'] in ['chef', 'manager']:
            found_user = user
            break
    
    if not found_user:
        print("Staff not found!")
        return
    
    print(f"Editing {found_user['username']}:")
    new_role = input(f"Enter new role (chef/manager) [{found_user['role']}]: ").strip().lower() or found_user['role']
    new_password = input("Enter new password or leave blank to keep current: ").strip()
    
    valid_roles = ["chef", "manager"]
    if new_role not in valid_roles:
        print(f"Invalid role! Keeping current role: {found_user['role']}")
    else:
        found_user['role'] = new_role
    
    if new_password:
        found_user['password'] = new_password
    
    save_users(users)
    print("Staff updated successfully!")

def delete_user(users):
    print("\n--- Delete Staff ---")
    username = input("Enter username to delete: ").strip()
    
    for i, user in enumerate(users):
        if user['username'].lower() == username.lower() and user['role'] in ['chef', 'manager']:
            del users[i]
            save_users(users)
            print(f"Staff '{username}' deleted successfully!")
            return
    print("Staff not found!")

def main():
    users = load_users()
    
    while True:
        print("\n--- Manage Staff ---")
        print("1. List Staff")
        print("2. Add Staff")
        print("3. Edit Staff")
        print("4. Delete Staff")
        print("5. Back to Admin Menu")
        
        choice = input("Enter your choice: ").strip()
        
        if choice == "1":
            list_users(users)
        elif choice == "2":
            add_user(users)
        elif choice == "3":
            edit_user(users)
        elif choice == "4":
            delete_user(users)
        elif choice == "5":
            print("Returning to Admin Menu...")
            break
        else:
            print("Invalid choice. Please try again.")
        
        input("\nPress Enter to continue...")

if __name__ == "__main__":
    main()

#done