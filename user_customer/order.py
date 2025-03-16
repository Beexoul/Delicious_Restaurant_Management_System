import datetime

# Menu items stored in a dictionary
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

def take_order():
    print("\n=== Customer Information ===")
    name = input("Enter your name: ")
    contact = input("Enter your contact number: ")
    location = input("Enter your delivery location: ")
    
    orders = {}
    while True:
        display_menu()
        item = input("\nEnter item name to order (or 'done' to finish): ")
        
        if item.lower() == 'done':
            break
            
        if item in menu:
            try:
                quantity = int(input(f"How many {item} do you want? "))
                if quantity > 0:
                    orders[item] = quantity
                else:
                    print("Please enter a positive quantity!")
            except ValueError:
                print("Please enter a valid number!")
        else:
            print("Item not found in menu!")
    
    return name, contact, location, orders

def save_order(name, contact, location, orders):
    if not orders:
        return
    
    with open("orderfile.txt", "a") as file:
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        file.write(f"\n=== Order at {timestamp} ===\n")
        file.write(f"Name: {name}\n")
        file.write(f"Contact: {contact}\n")
        file.write(f"Location: {location}\n")
        file.write("Orders:\n")
        for item, quantity in orders.items():
            file.write(f"{item}: {quantity}\n")
        file.write("================\n")

def generate_bill(name, contact, location, orders):
    if not orders:
        print("\nNo items ordered!")
        return
    
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

def main():
    print("Welcome to the Restaurant Ordering System!")
    while True:
        name, contact, location, orders = take_order()
        generate_bill(name, contact, location, orders)
        save_order(name, contact, location, orders)
        
        choice = input("\nWould you like to place another order? (yes/no): ")
        if choice.lower() != 'yes':
            print("Thank you for ordering!")
            break
        
if __name__ == "__main__":
    main()