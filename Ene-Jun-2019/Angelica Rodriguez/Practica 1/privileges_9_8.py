""""
9-8. Privileges: Write a separate Privileges class. The class should have one
attribute, privileges, that stores a list of strings as described in Exercise
9-7. Move the show_privileges() method to this class. Make a Privileges instance
as an attribute in the Admin class. Create a new instance of Admin and use your
method to show its privileges.
"""

class User(object):
    def __init__(self, first_name, last_name, username, password):
        """Initialize attributes"""
        self.first_name = first_name
        self.last_name = last_name
        self.username = username
        self.password = password

    def describe_user(self):
        """Description of user profile"""
        return """
        First name: {}\nLast name: {}\nUsername: {}\nPassword: {}
        """.format(self.first_name, self.last_name,
                    self.username, self.password).strip()

    def greet_user(self):
        """Greets a user"""
        return "Welcome " + self.first_name + " " + self.last_name

class Admin(User):
    """Represent aspects of a User, specific to Admin"""

    def __init__(self, first_name, last_name, username, password):
        """
        Initialize attibutes of the parent class.
        Then initialize attibutes specific to an admin
        """
        super().__init__(first_name, last_name, username, password)
        self.privileges = Privileges()

class Privileges(object):
    """Represent privileges of users"""
    def __init__(self):
        self.privileges = []

    def store_privileges(self, *privileges_list):
        """Set privileges in a list"""
        self.privileges = privileges_list
        return self

    def get_privileges(self):
        """See the privileges stored in the list"""
        for privilege in self.privileges:
            print(privilege)

# create admin and print privileges
admin1 = Admin('Angelica', 'Rodriguez', 'angelica_rodriguez', 'aRodriguez')
admin1.privileges.store_privileges('update database', 'add users', 'remove users')
admin1.privileges.get_privileges()
