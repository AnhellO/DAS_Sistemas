""" An administrator is a special kind of user. Write a class called
Admin that inherits from the User class you wrote in Exercise 9-3 (page 166)
or Exercise 9-5 (page 171). Add an attribute, privileges, that stores a list
of strings like "can add post", "can delete post", "can ban user", and so on.
Write a method called show_privileges() that lists the administrator’s set of
privileges. Create an instance of Admin, and call your method. """


class User(object):
    """Representa un usuario."""
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.login_attempts = 0

    def describe_user(self):
        """ method that prints a summary of the user’s information """
        description = "Nombre: " + self.first_name.title()+ "\nApellido: "+ self.last_name.title()+ "\nEdad: "+ str(self.age)
        return description

    def greet_user(self):
        """ method that prints a personalized greeting to the user"""
        print("¡Bienvenid@ " + self. first_name.title()+ ' '+self.last_name.title()+'!')

    def  increment_login_attempts(self):
        self.login_attempts+=1

    def reset_login_attempts(self):
        self.login_attempts=0

class Admin(User):
    """Representa un tipo de usuario, especificamente un administrador ."""
    def __init__(self, first_name, last_name, age):
        super(Admin, self).__init__(first_name, last_name, age)
        self.privileges = []

    def set_privileges(self, *privileges):
        self.privileges=privileges

    def show_privileges(self):
        """ method that lists the administrator’s set of privileges """
        print("\nEl administrador tiene los siguienes privilegios: ")
        for privilege in self.privileges:
            print("- "+ privilege)



usuario = User('karla', 'berlanga', 21)
print(usuario.describe_user())
usuario.greet_user()
print("\n")
print("Administrador")
administrador = Admin('pablo', 'garza', 21)
print(administrador.describe_user())
administrador.set_privileges('can add post', 'can delete post', 'can ban user')
administrador.show_privileges()
