import psycopg2
import datetime

class DatabaseConnection:

    def __init__(self):
        try:
            self.conn = psycopg2.connect(
                database="level_up",
                user="postgres",
                password="manben",
                port="5433",
                host="localhost"
            )
            self.conn.autocommit = True
            self.cursor = self.conn.cursor()
            print("Connection established")
        except Exception as ex:
            print("Unable to connect")
            print(ex)

    def add_new_user(self, first_name, last_name, email, age, password):
        """Add new user to Database."""
        try:
            query = """
            INSERT INTO users (first_name, last_name, age, email, password, created_at) VALUES 
            ('{}', '{}', '{}', '{}', '{}', '{}')
            """.format(first_name, last_name, age, email, password, datetime.datetime.now())
            self.cursor.execute(query)
            return "New User created succesffuly"
        except Exception as ex:
            return "Error occured {}".format(ex)

    def get_all_users(self):
        """Get all users from database."""
        query = """
        SELECT * FROM users
        """
        self.cursor.execute(query)
        return self.cursor.fetchall()

    def add_new_event(self, name, price, location):
        """Insert New Event to the database."""
        try:
            query = """
            INSERT INTO events (name, price, location, created_at) VALUES 
            ('{}', '{}', '{}', '{}')
            """.format(name, price, location, datetime.datetime.now())
            self.cursor.execute(query)
            return "New Event created succesffuly"
        except Exception as ex:
            return "Error occured {}".format(ex)
    
    def get_all_events(self):
        """Get all events."""
        try:
            query = """
            SELECT * FROM events
            """
            self.cursor.execute(query)
            return self.cursor.fetchall()
        except Exception as ex:
            return "Unable to retrieve all Events - {}".format(ex)

    def get_all_tickets(self):
        """Get all tickets."""
        try:
            query = """
            SELECT * FROM tickets
            """
            self.cursor.execute(query)
            return self.cursor.fetchall()
        except Exception as ex:
            return "Unable to retrieve all Tickets - {}".format(ex)

    def search_data(self, table, field, data):
        """Search data from the provided table."""
        try:
            query =  """
            SELECT * FROM {} WHERE {}='{}'
            """.format(table, field, data)
            self.cursor.execute(query)
            return self.cursor.fetchone()   
        except Exception as ex:
            return "Error occured {}".format(ex)

    def add_new_ticket(self, user_id, event_id, verification_code):
        """Assign event ticket to user."""
        try:
            query = """
            INSERT INTO tickets (user_id, event_id, is_valid, verification_code, created_at) VALUES 
            ('{}', '{}', '{}', '{}', '{}')
            """.format(user_id, event_id, 1, verification_code, datetime.datetime.now())
            self.cursor.execute(query)
            return "New Event ticket assigned to user succesffuly"
        except Exception as ex:
            return "Error occured {}".format(ex)