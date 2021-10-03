class User():

    def __init__(self, first_name, last_name, username, email, location):
        self.first_name = first_name.title()
        self.last_name = last_name.title()
        self.username = username
        self.email = email
        self.login_attempts = 0

    def describe_user(self):
        print(f"\n{self.first_name} {self.last_name}")
        print(f"  Username: {self.username}")
        print(f"  Email: {self.email}")
        print(f"  Location: {self.location}")

    def greet_user(self):
        print(f"\nWelcome back, {self.username}!")

    def increment_login_attempts(self):
        self.login_attempts += 1

    def reset_login_attempts(self):
        self.login_attempts = 0

maria = User('maria', 'torres', 'm_torres', 'maria@example.com')
maria.describe_user()
maria.greet_user()

print("\nMaking 3 login attempts...")
maria.increment_login_attempts()
maria.increment_login_attempts()
maria.increment_login_attempts()
print(f"  Login attempts: {maria.login_attempts}")

print("Resetting login attempts...")
maria.reset_login_attempts()
print(f"  Login attempts: {maria.login_attempts}")