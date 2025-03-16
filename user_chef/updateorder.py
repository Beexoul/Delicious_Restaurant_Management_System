def view_and_update_orders():
    try:
        with open("orderfile.txt", "r") as file:
            lines = file.readlines()
            
            if not lines or not any(line.strip() for line in lines):
                print("No orders yet!")
                return False
                
            print("\n" + "=" * 50)
            print("CURRENT ORDERS".center(50))
            print("=" * 50)
            
            # Filter and display only menu items
            menu_items = []
            item_index = 1
            in_order_section = False
            
            for line in lines:
                line = line.strip()
                if line.startswith("Orders:"):
                    in_order_section = True
                elif line.startswith("====="):
                    in_order_section = False
                elif in_order_section and line and not line.startswith("[Done]"):
                    print(f"{item_index}. {line}")
                    menu_items.append((item_index, line))
                    item_index += 1
            
            if not menu_items:
                print("No active menu items found!")
                return False
                
            return lines, menu_items
            
    except FileNotFoundError:
        print("No order file found yet! No orders have been placed.")
        return False

def update_order_status(lines, menu_items):
    try:
        order_num = int(input("\nEnter the order number to update (or 0 to skip): "))
        if order_num == 0:
            return False
            
        if order_num < 1 or order_num > len(menu_items):
            print("Invalid order number!")
            return False
            
        print("\nOptions:")
        print("1. Mark as Done")
        print("2. Mark as In Preparation")
        
        choice = input("Choose an action (1-2): ")
        
        if choice == "1":
            status = "[Done]"
        elif choice == "2":
            status = "[In Preparation]"
        else:
            print("Invalid choice!")
            return False
            
        # Find the actual line in the original file to update
        selected_item = menu_items[order_num - 1][1]  # Get the menu item text
        for i, line in enumerate(lines):
            if line.strip() == selected_item:
                lines[i] = f"{selected_item} {status}\n"
                break
        
        # Write updated orders back to file
        with open("orderfile.txt", "w") as file:
            file.writelines(lines)
            
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
            lines, menu_items = result
            update_order_status(lines, menu_items)
            
        choice = input("\nPress Enter to refresh orders or type 'exit' to quit: ")
        if choice.lower() == 'exit':
            print("Closing order updater...")
            break

if __name__ == "__main__":
    main()