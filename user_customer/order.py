import datetime
import json
import os

menu = {
    "Buff Mo:Mo": 150,
    "Chicken Mo:Mo": 180,
    "Veg Mo:Mo": 120,
    "Veg Keema Noodles": 150,
    "Buff Keema Noodles": 180,
    "Chicken Keema Noodles": 200
}

def display_menu():
    print("\n=== Menu ===")
    print("Item Name".ljust(25) + "Price")
    print("-" * 35)
    for item, price in menu.items():
        print(f"{item.ljust(25)} {price}")
    print("-" * 35)

def load_customer_profile(username):
    filename = f"./User_Data/customer_profile_{username}.json"
    try:
        with open(filename, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return None

def take_order(customer_id, username):
    customer_data = load_customer_profile(username)
    if not customer_data:
        print("Please create a profile first in the Profile menu!")
        return None, None, None, None
    
    name = customer_data['name']
    contact = customer_data['contact_number']
    location = customer_data['address']
    
    orders = {}
    while True:
        print("\n1. Add Item")
        print("2. Edit Item")
        print("3. Delete Item")
        print("4. View Current Order")
        print("5. Confirm and Pay")
        print("6. Cancel")
        
        choice = input("Enter your choice: ")
        
        if choice == "1":
            display_menu()
            item = input("\nEnter item name to order: ")
            if item in menu:
                try:
                    quantity = int(input(f"How many {item} do you want? "))
                    if quantity > 0:
                        orders[item] = orders.get(item, 0) + quantity
                        print(f"Added {quantity} {item}(s) to your order.")
                    else:
                        print("Please enter a positive quantity!")
                except ValueError:
                    print("Please enter a valid number!")
            else:
                print("Item not found in menu!")
                
        elif choice == "2": 
            if not orders:
                print("No items in your order yet!")
            else:
                print("\nCurrent Order:")
                for i, (item, qty) in enumerate(orders.items(), 1):
                    print(f"{i}. {item}: {qty}")
                try:
                    item_num = int(input("Enter item number to edit: "))
                    if 1 <= item_num <= len(orders):
                        item = list(orders.keys())[item_num - 1]
                        new_qty = int(input(f"Enter new quantity for {item} (current: {orders[item]}): "))
                        if new_qty > 0:
                            orders[item] = new_qty
                            print(f"Updated {item} to {new_qty}.")
                        elif new_qty == 0:
                            del orders[item]
                            print(f"Removed {item} from order.")
                        else:
                            print("Quantity must be positive!")
                    else:
                        print("Invalid item number!")
                except ValueError:
                    print("Please enter a valid number!")
                    
        elif choice == "3": 
            if not orders:
                print("No items in your order yet!")
            else:
                print("\nCurrent Order:")
                for i, (item, qty) in enumerate(orders.items(), 1):
                    print(f"{i}. {item}: {qty}")
                try:
                    item_num = int(input("Enter item number to delete: "))
                    if 1 <= item_num <= len(orders):
                        item = list(orders.keys())[item_num - 1]
                        del orders[item]
                        print(f"Deleted {item} from order.")
                    else:
                        print("Invalid item number!")
                except ValueError:
                    print("Please enter a valid number!")
                    
        elif choice == "4": 
            if not orders:
                print("No items in your order yet!")
            else:
                generate_bill(name, contact, location, orders)
                
        elif choice == "5":  
            if not orders:
                print("No items to confirm!")
            else:
                generate_bill(name, contact, location, orders)
                payment = input("Enter 'pay' to confirm payment: ")
                if payment.lower() == 'pay':
                    save_order(customer_id, name, contact, location, orders, username)
                    print("Order confirmed and payment received!")
                    return name, contact, location, orders
                else:
                    print("Payment not confirmed. Order remains unplaced.")
                    
        elif choice == "6": 
            print("Order cancelled.")
            return None, None, None, None
            
        else:
            print("Invalid choice!")

def save_order(customer_id, name, contact, location, orders, username):
    order_data = {
        "order_id": f"{customer_id}_{datetime.datetime.now().strftime('%Y%m%d%H%M%S')}",  
        "customer_id": customer_id,
        "username": username,
        "name": name,
        "contact": contact,
        "location": location,
        "timestamp": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "orders": orders,
        "status": {}  
    }
    
    script_dir = os.path.dirname(os.path.abspath(__file__))
    project_root = os.path.dirname(script_dir)
    orders_file = os.path.join(project_root, "User_Data", "orders.json")

    
    if os.path.exists(orders_file):
        with open(orders_file, 'r') as file:
            all_orders = json.load(file)
    else:
        all_orders = []
    
    all_orders.append(order_data)
    
    with open(orders_file, 'w') as file:
        json.dump(all_orders, file, indent=4)

def generate_bill(name, contact, location, orders):
    print("\n" + "=" * 50)
    print("RESTAURANT BILL".center(50))
    print("=" * 50)
    print(f"Name: {name}")
    print(f"Contact: {contact}")
    print(f"Location: {location}")
    print("=" * 50)
    
    print("Item Name".ljust(25) + "Qty".ljust(10) + "Price".ljust(10) + "Total")
    print("-" * 50)
    
    grand_total = 0
    for item, quantity in orders.items():
        price = menu[item]
        total = price * quantity
        grand_total += total
        print(f"{item.ljust(25)} {str(quantity).ljust(10)} {str(price).ljust(10)} {total}")
    
    print("-" * 50)
    print(f"Grand Total:".ljust(45) + f"{grand_total}")
    print("=" * 50)

def main(logged_in_username):
    customer_data = load_customer_profile(logged_in_username)
    if customer_data:
        customer_id = customer_data['contact_number']  
        while True:
            name, contact, location, orders = take_order(customer_id, logged_in_username)
            if name: 
                break
            choice = input("\nWould you like to try ordering again? (yes/no): ")
            if choice.lower() != 'yes':
                print("Thank you for visiting!")
                break
    else:
        print("Please set up your profile first in the Profile menu!")