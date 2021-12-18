class User():
    
    def __init__(self, Name, LastName, ID, Mail, Phone):
        self.Name = Name
        self.LastName = LastName
        self.ID = ID
        self.Mail = Mail
        self.Phone = Phone
        
    def Describe_U(self):
        s = "\nName: " + self.Name + " "+self.LastName + "\nID: "+self.ID
        s += "\nInfo contacto\nPhone: " + self.Phone + " Mail: " + self.Mail
        print(s)
    
    def Greet_U(self):
        s = "\nWelcome " + self.Name + " " + self.LastName + "\n"
        print(s)

Usuarios = []
Usuarios.append(User("Omar","Padilla","1","omarpadilla@mail.com","1234567890"))
Usuarios.append(User("Diego","Castillo","2","castillo117@mail.com","0987654321"))
Usuarios.append(User("Fernanda","Cisneros","3","fercis@mail.com","7894561230"))
Usuarios.append(User("Alejandra","Sanchez","4","alesa19@mail.com","3692581470"))
Usuarios.append(User("Armando","Garces","5","chivascampeon@mail.com","4561237890"))

for i in Usuarios:
    i.Describe_U()
    i.Greet_U()