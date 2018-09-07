from models.database import DatabaseConnection

database = DatabaseConnection()

while True:
    print("\n====================================================")
    print("\t WELCOME TO EVENT MANAGEMENT SYSTEM")
    print("====================================================\n")
    print("SELECT MENU ITEM")
    print("[1] - Add New User")
    print("[2] - Add New Event")
    print("[3] - Add Ticket")
    print("[4] - Get all Users")
    print("[5] - Get all Events")
    print("[6] - Get all Tickets")
    print("[0] - Exit")

    selector = input(":")
    
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

    elif selector == "4":
        users = database.get_all_users()
        print("All Registered Users.")
        print("ID \tName \t\tAge \tEmail \t\tPassword \tCreated_at")
        for row in users:
            print("{} \t{} {} \t{} \t{} \t\t{} \t{}".format(row[0], row[1], row[2], row[3], row[4], row[5], row[6]))

    elif selector == "0":
        """Break the loop."""
        print("You Exited!")
        break

    else:
        print("Print Select a valid menu.")