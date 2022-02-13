"""9-8. Privileges:

Write a separate Privileges class . The class should have one
attribute, privileges, that stores a list of strings as described in Exercise 9-7 .
Move the show_privileges() method to this class . Make a Privileges instance
as an attribute in the Admin class . Create a new instance of Admin and use your
method to show its privileges."""

class User():
    def __init__(self, first_name, last_name, username, email, number):
        self.first_name = first_name.title()
        self.last_name = last_name.title()
        self.username = username
        self.email = email
        self.number = number.title()
        self.login_attempts = 0

    def describe_user(self):
        print(f"\n{self.first_name} {self.last_name}")
        print(f"  Username: {self.username}")
        print(f"  Email: {self.email}")
        print(f"  Number: {self.number}")

    def greet_user(self):
        print(f"\n Hola {self.username} que tengas un excelente dia!")

    def increment_login_attempts(self):
        self.login_attempts += 1

    def reset_login_attempts(self):
        self.login_attempts = 0

class Admin(User):
    def __init__(self, first_name, last_name, username, email, number):
        super().__init__(first_name, last_name, username, email, number)
        self.privileges = Privileges()

class Privileges():
    def __init__(self, privileges=[]):
        self.privileges = privileges

    def show_privileges(self):
        print("\nPrivilegios:")
        if self.privileges:
            for privilege in self.privileges:
                print(f"- {privilege}")
        else:
            print("Este usuario no cuenta con privilegios.")

Alexa = Admin('Alexa', 'Cazarez', 'Alex', 'Alex@hotmail.com', '844631126')
Alexa.describe_user()
Alexa.privileges.show_privileges()

print("\nAñadiendo privilegios:")
Alexa_privileges = [
    'can add post',
    'can delete post',
    'can ban user',
    ]

Alexa.privileges.privileges = Alexa_privileges
Alexa.privileges.show_privileges()