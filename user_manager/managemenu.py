import json
import os

MENU_FILE = os.path.join(os.path.dirname(__file__), "..", "User_Data", "menu.json")

def load_menu():
    try:
        with open(MENU_FILE, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        # Default menu if file doesn't exist
        return {
            "Buff Mo:Mo": 150,
            "Chicken Mo:Mo": 180,
            "Veg Mo:Mo": 120,
            "Veg Keema Noodles": 150,
            "Buff Keema Noodles": 180,
            "Chicken Keema Noodles": 200
        }

def save_menu(menu):
    os.makedirs(os.path.dirname(MENU_FILE), exist_ok=True)
    with open(MENU_FILE, 'w') as file:
        json.dump(menu, file, indent=4)

def display_menu(menu):
    if not menu:
        print("\nNo items in the menu!")
        return
    
    print("\n=== Current Menu ===")
    print("Item Name".ljust(25) + "Price")
    print("-" * 35)
    for item, price in menu.items():
        print(f"{item.ljust(25)} {price}")
    print("-" * 35)

def add_item(menu):
    print("\n--- Add New Menu Item ---")
    item = input("Enter item name: ").strip()
    if item in menu:
        print("Item already exists in the menu!")
        return
    
    try:
        price = int(input(f"Enter price for {item}: "))
        if price <= 0:
            print("Price must be a positive number!")
            return
    except ValueError:
        print("Please enter a valid number for the price!")
        return
    
    menu[item] = price
    save_menu(menu)
    print(f"Item '{item}' added successfully with price {price}!")

def edit_item(menu):
    if not menu:
        print("\nNo items in the menu to edit!")
        return
    
    print("\n--- Edit Menu Item ---")
    display_menu(menu)
    item = input("Enter item name to edit: ").strip()
    if item not in menu:
        print("Item not found in the menu!")
        return
    
    try:
        new_price = input(f"Enter new price for {item} (current: {menu[item]}): ").strip()
        if new_price:
            new_price = int(new_price)
            if new_price <= 0:
                print("Price must be a positive number!")
                return
            menu[item] = new_price
            save_menu(menu)
            print(f"Price for '{item}' updated to {new_price}!")
        else:
            print("No changes made.")
    except ValueError:
        print("Please enter a valid number for the price!")

def delete_item(menu):
    if not menu:
        print("\nNo items in the menu to delete!")
        return
    
    print("\n--- Delete Menu Item ---")
    display_menu(menu)
    item = input("Enter item name to delete: ").strip()
    if item not in menu:
        print("Item not found in the menu!")
        return
    
    del menu[item]
    save_menu(menu)
    print(f"Item '{item}' deleted successfully!")

def main():
    menu = load_menu()
    print("Menu Management System")
    while True:
        print("\n1. Display Menu")
        print("2. Add Item")
        print("3. Edit Item")
        print("4. Delete Item")
        print("5. Exit")
        
        choice = input("Enter your choice (1-5): ")
        
        if choice == "1":
            display_menu(menu)
        elif choice == "2":
            add_item(menu)
        elif choice == "3":
            edit_item(menu)
        elif choice == "4":
            delete_item(menu)
        elif choice == "5":
            print("Exiting...")
            break
        else:
            print("Invalid choice! Please try again.")

if __name__ == "__main__":
    main()

#done