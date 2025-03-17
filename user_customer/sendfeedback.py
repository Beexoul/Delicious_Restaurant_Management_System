import json
import os
from datetime import datetime

def save_feedback(username, feedback):
    feedback_data = {
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "username": username,
        "feedback": feedback
    }
    
    script_dir = os.path.dirname(os.path.abspath(__file__))
    project_root = os.path.dirname(script_dir)
    feedback_file = os.path.join(project_root, "User_Data", "feedbacks.json")
    
    if os.path.exists(feedback_file):
        with open(feedback_file, 'r') as file:
            feedbacks = json.load(file)
    else:
        feedbacks = []
    
    feedbacks.append(feedback_data)
    
    with open(feedback_file, 'w') as file:
        json.dump(feedbacks, file, indent=4)
    
    print("Feedback submitted successfully!")

def main(logged_in_username):
    print("--------------------------------")
    print("\n--- Submit Feedback ---")
    print("--------------------------------")
    print(f"\nSubmitting feedback as: {logged_in_username}")
    print(" ")
    
    feedback = input("Enter your feedback: ")
    if not feedback.strip():
        print("Feedback cannot be empty. Returning to menu...")
        return
    
    save_feedback(logged_in_username, feedback)
    print("Thank you for your feedback! Returning to the menu...")
    input("Press Enter to continue...")

#done