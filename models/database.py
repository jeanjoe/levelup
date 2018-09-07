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
        try:
            query = """
            INSERT INTO users (first_name, last_name, age, email, password, created_at) VALUES 
            ('{}', '{}', '{}', '{}', '{}', '{}')
            """.format(first_name, last_name, age, email, password, datetime.datetime.now())
            self.cursor.execute(query)
            return "New User created succesffuly"
        except Exception as ex:
            return "Error occured {}".format(ex)