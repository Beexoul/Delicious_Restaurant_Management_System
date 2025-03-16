import json
import os
from datetime import datetime, date
from collections import Counter

menu = {
    "Buff Mo:Mo": 150,
    "Chicken Mo:Mo": 180,
    "Veg Mo:Mo": 120,
    "Veg Keema Noodles": 150,
    "Buff Keema Noodles": 180,
    "Chicken Keema Noodles": 200
}

def load_json_file(filename):
    if os.path.exists(filename):
        with open(filename, 'r') as file:
            return json.load(file)
    return None

def get_number_of_users():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    project_root = os.path.dirname(script_dir)
    orders_file = os.path.join(project_root, "User_Data", "orders.json")
    
    orders = load_json_file(orders_file)
    if orders:
        return len(orders)
    return 0

def get_most_selling_item():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    project_root = os.path.dirname(script_dir)
    orders_file = os.path.join(project_root, "User_Data", "orders.json")

    orders = load_json_file(orders_file)
    if not orders:
        return None, 0
    
    item_counts = Counter()
    for order in orders:
        for item, quantity in order.get('orders', {}).items():
            item_counts[item] += quantity
    
    if not item_counts:
        return None, 0
    
    most_sold_item, quantity = item_counts.most_common(1)[0]
    return most_sold_item, quantity

def get_daily_sales(today=None):
    if today is None:
        today = date.today()
    
    script_dir = os.path.dirname(os.path.abspath(__file__))
    project_root = os.path.dirname(script_dir)
    orders_file = os.path.join(project_root, "User_Data", "orders.json")
        
    orders = load_json_file(orders_file)
    if not orders:
        return {}, 0
    
    daily_sales = Counter()
    total_income = 0
    
    for order in orders:
        try:
            order_date = datetime.strptime(order['timestamp'], "%Y-%m-%d %H:%M:%S").date()
            if order_date == today:
                for item, quantity in order.get('orders', {}).items():
                    if item in menu: 
                        daily_sales[item] += quantity
                        total_income += menu[item] * quantity
        except (KeyError, ValueError) as e:
            print(f"Skipping order due to error: {e}")
            continue
    
    return daily_sales, total_income

def main():
    print("\n--------------------------------------")
    print("Admin Report - Delicious Restaurant".center(50))
    print("--------------------------------------")
    
    num_users = get_number_of_users()
    print(f"\nTotal Number of Registered Customers: {num_users}")
    
    most_sold_item, quantity_sold = get_most_selling_item()
    if most_sold_item:
        print(f"\nMost Selling Food Item: {most_sold_item} ({quantity_sold} sold)")
    else:
        print("\nMost Selling Food Item: None (no orders yet)")
    
    today = date.today()
    daily_sales, total_income = get_daily_sales(today)
    
    print(f"\nSales Report for {today}:")
    if daily_sales:
        print("Item Name".ljust(25) + "Quantity Sold".ljust(15) + "Revenue")
        print("-" * 65)
        for item, quantity in daily_sales.items():
            revenue = menu[item] * quantity
            print(f"{item.ljust(25)} {str(quantity).ljust(15)} {revenue}")
        print("-" * 65)
        print(f"Total Income Today:".ljust(50) + f"{total_income}")
    else:
        print("No sales recorded for today.")
    
    input("\nPress Enter to return to the admin menu...")

if __name__ == "__main__":
    main()