#An administrator is a special kind of user. Write a class called
#Admin that inherits from the User class you wrote in Exercise 9-3 (page 166)
#or Exercise 9-5 (page 171). Add an attribute, privileges, that stores a list
#of strings like "can add post", "can delete post", "can ban user", and so on.
#Write a method called show_privileges() that lists the administrator’s set of
#privileges. Create an instance of Admin, and call your method.
class User():

    def __init__(self, first_name, last_name, username, email, location):
        """Iniciar usuario"""
        self.first_name = first_name.title()
        self.last_name = last_name.title()
        self.username = username
        self.email = email
        self.location = location.title()
        self.login_attempts = 0

    def describe_user(self):
        """Informacion del usuario"""
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
    """Usuario con privilegios administrativos"""
    def __init__(self, first_name, last_name, username, email, location):
        """Iniciando administrador."""
        super().__init__(first_name, last_name, username, email, location)
        self.privileges = []

    def show_privileges(self):
        """Mostrando privilegios de administrador"""
        print("\nPrivilegios:")
        for privilege in self.privileges:
            print("- " + privilege)


noemi = Admin('noemi', 'flores', 'noemi_flores', 'noemi_flores@uadec.edu.mx', 'Saltillo')
noemi.describe_user()

noemi.privileges = [
    'Restablecer contraseñas ',
    'Cancelar cuentas',
    ]

noemi.greet_user()
noemi.show_privileges()