"""9-7. Admin:

An administrator is a special kind of user . Write a class called
Admin that inherits from the User class you wrote in Exercise 9-3 (page 166)
or Exercise 9-5 (page 171) . Add an attribute, privileges, that stores a list
of strings like "can add post", "can delete post", "can ban user", and so on.
Write a method called show_privileges() that lists the administrator’s set of
privileges. Create an instance of Admin, and call your method."""

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

"""Alexa = User('Alexa', 'Cazarez', 'Alex', 'Alex@hotmail.com', '844631126')
Alexa.describe_user()
Alexa.greet_user()

#       Ejemplos del texto
Alexa.privileges = [ 
    'can add post',
    'can delete post',
    'can ban user',
    ]

Alexa.show_privileges()
"""