""" Write a separate Privileges class. The class should have one
attribute, privileges, that stores a list of strings as described in Exercise 9-7.
Move the show_privileges() method to this class. Make a Privileges instance
as an attribute in the Admin class. Create a new instance of Admin and use your
method to show its privileges. """

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

class Privileges(object):
    """docstring for ."""
    def __init__(self):
        self.privileges = []

    def set_privileges(self, *privileges):
        self.privileges=privileges

    def show_privileges(self):
        """ method that lists the administrator’s set of privileges """
        print("\nEl administrador tiene los siguienes privilegios: ")
        for privilege in self.privileges:
            print("- "+ privilege)



class Admin(User):
    """Representa un tipo de usuario, especificamente un administrador ."""
    def __init__(self, first_name, last_name, age):
        super(Admin, self).__init__(first_name, last_name, age)
        self.privileges=Privileges()




administrador = Admin('pablo', 'garza', 21)
print(administrador.describe_user())
administrador.privileges.set_privileges('can add post', 'can delete post', 'can ban user')
administrador.privileges.show_privileges()
