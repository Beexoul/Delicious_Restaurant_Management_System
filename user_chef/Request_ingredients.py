import json
import os
from datetime import datetime

USER_DATA_DIR = r"./User_Data"
INGREDIENT_REQUESTS_FILE = os.path.join(USER_DATA_DIR, "ingredient_requests.json")

def load_requests():
    if os.path.exists(INGREDIENT_REQUESTS_FILE):
        with open(INGREDIENT_REQUESTS_FILE, 'r') as file:
            return json.load(file)
    return []

def save_requests(requests):
    with open(INGREDIENT_REQUESTS_FILE, 'w') as file:
        json.dump(requests, file, indent=4)

def request_ingredients():
    print("\n--- Request Ingredients ---")
    requests = load_requests()
    
    while True:
        ingredient = input("Enter ingredient name (or 'done' to finish): ").strip()
        if ingredient.lower() == 'done':
            break
            
        if not ingredient:
            print("Ingredient name cannot be empty!")
            continue
            
        try:
            quantity = input("Enter quantity needed: ").strip()
            if not quantity:
                print("Quantity cannot be empty!")
                continue
            quantity = float(quantity) 
            if quantity <= 0:
                print("Quantity must be positive!")
                continue
                
            request = {
                "ingredient": ingredient,
                "quantity": quantity,
                "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                "status": "Pending"
            }
            
            requests.append(request)
            print(f"Request for {quantity} of {ingredient} added successfully!")
            
        except ValueError:
            print("Please enter a valid number for quantity!")
            continue
    
    if requests != load_requests():
        save_requests(requests)
        print("\nAll requests saved successfully!")

def view_requests():
    requests = load_requests()
    
    if not requests:
        print("\nNo ingredient requests found!")
        return
        
    print("\n--- Pending Ingredient Requests ---")
    print("Timestamp".ljust(20) + "Ingredient".ljust(25) + "Quantity".ljust(15) + "Status")
    print("-" * 80)
    
    for request in requests:
        if request["status"] == "Pending":
            print(f"{request['timestamp'].ljust(20)} {request['ingredient'].ljust(25)} {str(request['quantity']).ljust(15)} {request['status']}")

def main():
    while True:
        print("\n--- Chef Ingredient Request System ---")
        print("1. Request Ingredients")
        print("2. View Pending Requests")
        print("3. Back to Chef Menu")
        
        choice = input("Enter your choice: ").strip()
        
        if choice == "1":
            request_ingredients()
        elif choice == "2":
            view_requests()
        elif choice == "3":
            print("Returning to Chef Menu...")
            break
        else:
            print("Invalid choice. Please try again.")
        
        input("\nPress Enter to continue...")

if __name__ == "__main__":
    main()