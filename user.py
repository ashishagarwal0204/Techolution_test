from storage import JSONStorage

class User:
    def __init__(self, name, user_id):
        self.name = name
        self.user_id = user_id

class UserManager:
    def __init__(self, filename):
        self.storage = JSONStorage(filename)
        self.users = self.storage.load_data()

    def add_user(self, name, user_id):
        user = User(name, user_id)
        self.users.append(user)
        self.storage.save_data([user.__dict__ for user in self.users])

    def list_users(self):
        for user in self.users:
            print(f"Name: {user.name}, User ID: {user.user_id}")
