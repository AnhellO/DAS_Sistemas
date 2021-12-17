class User():
    """Represent a simple user profile."""

    def __init__(self, first_name, last_name, username, email):
        self.first_name = first_name.title()
        self.last_name = last_name.title()
        self.username = username
        self.email = email
        self.login_attempts = 0

    def describe_user(self):
        print(f"\n{self.first_name} {self.last_name}")
        print(f"  Username: {self.username}")
        print(f"  Email: {self.email}")


    def greet_user(self):
        print(f"\nBienvenid@, {self.username}!")

    def increment_login_attempts(self):
        self.login_attempts += 1

    def reset_login_attempts(self):
        self.login_attempts = 0

class Admin(User):
    def __init__(self, first_name, last_name, username, email):
        super().__init__(first_name, last_name, username, email)
        self.privileges = []

    def show_privileges(self):
        """Mostrar los privilegios."""
        print("\nPrivileges:")
        for privilege in self.privileges:
            print(f"- {privilege}")


maria = Admin('maria', 'torres', 'm_torres', 'maria@example.com')
maria.describe_user()

maria.privileges = [
    'can reset passwords',
    'can moderate discussions',
    'can suspend accounts',
    ]

maria.show_privileges()        