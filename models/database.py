import psycopg2

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
            self.cursor = self.conn.cursor()
            print("Connection established")
        except Exception as ex:
            print("Unable to connect")
            print(ex)
