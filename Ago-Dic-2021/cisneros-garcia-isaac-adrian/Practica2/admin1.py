from user1 import User
class Admin(User):
    
    def __init__(self, first_name, last_name, username, email, location):
        super().__init__(first_name, last_name, username, email, location)
        self.privileges = Privileges()

class Privileges():

    def __init__(self, privileges=[]):
        self.privileges = privileges

    def show_privileges(self):
        print("\n ---Privilegios:--- \n")
        if self.privileges:
            for privilege in self.privileges:
             print(f"- {privilege}")
        else:
         print("- El usurio no tiene privilegios.")