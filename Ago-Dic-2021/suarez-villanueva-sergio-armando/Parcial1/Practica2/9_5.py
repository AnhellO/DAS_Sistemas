class User():
    
    def __init__(self, Name, LastName, ID, Mail, Phone):
        self.Name = Name
        self.LastName = LastName
        self.ID = ID
        self.Mail = Mail
        self.Phone = Phone
        self.LoginAtt = 0
        
    def Describe_U(self):
        s = "\nName: " + self.Name + " " + self.LastName + "\nID: " + self.ID + "\Info\nPhone: "+self.Phone+" Mail: "+self.Mail
        print(s)
    
    def Greet_U(self):
        s = "\nBienvenid@ " + self.Name + " " + self.LastName + "\n"
        print(s)
    
    def get_LoginAtt(self):
        print("LogIn Attemps: "+str(self.LoginAtt))
    
    def increment_LoginAtt(self):
        self.LoginAtt += 1
        
    def reset_LoginAtt(self):
        self.LoginAtt = 0
        
Usuario = User("Manuel","Padilla","1","manupadi@mail.com","7418529630")

Usuario.get_LoginAtt()
for i in range(25):
    Usuario.increment_LoginAtt()
    
Usuario.get_LoginAtt()
Usuario.reset_LoginAtt()
Usuario.get_LoginAtt()