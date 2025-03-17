from user_customer import customerprofile
from user_customer import sendfeedback
from user_customer import orderstatus
from user_customer import order

def main(logged_in_username):
    while True:
        print("\n--------------------------------------")
        print("Welcome to the Delicious Restaurant!")
        print("--------------------------------------")
        print(f"\n_____Welcome Customer {logged_in_username}!______")
        print(" ")
        print("\n1. Profile")
        print("2. Place Order")
        print("3. Check Order Status")
        print("4. Give Feedback")
        print("5. Logout")

        choice = input("Enter your choice: ")

        if choice == "1":
            customerprofile.main(logged_in_username)
        elif choice == "2":
            order.main(logged_in_username)
        elif choice == "3":
            orderstatus.main(logged_in_username)      
        elif choice == "4":
            sendfeedback.main(logged_in_username)
        elif choice == "5":
            print("Logging out.")
            print("..")
            print("...")
            break
        else:
            print("Invalid choice. Please try again.")

#done