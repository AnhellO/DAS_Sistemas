from user import User

class Admin(User):
    def __init__(self, first_name, last_name, id, username):
        super().__init__(first_name, last_name, id, username)
        self.privileges = Privileges()

class Privileges():
    def __init__(self, privileges = ['can add post', 'can delete post', 'can ban user']) -> None:
        self.privileges = privileges

    def show_privileges(self):
        for i in self.privileges:
            print(i)
