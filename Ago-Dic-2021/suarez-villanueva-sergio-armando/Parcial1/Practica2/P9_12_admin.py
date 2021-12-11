from P9_12_user import User
class Privileges():
    
    def __init__(self):
        self.list = ["Ban User","Create Post","Close Post","Add User"]

    def show_privileges(self):
        for i in self.list:
            print(i)
            
class Admin(User):
    
    def __init__(self, Name, LastName, ID, Mail, nPhone):
        super().__init__(Name, LastName, ID, Mail, nPhone)
        self.privileges=Privileges()