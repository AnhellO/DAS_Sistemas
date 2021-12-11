class User():
    
    def __init__(self, Name, LastName, ID, Mail, Phone):
        self.Name = Name
        self.LastName = LastName
        self.ID = ID
        self.Mail = Mail
        self.Phone = Phone
        
    def Describe_U(self):
        s="\nName: " + self.Name + " " + self.LastName + "\nID: " + self.ID + "\nInfo\nPhone: " + self.Phone + "Mail: " + self.Mail
        print(s)
    
    def Greet_U(self):
        s = "\nWelcome " + self.Name+" " + self.LastName + "\n"
        print(s)

class Privileges():
    
    def __init__(self):
        self.list = ["Ban User","Create Post","Close Post","Add User"]

    def show_privileges(self):
        for i in self.list:
            print(i)
            
class Admin(User):
    
    def __init__(self, Name, LastName, ID, Mail, Phone):
        super().__init__(Name, LastName, ID, Mail, Phone)
        self.privileges = Privileges()