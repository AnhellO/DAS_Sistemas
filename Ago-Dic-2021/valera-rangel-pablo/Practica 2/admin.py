from user1 import Users
class Admin(Users):
    def __init__(self, first_name, last_name, age, location):
        super().__init__(first_name, last_name, age, location)
        self.privileges = []

    def show_privileges(self):
        for privilege in self.privileges:
            print(f'This user can: {privilege}')


class Privileges():
    def __init__(self, privileges=[]):
        self.privileges = privileges

    def show_privileges(self):
        if self.privileges:
            for privilege in self.privileges:
                print(f'This user can: {privilege}')
        else:
            print('This user don´t have privileges')
