from User import User
class Admin(User):
    def __init__(self, first_name, last_name):
        super().__init__(first_name, last_name)
        self.privileges = privileges()


class privileges():
    def __init__(self):
        self.privileges = {'Can add post','Can delete post','Can ban user'}

            
    def show_privileges(self):
        print('Privilegios del Admin:')
        for privilegio in self.privileges:
            print('- '+privilegio)

