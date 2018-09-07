from models.database import DatabaseConnection

database = DatabaseConnection()

while True:
    print("\n====================================================")
    print("\t WELCOME TO EVENT MANAGEMENT SYSTEM")
    print("====================================================\n")
    print("SELECT MENU ITEM")
    print("[1] - Add new user")
    print("[2] - Add New Event")
    print("[3] - Add Ticket")
    print("[4] - Get all users")
    print("[0] - Exit")

    selector = input(":")
    print(selector)
    if selector == "1":
        """Insert New User."""
        first_name = input("Enter your first name: ")
        last_name = input("Enter your last name: ")
        email = input("Enter a valid Email address: ")
        age = input("Enter your age: ")
        password = input("Enter your password: ")

        print(database.add_new_user(first_name, last_name, email, age, password))

    elif selector == "2":
        """Insert New Event."""
        event_name = input("Enter Event name: ")
        event_price = input("Enter Event price: ")
        event_location = input("Enter Event location: ")

        print(database.add_new_event(event_name, event_price, event_location))
    else:
        print("Print Select a valid menu.")