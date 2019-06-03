#Write a separate Privileges class. The class should have one
#attribute, privileges, that stores a list of strings as described in Exercise 9-7.
#Move the show_privileges() method to this class. Make a Privileges instance
#as an attribute in the Admin class. Create a new instance of Admin and use your
#method to show its privileges.
class User():

    def __init__(self, first_name, last_name, username, email, location):
        """Iniciar usuario."""
        self.first_name = first_name.title()
        self.last_name = last_name.title()
        self.username = username
        self.email = email
        self.location = location.title()
        self.login_attempts = 0

    def describe_user(self):
        """Informacion de usuario"""
        print("\n" + self.first_name + " " + self.last_name)
        print("  Username: " + self.username)
        print("  Email: " + self.email)
        print("  Location: " + self.location)

    def greet_user(self):
        """Saludo al usuario"""
        print("\nBienvenido/a, " + self.username + "!")

    def increment_login_attempts(self):
        """Incrementando cuentas"""
        self.login_attempts += 1

    def reset_login_attempts(self):
        """Restablecer cuentas a 0"""
        self.login_attempts = 0


class Admin(User):
    """Usuario con privilegios administrativos."""

    def __init__(self, first_name, last_name, username, email, location):
        """Iniciando administrador"""
        super().__init__(first_name, last_name, username, email, location)

        #Iniciar conjunto vacio de privilegios
        self.privileges = Privileges()

class Privileges():
    """Almacenando privilegios de administrador"""

    def __init__(self, privileges=[]):
        self.privileges = privileges

    def show_privileges(self):
        print("\nPrivilegios:")
        if self.privileges:
            for privilege in self.privileges:
                print("- " + privilege)
        else:
            print("- Este usuario no tiene privilegios.")


noemi = Admin('noemi', 'flores', 'noemi_flores', 'noemi_flores@uadec.edu.mx', 'Saltillo')
noemi.describe_user()

noemi.privileges.show_privileges()

print("\nAgregando privilegios...")
noemi_privileges = [
    'Restablecer contraseñas ',
    'Cancelar cuentas',
    ]
noemi.privileges.privileges = noemi_privileges
noemi.privileges.show_privileges()