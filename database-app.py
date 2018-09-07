from models.database import DatabaseConnection

database = DatabaseConnection()

first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")
email = input("Enter a valid Email address: ")
age = input("Enter your age: ")
password = input("Enter your password: ")

print(database.add_new_user(first_name, last_name, email, age, password))