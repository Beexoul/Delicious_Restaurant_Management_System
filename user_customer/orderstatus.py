def display_order_status():
    try:
        with open("orderfile.txt", "r") as file:
            lines = file.readlines()
            
            if not lines or not any(line.strip() for line in lines):
                print("No orders have been placed yet!")
                return
                
            print("\n" + "=" * 50)
            print("YOUR ORDER STATUS".center(50))
            print("=" * 50)
            
            # Filter and display only menu items with status
            menu_items = []
            in_order_section = False
            item_index = 1
            
            for line in lines:
                line = line.strip()
                if line.startswith("Orders:"):
                    in_order_section = True
                elif line.startswith("====="):
                    in_order_section = False
                elif in_order_section and line and not line.startswith("[Done]"):
                    print(f"{item_index}. {line}")
                    menu_items.append(line)
                    item_index += 1
            
            if not menu_items:
                print("No active orders found!")
                
    except FileNotFoundError:
        print("No orders have been placed yet!")

def main():
    print("Welcome to Order Status Checker")
    while True:
        display_order_status()
        
        choice = input("\nPress Enter to refresh status or type 'exit' to quit: ")
        if choice.lower() == 'exit':
            print("Thank you for checking your order status. Goodbye!")
            break

if __name__ == "__main__":
    main()