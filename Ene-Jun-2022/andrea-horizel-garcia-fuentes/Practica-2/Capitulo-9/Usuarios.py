class Usuario():

#9.3 Usuarios
    

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

#9.7 Administrador 
class Admin(Usuario):
   def __init__(self, primer_nombre, apellido, nomusario, correo, localidad):
        super().__init__(primer_nombre, apellido, nomusario, correo, localidad)
        self.privileges = Privileges()

  

#9.8 Privilegios
class Privileges():
    def __init__(self, privileges=[]):
        self.privileges = privileges

    def show_privileges(self):
        print("\nPrivileges:")
        for privilege in self.privileges:
            print("- " + privilege)
        
Andrea = Admin('Andrea', 'garcia', 'a_garcia', 'a_garcia@example.com', 'Saltillo')
Andrea.describe_Usuario()
Andrea.greet_usuario()

Andrea.privileges.privileges= [
    'can delet user',
    'can add post',
    'can reset passwords',
    ]

Andrea.privileges.show_privileges()

Justin = Usuario('Justin', 'hamburguesas', 'JustinHamburguesas', 'JH@example.com', 'Saltillo')
Justin.describe_Usuario()
Justin.greet_usuario()

#9.5 intentos de inicio de sesión

print("\nCrear 3 login attempts...")
Andrea.increment_login_attempts()
Andrea.increment_login_attempts()
Andrea.increment_login_attempts()
print("  Login attempts: " + str(Andrea.login_attempts))

print("Reinicar login attempts...")
Andrea.reset_login_attempts()
print("  Login attempts: " + str(Andrea.login_attempts))
