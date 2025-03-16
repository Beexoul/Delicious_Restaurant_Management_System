def view_orders():
    try:
        with open("orderfile.txt", "r") as file:
            orders = file.read()
            
            if not orders.strip():
                print("No orders yet!")
                return
                
            print("\n" + "=" * 50)
            print("CURRENT ORDERS".center(50))
            print("=" * 50)
            print(orders)
            
    except FileNotFoundError:
        print("No order file found yet! No orders have been placed.")

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