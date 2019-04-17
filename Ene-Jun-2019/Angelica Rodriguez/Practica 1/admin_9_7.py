"""
9-7. Admin: An administrator is a special kind of user. Write a class called
Admin that inherits from the User class you wrote in Exercise 9-3 (page 166)
or Exercise 9-5 (page 171). Add an attribute, privileges, that stores a list
of strings like "can add post", "can delete post", "can ban user", and so on.
Write a method called show_privileges() that lists the administrator’s set of
privileges. Create an instance of Admin, and call your method.
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
        self.privileges = []

    def store_privileges(self, *privileges_list):
        """Set privileges in a list"""
        self.privileges = privileges_list
        return self

    def get_privileges(self):
        """See the privileges stored in the list"""
        for privilege in self.privileges:
            print(privilege)

# Create three users and call methods
u1 = User('Maria', 'Lopez', 'maria_lopez', 'password1')
print("First User")
print(u1.describe_user())
print(u1.greet_user())

u2 = User('Juan', 'Perez', 'juan_perez', 'password2')
print("\nSecond User")
print(u2.describe_user())
print(u2.greet_user())

admin1 = Admin('Angelica', 'Rodriguez', 'angelica_rodriguez', 'aRodriguez')
print("\nThird User")
print(admin1.describe_user())
print(admin1.greet_user())
print("\nPrivileges of third user")
admin1.store_privileges('can add users', 'can delete users', 'can be user')
admin1.get_privileges()
