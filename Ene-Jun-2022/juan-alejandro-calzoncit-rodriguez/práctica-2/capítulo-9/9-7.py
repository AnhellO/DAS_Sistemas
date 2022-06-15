from user import User

class Admin(User):

    def __init__(self, first_name, last_name, age, localitation, login_attempts,privileges):
        super().__init__(first_name, last_name, age, localitation, login_attempts)
        self.privileges = privileges

    def show_privileges(self):
        print(self.privileges)


admn1 = Admin("Rodolfo", "Carranza", 32, "México", 8, ['can add post','can delete post','can ban user'])        

admn1.show_privileges()
