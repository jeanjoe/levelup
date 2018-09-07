from models.database import DatabaseConnection

database = DatabaseConnection()

if __name__ == "__main__":

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
        print("[7] - Get a User")
        print("[8] - Get an Event")
        print("[9] - Update Ticket")
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
            print("--------------------------------------------------------------------------------------")
            print("ID \t|Firstame \t|Lastname \t\t|Age \t|Email \t\t|Password \t|Created_at")
            print("--------------------------------------------------------------------------------------")
            for row in users:
                print("{} \t|{} \t|{} \t|{} \t|{} \t\t|{} \t|{}".format(row[0], row[1], row[2], row[3], row[4], row[5], row[6]))

        elif selector == "3":
            """Assign event ticket to user."""
            #Get user id and check if it exists
            user_id = input("Enter user ID: ")
            check_user = database.search_data("users", "id", user_id)
            if check_user:
                
                #Get event id and check if it exists
                event_id = input("Enter Event ID: ")
                check_event = database.search_data("events", "id", event_id)
                if check_event:
                    verification_code = input("Enter 5 Digit verification code: ")
                    print(database.add_new_ticket(user_id, event_id, verification_code))
                else:
                    print("Event Not Found")
            else:
                print("User Not Found")

        elif selector == "5":
            """Get all tickets."""
            events = database.get_all_events()
            print("All Registered Users.")
            print("--------------------------------------------------------------------------------------")
            print("ID \t|Name \t\t|Price \t|Location \t|Created at")
            print("--------------------------------------------------------------------------------------")
            for row in events:
                print("{} \t|{} \t\t|{} \t|{} \t|{}".format(row[0], row[1], row[2], row[3], row[4]))

        elif selector == "6":
            """Get all tickets."""
            tickets = database.get_all_tickets()
            print("All Registered Users.")
            print("--------------------------------------------------------------------------------------")
            print("ID \t|USER \t\t|EVENT \t|VALID \t|CODE \t|CREATED AT")
            print("--------------------------------------------------------------------------------------")
            for row in tickets:
                print("{} \t|{} \t\t|{} \t|{} \t|{} \t{}".format(row[0], row[1], row[2], row[3], row[4], row[5]))

        elif selector == "7":
            #Get user id and check if it exists
            user_id = input("Enter user ID: ")
            check_user = database.search_data("users", "id", user_id)
            if check_user:
                print("User Details.")
                print("--------------------------------------------------------------------------------------")
                print("ID \t|Firstname \t|Lasname \t|Age \t|Password \t|Email \t|Created_at")
                print("--------------------------------------------------------------------------------------")
                print("{} \t|{} \t{} \t\t|{} \t|{} \t{}".format(check_user[0], check_user[1], check_user[2], check_user[3], check_user[5], check_user[4]))
            else:
                print("User Not Found")

        elif selector == "8":
            pass

        elif selector == "9":
            pass

        elif selector == "0":
            """Break the loop."""
            print("You Exited!")
            break

        else:
            print("\nPlease Select a valid MENU ID.")