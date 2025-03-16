# feedback.py
from tabulate import tabulate
import os

def main():
    print("--------------------------------")
    print("\n--- Feedback List ---")
    print("--------------------------------")
    print(" ")
    
    script_dir = os.path.dirname(os.path.abspath(__file__))
    project_root = os.path.dirname(script_dir) 
    feedback_file = os.path.join(project_root, 'feedbacks.txt')
    
    try:
        with open(feedback_file, 'r') as file:
            feedbacks = file.readlines()
            if not feedbacks:
                print("No any feedback")
            else:
                table_data = []
                for feedback in feedbacks:
                    feedback = feedback.strip()
                    if feedback:
                        try:
                            timestamp = feedback[1:20]
                            rest = feedback[22:]
                            username = rest.split(" | ")[0].split(": ")[1]
                            feedback_text = rest.split(" | ")[1].split(": ")[1]
                            table_data.append([timestamp, username, feedback_text])
                        except IndexError:
                            print(f"Skipping malformed feedback entry: {feedback}")
                            continue
                
                if table_data:
                    headers = ["Timestamp", "Customer", "Feedback"]
                    print(tabulate(table_data, headers=headers, tablefmt="grid"))
                else:
                    print("No valid feedback entries found")
    
    except FileNotFoundError:
        print("No any feedback (file not found)")
    
    print(" ")
    input("Press Enter to continue...")

if __name__ == "__main__":
    main()