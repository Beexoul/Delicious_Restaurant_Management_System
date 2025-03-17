import json
import os
from datetime import datetime, date
from collections import Counter

MENU = {
    "Buff Mo:Mo": 150,
    "Chicken Mo:Mo": 180,
    "Veg Mo:Mo": 120,
    "Veg Keema Noodles": 150,
    "Buff Keema Noodles": 180,
    "Chicken Keema Noodles": 200
}

def load_json_file(filename):
    try:
        if os.path.exists(filename):
            with open(filename, 'r') as file:
                return json.load(file)
        return None
    except json.JSONDecodeError as e:
        print(f"Error decoding JSON file {filename}: {e}")
        return None

def get_orders_file_path():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    project_root = os.path.dirname(script_dir)
    return os.path.join(project_root, "User_Data", "orders.json")

def get_number_of_users():
    orders = load_json_file(get_orders_file_path())
    return len(orders) if orders else 0

def get_most_selling_item():
    orders = load_json_file(get_orders_file_path())
    if not orders:
        return None, 0
    
    item_counts = Counter()
    for order in orders:
        orders_dict = order.get('orders', {})
        for item, quantity in orders_dict.items():
            if isinstance(quantity, (int, float)) and quantity > 0:
                item_counts[item] += quantity
    
    return item_counts.most_common(1)[0] if item_counts else (None, 0)

def get_daily_sales(today=None):
    if today is None:
        today = date.today()
    
    orders = load_json_file(get_orders_file_path())
    if not orders:
        return {}, 0
    
    daily_sales = Counter()
    total_income = 0
    
    for order in orders:
        timestamp = order.get('timestamp')
        if not isinstance(timestamp, str):
            print(f"Skipping order with missing/invalid timestamp: {order}")
            continue
        
        try:
            order_date = datetime.strptime(timestamp, "%Y-%m-%d %H:%M:%S").date()
        except ValueError as e:
            corrected = False
            if 'd' in timestamp:
                try:
                    corrected_timestamp = timestamp.replace('d', str(today.day).zfill(2))
                    order_date = datetime.strptime(corrected_timestamp, "%Y-%m-%d %H:%M:%S").date()
                    print(f"Corrected timestamp '{timestamp}' to '{corrected_timestamp}'")
                    corrected = True
                except ValueError:
                    pass
            if not corrected:
                print(f"Skipping order due to timestamp error: {e} - Order: {order}")
                continue

        if order_date == today:
            for item, quantity in order.get('orders', {}).items():
                if item in MENU and isinstance(quantity, (int, float)) and quantity > 0:
                    daily_sales[item] += quantity
                    total_income += MENU[item] * quantity
    
    return daily_sales, total_income

def print_admin_report():
    print("\n" + "-" * 38)
    print("Admin Report - Delicious Restaurant".center(38))
    print("-" * 38)

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
        print(f"{'Item Name':<25} {'Quantity Sold':<15} {'Revenue':<10}")
        print("-" * 50)
        for item, quantity in daily_sales.items():
            revenue = MENU[item] * quantity
            print(f"{item:<25} {quantity:<15} {revenue:<10}")
        print("-" * 50)
        print(f"{'Total Income Today:':<40} {total_income}")
    else:
        print("No sales recorded for today.")

def main():
    print_admin_report()
    input("\nPress Enter to return to the admin menu...")

if __name__ == "__main__":
    main()

#done