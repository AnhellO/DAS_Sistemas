from user_module import Usuario

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
