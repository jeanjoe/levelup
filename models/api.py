import uuid

class Person(object):

    def __init__(self, name, email):
        self.name = name
        self.email = email

    def details(self):
        data = {
            "name": self.name,
            "email": self.email
        }
        return data

class User(Person):

    def __init__(self, name, email, password):
        super().__init__(name, email)
        self.password = password

    def details(self):
        data = {
            "id": str(uuid.uuid1()),
            "name": self.name,
            "email": self.email,
            "password":self.password
        }
        return data

class GuestList():

    def __init__(self, users_list = []):
        self.users_list = users_list

    def add_user(self, name, email, password):
        """Search user and add if not exists."""
        if self.search_user(name):
            return False
        user = User(name, email, password).details()
        self.users_list.append(user)
        return user

    def get_all_users(self):
        """Return a list of All users."""
        return self.users_list

    def delete_user(self,user_id):
        """Search user if exists remove from list."""
        get_user = [user for user in self.users_list if user['id'] == user_id]
        if get_user:
            self.users_list.remove(get_user[0])
            return get_user
        return None

    def search_user(self, name):
        """Search user from list using name."""
        user = [user for user in self.users_list if user['name'] == name]
        if user:
            return user
        return None