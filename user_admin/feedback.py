from tabulate import tabulate
import os
import json

def main():
    print("--------------------------------")
    print("\n--- Feedback List ---")
    print("--------------------------------")
    print(" ")
    
    script_dir = os.path.dirname(os.path.abspath(__file__))
    project_root = os.path.dirname(script_dir)
    feedback_file = os.path.join(project_root, "User_Data", "feedbacks.json")
    
    try:
        with open(feedback_file, 'r') as file:
            feedbacks = json.load(file)
            if not feedbacks:
                print("No feedback available.")
            else:
                table_data = [
                    [f["timestamp"], f["username"], f["feedback"]]
                    for f in feedbacks
                ]
                headers = ["Timestamp", "Customer_UserName", "Feedback"]
                print(tabulate(table_data, headers=headers, tablefmt="grid"))
    
    except FileNotFoundError:
        print("No feedback available (file not found).")
    except json.JSONDecodeError:
        print("Error reading feedback file. It may be corrupted.")
    
    print(" ")
    input("Press Enter to continue...")

if __name__ == "__main__":
    main()

#done