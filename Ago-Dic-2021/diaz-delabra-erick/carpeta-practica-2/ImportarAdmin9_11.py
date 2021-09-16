class Usuario():
    def __init__(self, nombre, apellido, username, email, ubi):
        self.nombre = nombre.title()
        self.apellido = apellido.title()
        self.username = username
        self.email = email
        self.ubi = ubi.title()

    def describe_user(self):
        print("\nNombre: " + self.nombre + " " + self.apellido)
        print("  Username: " + self.username)
        print("  Email: " + self.email)
        print("  Ciudad: " + self.ubi)

    def greet_user(self):
        print("\nBienvenido: " + self.username)

class Admin(Usuario):
    def __init__(self, nombre, apellido, username, email, ubi):
        super().__init__(nombre, apellido, username, email, ubi)
        self.Privilegios = Privilegios([])
    
class Privilegios():
    def __init__(self, Privilegios):
        self.priv1 = Privilegios
    def show_Privilegios(self):
        for priv1 in self.Privilegios:
            print(priv1)