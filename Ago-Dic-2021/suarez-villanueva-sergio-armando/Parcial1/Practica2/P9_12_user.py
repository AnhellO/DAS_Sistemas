class User():
    
    def __init__(self, Name, LasName, ID, Mail, nPhone):
        self.Name = Name
        self.LasName = LasName
        self.ID = ID
        self.Mail = Mail
        self.nPhone = nPhone
        
    def Describe_U(self):
        s = "\nName: " + self.Name + " "+self.LasName + "\nID: " + self.ID + "\nInfo\nnPhone: " + self.nPhone + " Mail: " + self.Mail
        print(s)
    
    def Greet_U(self):
        s = "\nWelcome " + self.Name + " " + self.LasName + "\n"
        print(s)