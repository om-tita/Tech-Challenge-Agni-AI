import sys
from utils import text_summarizer
from models import User, Session, Event
from controllers import AuthController, MessageController, DepartmentController, EventController

def main():
    print("Welcome to Kurakani - Employee Communication App")
    # Initialize controllers
    auth_controller = AuthController()
    message_controller = MessageController()
    department_controller = DepartmentController()
    event_controller = EventController()

    # Main application loop
    while True:
        print("1. Login")
        print("2. Register")
        print("3. Exit")
        choice = input("Select an option: ")

        if choice == '1':
            employee_id = input("Enter Employee ID: ")
            phone_number = input("Enter Phone Number: ")
            auth_controller.login(employee_id, phone_number)
        elif choice == '2':
            # Registration logic
            pass
        elif choice == '3':
            print("Exiting the application...")
            sys.exit()
        else:
            print("Invalid choice. Please try again.")

if __name__ == '__main__':
    main()