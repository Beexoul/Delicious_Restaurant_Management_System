# sendfeedback.py
from datetime import datetime

def save_feedback(username, feedback):
    with open('feedbacks.txt', 'a') as file:
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        file.write(f"[{timestamp}] Customer: {username} | Feedback: {feedback}\n")
    print("Feedback submitted successfully!")

def main():
    print("--------------------------------")
    print("\n--- Submit Feedback ---")
    print("--------------------------------")
    print(" ")
    
    username = input("Enter your username: ")
    if not username.strip():
        print("Username cannot be empty. Returning to menu...")
        return
    
    print(f"Submitting feedback as: {username}")
    print(" ")
    
    feedback = input("Enter your feedback: ")
    if not feedback.strip():
        print("Feedback cannot be empty. Returning to menu...")
        return
    
    save_feedback(username, feedback)
    print("Thank you for your feedback! Returning to the menu...")
    input("Press Enter to continue...")

if __name__ == "__main__":
    main()