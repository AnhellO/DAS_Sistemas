from onlyuser import User

class Admin(User):

    def __init__(self, first_name, last_name, age, localitation, login_attempts,privileges):
        super().__init__(first_name, last_name, age, localitation, login_attempts)
        self.privileges = Privileges(privileges)


class Privileges():

    def __init__(self, privileges):
        self.privileges = privileges

    def show_privileges(self):
        print(self.privileges) 