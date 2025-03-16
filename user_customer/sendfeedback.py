# sendfeedback.py
from datetime import datetime

def save_feedback(feedback):
    with open('feedbacks.txt', 'a') as file:
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        file.write(f"[{timestamp}] {feedback}\n")
    print("Feedback submitted successfully!")

def main():
    print("--------------------------------")
    print("\n--- Submit Feedback ---")
    print("--------------------------------")
    print(" ")
    
    while True:
        feedback = input("Enter your feedback (or type 'exit' to finish): ")
        if feedback.lower() == 'exit':
            break
        save_feedback(feedback)
    
    print("Thank you for your feedback! Returning to the menu...")
    input("Press Enter to continue...")

if __name__ == "__main__":
    main()