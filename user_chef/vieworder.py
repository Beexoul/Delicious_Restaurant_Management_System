import json
import os

def view_orders():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    project_root = os.path.dirname(script_dir)
    orders_file = os.path.join(project_root, "User_Data", "orders.json")
    
    try:
        with open(orders_file, 'r') as file:
            orders = json.load(file)
            
            if not orders:
                print("No orders yet!")
                return
                
            print("\n" + "=" * 50)
            print("CURRENT ORDERS".center(50))
            print("=" * 50)
            
            for order in orders:
                print(f"\nOrder ID: {order['order_id']}")
                print(f"Placed at: {order['timestamp']}")
                print(f"Customer Name: {order['name']}")
                print(f"Contact: {order['contact']}")
                print(f"Location: {order['location']}")
                print("Items:")
                for item, quantity in order['orders'].items():
                    status = order['status'].get(item, "Pending") 
                    print(f"  - {item}: {quantity} [{status}]")
                print("=" * 50)
            
    except FileNotFoundError:
        print("No order file found yet! No orders have been placed.")
    except json.JSONDecodeError:
        print("Error reading orders file. It may be corrupted.")

def main():
    print("Chef's Order Viewer")
    while True:
        view_orders()
        choice = input("\nPress Enter to refresh orders or type 'exit' to quit: ")
        if choice.lower() == 'exit':
            print("Closing order viewer...")
            break

if __name__ == "__main__":
    main()

#done