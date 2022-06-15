"""9-5. Login Attempts:

Add an attribute called login_attempts to your User
class from Exercise 9-3 (page 166) . Write a method called increment_
login_attempts() that increments the value of login_attempts by 1 . Write
another method called reset_login_attempts() that resets the value of login_
attempts to 0 .
Make an instance of the User class and call increment_login_attempts()
several times . Print the value of login_attempts to make sure it was incremented
properly, and then call reset_login_attempts() . Print login_attempts again to
make sure it was reset to 0 """

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

Alexa = User('Alexa', 'Cazarez', 'Alex', 'Alex@hotmail.com', '844631126')
Alexa.describe_user()
Alexa.greet_user()

print("\n3 Intentos de login:")
Alexa.increment_login_attempts()
Alexa.increment_login_attempts()
Alexa.increment_login_attempts()
print(f"    Login attempts: {Alexa.login_attempts}")

print("Reseteo a intentos de login:")
Alexa.reset_login_attempts()
print(f"    Login attempts: {Alexa.login_attempts}")