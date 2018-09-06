
class User:

    users_list = [
        {
            "username": "Manzede Benard",
            "email": "manzede@gmail.com",
            "password": "12345"
        },
        {
            "username": "Kyakulumbye Ahmad",
            "email": "kyakulumbye@gmail.com",
            "password": "555555"
        }
    ]

    def __init__(self):
        pass

    def add_user(self, name, email, password):
        user = {
            "name": name,
            "email": email,
            "password": password
        }
        self.users_list.append(user)
        return user

    def get_all_users(self):
        return self.users_list

    def delete_user(self,name):
        search_result = self.search_user(name)
        if search_result:
            self.users_list.remove(search_result[0])
            return search_result
        return None

    def search_user(self, name):
        user = [user for user in self.users_list if user['username'] == name]
        if user:
            return user
        return None