import json
import os

def view_and_update_orders():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    project_root = os.path.dirname(script_dir)
    orders_file = os.path.join(project_root, "User_Data", "orders.json")
    
    try:
        with open(orders_file, 'r') as file:
            orders = json.load(file)
            
            if not orders:
                print("No orders yet!")
                return False
                
            print("\n" + "=" * 50)
            print("CURRENT ORDERS".center(50))
            print("=" * 50)
            
            menu_items = []
            item_index = 1
            
            for order_idx, order in enumerate(orders):
                for item, quantity in order['orders'].items():
                    status = order['status'].get(item, "Pending")
                    if status != "Done": 
                        display_text = f"{item}: {quantity} [{status}] (Order ID: {order['order_id']})"
                        print(f"{item_index}. {display_text}")
                        menu_items.append((order_idx, item, quantity, display_text))
                        item_index += 1
            
            if not menu_items:
                print("No active menu items found!")
                return False
                
            return orders, menu_items
            
    except FileNotFoundError:
        print("No order file found yet! No orders have been placed.")
        return False
    except json.JSONDecodeError:
        print("Error reading orders file. It may be corrupted.")
        return False

def update_order_status(orders, menu_items):
    try:
        order_num = int(input("\nEnter the order number to update (or 0 to skip): "))
        if order_num == 0:
            return False
            
        if order_num < 1 or order_num > len(menu_items):
            print("Invalid order number!")
            return False
            
        print("\nOptions:")
        print("1. Mark as Completed")
        print("2. Mark as In Progress")
        
        choice = input("Choose an action (1-2): ")
        
        if choice == "1":
            status = "Completed"
        elif choice == "2":
            status = "In Progress"
        else:
            print("Invalid choice!")
            return False
            
        order_idx, item, quantity, _ = menu_items[order_num - 1]
        orders[order_idx]['status'][item] = status
        
        script_dir = os.path.dirname(os.path.abspath(__file__))
        project_root = os.path.dirname(script_dir)
        orders_file = os.path.join(project_root, "User_Data", "orders.json")
        with open(orders_file, 'w') as file:
            json.dump(orders, file, indent=4)
            
        print("Order updated successfully!")
        return True
        
    except ValueError:
        print("Please enter a valid number!")
        return False

def main():
    print("Chef's Order Updater")
    while True:
        result = view_and_update_orders()
        
        if result:
            orders, menu_items = result
            update_order_status(orders, menu_items)
            
        choice = input("\nPress Enter to refresh orders or type 'exit' to quit: ")
        if choice.lower() == 'exit':
            print("Closing order updater...")
            break

if __name__ == "__main__":
    main()

#done