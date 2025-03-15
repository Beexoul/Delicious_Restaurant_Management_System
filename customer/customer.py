import customerprofile
import sendfeedback
import orderstatus
import order
def main():
    while True:
        print("\n1. Profile")
        print("2. Place Order")
        print("3. Check Order Status")
        print("4. Give Feedback")
        print("5. Back to Main Menu")

        choice = input("Enter your choice: ")

        if choice == "1":
            customerprofile.main()
        elif choice == "2":
            order.main()
        elif choice == "3":
            orderstatus.main()
        elif choice == "4":
            sendfeedback.main()
        elif choice == "5":
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
