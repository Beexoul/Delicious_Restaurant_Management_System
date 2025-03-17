import json
import os
from datetime import datetime

USER_DATA_DIR = r"./User_Data"
INGREDIENT_REQUESTS_FILE = os.path.join(USER_DATA_DIR, "ingredient_requests.json")
INVENTORY_FILE = os.path.join(USER_DATA_DIR, "inventory.json")

def load_requests():
    if os.path.exists(INGREDIENT_REQUESTS_FILE):
        with open(INGREDIENT_REQUESTS_FILE, 'r') as file:
            return json.load(file)
    return []

def save_requests(requests):
    with open(INGREDIENT_REQUESTS_FILE, 'w') as file:
        json.dump(requests, file, indent=4)

def load_inventory():
    if os.path.exists(INVENTORY_FILE):
        with open(INVENTORY_FILE, 'r') as file:
            return json.load(file)
    return {
        "Flour": 0.0,
        "Sugar": 0.0,
        "Salt": 0.0,
        "Chicken": 0.0,
        "Vegetables": 0.0
    }

def save_inventory(inventory):
    with open(INVENTORY_FILE, 'w') as file:
        json.dump(inventory, file, indent=4)

def view_requests():
    requests = load_requests()
    
    if not requests:
        print("\nNo ingredient requests found!")
        return None, []
        
    print("\n--- Ingredient Requests ---")
    print("No.".ljust(5) + "Timestamp".ljust(20) + "Ingredient".ljust(25) + "Quantity".ljust(15) + "Status")
    print("-" * 80)
    
    pending_requests = []
    for idx, request in enumerate(requests, 1):
        print(f"{str(idx).ljust(5)} {request['timestamp'].ljust(20)} {request['ingredient'].ljust(25)} {str(request['quantity']).ljust(15)} {request['status']}")
        if request["status"] == "Pending":
            pending_requests.append((idx - 1, request))
    
    return requests, pending_requests

def manage_request(requests, pending_requests):
    if not pending_requests:
        print("\nNo pending requests to manage!")
        return False
    
    try:
        request_num = int(input("\nEnter the request number to manage (0 to skip): "))
        if request_num == 0:
            return False
            
        if request_num < 1 or request_num > len(requests):
            print("Invalid request number!")
            return False
            
        request_idx = None
        for idx, req in pending_requests:
            if request_num == idx + 1:
                request_idx = idx
                break
                
        if request_idx is None:
            print("Invalid selection! Only pending requests can be managed.")
            return False
            
        request = requests[request_idx]
        
        print("\nOptions:")
        print("1. Approve Request")
        print("2. Reject Request")
        
        choice = input("Choose an action (1-2): ")
        
        inventory = load_inventory()
        
        if choice == "1":
            ingredient = request['ingredient']
            quantity = request['quantity']
            
            if ingredient in inventory:
                inventory[ingredient] += quantity
            else:
                inventory[ingredient] = quantity
                
            request['status'] = "Approved"
            request['processed_timestamp'] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            save_inventory(inventory)
            print(f"Request for {quantity} of {ingredient} approved and added to inventory!")
            
        elif choice == "2":
            request['status'] = "Rejected"
            request['processed_timestamp'] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            print(f"Request for {request['quantity']} of {request['ingredient']} rejected!")
            
        else:
            print("Invalid choice!")
            return False
            
        save_requests(requests)
        return True
        
    except ValueError:
        print("Please enter a valid number!")
        return False

def view_inventory():
    inventory = load_inventory()
    
    if not inventory:
        print("\nInventory is empty!")
        return
        
    print("\n--- Current Inventory ---")
    print("Ingredient".ljust(25) + "Quantity")
    print("-" * 40)
    for item, qty in inventory.items():
        print(f"{item.ljust(25)} {qty}")

def main():
    while True:
        print("\n--- Manage Ingredient Requests ---")
        print("1. View and Manage Requests")
        print("2. View Inventory")
        print("3. Back to Manager Menu")
        
        choice = input("Enter your choice: ").strip()
        
        if choice == "1":
            result = view_requests()
            if result:
                requests, pending_requests = result
                manage_request(requests, pending_requests)
        elif choice == "2":
            view_inventory()
        elif choice == "3":
            print("Returning to Manager Menu...")
            break
        else:
            print("Invalid choice. Please try again.")
        
        input("\nPress Enter to continue...")

if __name__ == "__main__":
    main()

#done