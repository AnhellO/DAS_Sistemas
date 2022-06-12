class Usuario():

    def __init__(self, primer_nombre, apellido, nomusario, correo, localidad):
        
        self.primer_nombre = primer_nombre.title()
        self.apellido = apellido.title()
        self.nomusario = nomusario
        self.correo = correo
        self.localidad = localidad.title()
        self.login_attempts = 0

    def describe_Usuario(self):
        print("\n" + self.primer_nombre + " " + self.apellido)
        print("  nomusario: " + self.nomusario)
        print("  correo: " + self.correo)
        print("  Localidad: " + self.localidad)

    def greet_usuario(self):
        print("\n bienvenidos, " + self.nomusario + "!")

    def increment_login_attempts(self):
         self.login_attempts += 1

    def reset_login_attempts(self):
         self.login_attempts = 0    

class Admin(Usuario):
   def __init__(self, primer_nombre, apellido, nomusario, correo, localidad):
        super().__init__(primer_nombre, apellido, nomusario, correo, localidad)
        self.privileges = Privileges()

class Privileges():
    def __init__(self, privileges=[]):
        self.privileges = privileges

    def show_privileges(self):
        print("\nPrivileges:")
        for privilege in self.privileges:
            print("- " + privilege)        

