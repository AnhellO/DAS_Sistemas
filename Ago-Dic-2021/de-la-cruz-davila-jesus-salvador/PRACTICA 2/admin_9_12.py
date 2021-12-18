from user_9_12 import User

class Admin(User):
    def __init__(self, first_name, last_name, username, email, number, age):
        super().__init__(first_name, last_name, username, email, number, age)
        
        self.privileges = Privileges([])
        

class Privileges():
    def __init__(self, privileges):
        self.priveleges = privileges
        
    def show_privileges(self):
        print("\nPrivilegios")
        for privilege in self.priveleges:
            print("- ", privilege)
        print("\n")