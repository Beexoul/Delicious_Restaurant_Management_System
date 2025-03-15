import manage_user
import view_reports
import feedback
import adminprofile

def main():
    while True:
        print("--------------------------------")
        print("\n_____Welcome Admin!______")
        print(" ")
        print(" ")
        print("1. Manage Users")
        print("2. View Reports")
        print("3. Provide Feedback")
        print("4. Admin Profile")
        print("5. Logout")
        
        choice = input("Enter your choice: ")
        
        if choice == "1":
            manage_user.main()
        elif choice == "2":
            view_reports.main()
        elif choice == "3":
            feedback.main()
        elif choice == "4":
            adminprofile.main()
        elif choice == "5":
            print("Logging out.")
            print("..")
            print("...")

            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()