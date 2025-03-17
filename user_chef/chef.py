from user_chef import chefprofile
from user_chef import Request_ingredients
from user_chef import vieworder
from user_chef import updateorder

def main():
    while True:
        print("--------------------------------")
        print("\n_____Welcome Chef!______")
        print(" ")
        print(" ")
        print("1. View Order")
        print("2. Update Order")
        print("3. Request Ingredient")
        print("4. Profile")
        print("5. Logout")
        
        choice = input("Enter your choice: ")
        
        if choice == "1":
            vieworder.main()
        elif choice == "2":
            updateorder.main()
        elif choice == "3":
            Request_ingredients.main()
        elif choice == "4":
            chefprofile.main()
        elif choice == "5":
            print("Logging out.")
            print("..")
            print("...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()

#done