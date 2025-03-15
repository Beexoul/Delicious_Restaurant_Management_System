def main():
    print("\n--- Manage Users ---")
    print("1. List Users")
    print("2. Add User")
    print("3. Back")

    choice = input("Enter your choice: ")

    if choice == "1":
        print("\nUser List:")
        print("1. admin")
        print("2. chef")
        print("3. manager")
        print("4. customer")
    elif choice == "2":
        print("\nAdd User (not implemented yet, will be added soon ).")
    elif choice == "3":
        return
    else:
        print("Invalid choice.")

if __name__ == "__main__":
    main()