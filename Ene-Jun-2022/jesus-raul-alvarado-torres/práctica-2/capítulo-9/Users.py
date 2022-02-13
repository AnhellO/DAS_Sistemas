"""9-3. Users:

Make a class called User. Create two attributes called first_name
and last_name, and then create several other attributes that are typically stored
in a user profile . Make a method called describe_user() that prints a summary
of the user’s information . Make another method called greet_user() that prints
a personalized greeting to the user .
Create several instances representing different users, and call both methods
for each user ."""

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

Raul = User('Raúl', 'Alvarado', 'Cachohuate', 'cachohuate80@hotmail.com', '8441264364')
Raul.describe_user()
Raul.greet_user()"""