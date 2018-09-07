
class User:

    def __init__(self, users_list = []):
        self.users_list = users_list

    def add_user(self, name, email, password):
        """Search user and add if not exists."""
        if self.search_user(name):
            return False
        user = {
            "name": name,
            "email": email,
            "password": password
        }
        self.users_list.append(user)
        return user

    def get_all_users(self):
        """Return a list of All users."""
        return self.users_list

    def delete_user(self,name):
        """Search user if exists remove from list."""
        search_result = self.search_user(name)
        if search_result:
            self.users_list.remove(search_result[0])
            return search_result
        return None

    def search_user(self, name):
        """Search user from list using name."""
        user = [user for user in self.users_list if user['name'] == name]
        if user:
            return user
        return None