class User:
    """9-8. Privileges: Write a separate Privileges class. The class should have one 
    attribute, privileges, that stores a list of strings as described in Exercise 9-7.
    Move the show_privileges() method to this class. Make a Privileges instance 
    as an attribute in the Admin class."""

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


 # Create a new instance of Admin and use your method to show its privileges.
admin_privileges = ["can add post", "can delete post", "can ban user",
                    "can add record", "can remove record", "can acess to server"]
user_admin = Admin("Alan", "Menchaca", "México",
                   "alanmenchaca@gmail.com")

user_admin.admin_privileges.privileges = admin_privileges
user_admin.admin_privileges.show_privileges()
# Admin privileges:
# - can add post
# - can delete post
# - can ban user
# - can add record
# - can remove record
# - can acess to server
