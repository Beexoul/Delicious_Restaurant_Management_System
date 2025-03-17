import json
import os

def display_order_status(logged_in_username):
    script_dir = os.path.dirname(os.path.abspath(__file__))
    project_root = os.path.dirname(script_dir)
    orders_file = os.path.join(project_root, "User_Data", "orders.json")
    
    try:
        with open(orders_file, 'r') as file:
            all_orders = json.load(file)
            
            if not all_orders:
                print("No orders have been placed yet!")
                return
                
            print("\n" + "=" * 50)
            print("YOUR ORDER STATUS".center(50))
            print("=" * 50)
            
            user_orders = [order for order in all_orders if order['username'] == logged_in_username]
            if not user_orders:
                print("No active orders found for you!")
                return
                
            item_index = 1
            for order in user_orders:
                for item, quantity in order['orders'].items():
                    status = order['status'].get(item, "Pending")
                    print(f"{item_index}. {item}: {quantity} [{status}]")
                    item_index += 1
            
            if item_index == 1:
                print("No items found in your orders!")
                
    except FileNotFoundError:
        print("No orders have been placed yet!")
    except json.JSONDecodeError:
        print("Error reading orders file. It may be corrupted.")

def main(logged_in_username):
    print("Welcome to Order Status Checker")
    while True:
        display_order_status(logged_in_username)
        choice = input("\nPress Enter to refresh status or type 'exit' to quit: ")
        if choice.lower() == 'exit':
            print("Thank you for checking your order status. Goodbye!")
            break

#done