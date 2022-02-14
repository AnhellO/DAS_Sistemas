class User:
    """9-7. Admin: An administrator is a special kind of user. Write a class called 
    Admin that inherits from the User class you wrote in Exercise 9-3 (page 166) 
    or Exercise 9-5 (page 171).
    """

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
    # Add an attribute, privileges, that stores a list of strings like "can add post",
    # "can delete post", "can ban user", and so on.
    def __init__(self, first_name, last_name, country, email, admin_privileges):
        super().__init__(first_name, last_name, country, email)
        self.privileges = admin_privileges

    # Write a method called show_privileges() that lists the administrator's set of
    # privileges. Create an instance of Admin, and call your method.
    def show_privileges(self):
        print("Admin privileges:")
        for privilege in self.privileges:
            print(f"- {privilege}")


admin_privileges = ["can add post", "can delete post", "can ban user",
                    "can add record", "can remove record", "can acess to server"]
user_admin = Admin("Alan", "Menchaca", "México",
                   "alanmenchaca@gmail.com", admin_privileges)
user_admin.show_privileges()
# Admin privileges:
# - can add post
# - can delete post
# - can ban user
# - can add record
# - can remove record
# - can acess to server
