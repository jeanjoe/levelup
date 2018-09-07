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
        print("[9] - Get a Ticket")
        print("[10] - Update User")
        print("[11] - Update EVent")
        print("[12] - Update Ticket")
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
            if users:
                print("All Registered Users.")
                print("--------------------------------------------------------------------------------------")
                print("ID \t|Firstame \t|Lastname \t\t|Age \t|Email \t\t|Password \t|Created_at")
                print("--------------------------------------------------------------------------------------")
                for row in users:
                    print("{} \t|{} \t|{} \t|{} \t|{} \t\t|{} \t|{}".format(row[0], row[1], row[2], row[3], row[4], row[5], row[6]))
            else:
                print("No users have been registered")

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
            """Get all Events."""
            events = database.get_all_events()
            if events:
                print("All Events.")
                print("--------------------------------------------------------------------------------------")
                print("ID \t|Name \t\t|Price \t|Location \t|Created at")
                print("--------------------------------------------------------------------------------------")
                for row in events:
                    print("{} \t|{} \t\t|{} \t|{} \t|{}".format(row[0], row[1], row[2], row[3], row[4]))
            else:
                print("No Events have been created")

        elif selector == "6":
            """Get all tickets."""
            tickets = database.get_all_tickets()
            if tickets:
                print("Event Tickets.")
                print("--------------------------------------------------------------------------------------")
                print("ID \t|USER \t\t|EVENT \t|VALID \t|CODE \t|CREATED AT")
                print("--------------------------------------------------------------------------------------")
                for row in tickets:
                    print("{} \t|{} \t\t|{} \t|{} \t|{} \t{}".format(row[0], row[1], row[2], row[3], row[4], row[5]))
            else:
                print("No event tickets assigned users.")

        elif selector == "7":
            """Get a user."""
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
            """Get an Event."""
            event_id = input("Enter event ID: ")
            check_event = database.search_data("events", "id", event_id)
            if check_event:
                print("Event Details.")
                print("--------------------------------------------------------------------------------------")
                print("ID \t|Name \t\t|Price \t|Location \t|Created at")
                print("--------------------------------------------------------------------------------------")
                print("{} \t|{} \t\t|{} \t|{} \t|{}".format(check_event[0], check_event[1], check_event[2], check_event[3], check_event[4]))
            else:
                print("Event Not Found")

        elif selector == "9":
            """Get a Ticket."""
            print("Get a Ticket.")
            ticket_id = input("Enter Ticket ID: ")
            check_ticket = database.search_data("tickets", "id", ticket_id)
            if check_ticket:
                print("Ticket Details.")
                print("--------------------------------------------------------------------------------------")
                print("ID \t|USER \t\t|EVENT \t|VALID \t|CODE \t|CREATED AT")
                print("--------------------------------------------------------------------------------------")
                print("{} \t|{} \t\t|{} \t|{} \t|{} \t|{}".format(check_ticket[0], check_ticket[1], check_ticket[2], check_ticket[3], check_ticket[4], check_ticket[5]))
            else:
                print("Ticket Not Found")

        elif selector == "0":
            """Break the loop."""
            print("You Exited!")
            break

        elif selector == "10":
            """Update User Detail."""
            user_id = input("Enter user ID")

            check_user = database.search_data("users", "id", user_id)
            if check_user:
                print("Update {} Details ".format(check_user[1]))
                first_name = input("Enter your first name: ")
                last_name = input("Enter your last name: ")
                email = input("Enter a valid Email address: ")
                age = input("Enter your age: ")
                password = input("Enter your password: ")

                print(database.update_user(user_id, first_name, last_name, email, age, password))

            else:
                print("Cannot find User with ID '{}'.".format(user_id))

        elif selector == "11":
            """Update Events details."""
            event_id = input("Enter Event ID")

            check_event = database.search_data("events", "id", event_id)

            if check_event:
                print("Update Event {} details".format(check_event[1]))
                event_name = input("Enter Event name: ")
                event_price = input("Enter Event price: ")
                event_location = input("Enter Event location: ")

                print(database.update_event(event_id, event_name, event_price, event_location))
            else:
                print("Unable to find Event with this ID '{}' ".format(event_id))

        elif selector == "12":
            """Update Tickets details."""
            ticket_id = input("Enter Ticket ID")
            check_ticket = database.search_data("tickets", "id", ticket_id)

            if check_ticket:
                print("Update Ticket Details for User {} Event {} ".format(check_ticket[1], check_ticket[2]))
                user_id = input("Enter user ID: ")
                check_user = database.search_data("users", "id", user_id)
                if check_user:
                    
                    #Get event id and check if it exists
                    event_id = input("Enter Event ID: ")
                    check_event = database.search_data("events", "id", event_id)
                    if check_event:
                        verification_code = input("Enter 5 Digit verification code: ")
                        print(database.update_ticket(ticket_id, user_id, event_id, verification_code))
                    else:
                        print("Event Not Found")
                else:
                    print("User Not Found")
            else:
                print("Unable to find ticket with ID {} ")

        else:
            print("\nPlease Select a valid MENU ID.")