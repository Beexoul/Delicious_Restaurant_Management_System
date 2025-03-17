from user_manager import managecustomer
from user_manager import manageitem
from user_manager import managemenu
from user_manager import managerprofile

def main():
    while True:
        print("\n1. Manage Customer")
        print("2. Manage Item")
        print("3. Manage Menu")
        print("4. Manage Profile")
        print("5. Back to Main Menu")

        choice = input("Enter your choice: ")

        if choice == "1":
            managecustomer.main()
        elif choice == "2":
            manageitem.main()
        elif choice == "3":
            managemenu.main()
        elif choice == "4":
            managerprofile.main()
        elif choice == "5":
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()

#done