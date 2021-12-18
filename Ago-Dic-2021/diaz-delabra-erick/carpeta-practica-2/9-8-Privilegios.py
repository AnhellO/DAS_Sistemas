class Usuario():
    def __init__(self, nombre, apellido, Username, email, ubi):
        self.nombre = nombre.title()
        self.apellido = apellido.title()
        self.Username = Username
        self.email = email
        self.ubi = ubi.title()

    def desc(self):
        print("\nNombe: " + self.nombre + " " + self.apellido)
        print("Username: " + self.Username)
        print("Email: " + self.email)
        print("Ciudad: " + self.ubi)
    def bienvenida(self):
        print("\nBienvenido: " + self.Username)

class Admin(Usuario):
    def __init__(self, nombre, apellido, Username, email, ubi):
        super().__init__(nombre, apellido, Username, email, ubi)
        self.privilegios = Privilegios()

class Privilegios():
    def __init__(self, privilegios=[]):
        self.privilegios = privilegios
    def mostrarp(self):
        print("\nPrivilegios:")
        if self.privilegios:
            for priv in self.privilegios:
                print(priv)
        else:
            print("No tiene privilegios.")

u1 = Admin('Erick', 'Diaz', 'erickgames', 'erickdiaz@uadec.edu.mx', 'Saltiyork')
u1.desc()
u1.privilegios.mostrarp()
print("\n\nAñadir privilegios:\n")
u1_Privilegios = ['Puede añadir posts','Puede banear usuarios','Puede ver las ubicaciones','Puede borrar cosas',]
u1.privilegios.privilegios = u1_Privilegios
u1.privilegios.mostrarp()