class User:

    def __init__(self, first_name, last_name, country, email):
        self.first_name = first_name
        self.last_name = last_name
        self.country = country
        self.email = email

    def describe_user(self):
        print(f"User name: {self.first_name} {self.last_name}\n"
              + f"Contry: {self.country}\n"
              + f"E-mail: {self.email}")

    def greet_user(self):
        print(f"Welcome, {self.first_name} {self.last_name}!\n")


class Admin(User):
    def __init__(self, first_name, last_name, country, email):
        super().__init__(first_name, last_name, country, email)
        self.admin_privileges = Privileges()


class Privileges:
    def __init__(self):
        self.privileges = []

    def show_privileges(self):
        print("Admin privileges:")
        for privilege in self.privileges:
            print(f"- {privilege}")
