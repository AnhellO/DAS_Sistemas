class Usuario():
    def __init__(self, nombre, apellido, Username, email, ubi):
        self.nombre = nombre.title()
        self.apellido = apellido.title()
        self.Username = Username
        self.email = email
        self.ubi = ubi.title()

    def describe_Usuario(self):
        print("\nNombre: " + self.nombre + " " + self.apellido)
        print("Username: " + self.Username)
        print("Email: " + self.email)
        print("Ciudad: " + self.ubi)
    def Bienvenida(self):
        print("\nBienvenido: " + self.Usuername)

class Admin(Usuario):
    def __init__(self, nombre, apellido, Username, email, ubi):
        super().__init__(nombre, apellido, Username, email, ubi)
        self.privilegios = []
    def privilegio(self):
        print("\n Privilegios:")
        for privilegios in self.privilegios:
            print(privilegios)

u1 = Admin('Erick', 'Diaz', 'erickgames', 'erickdiaz@uadec.edu.mx', 'saltiyork')
u1.describe_Usuario()
u1.privilegios = ['Puede añadir posts','Puede banear usuarios','Puede ver las ubicaciones','Puede borrar cosas',]
u1.privilegio()