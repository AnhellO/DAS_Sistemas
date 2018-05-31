class User():

    def __init__(self, first_name, last_name, username, email, location):

        self.first_name = first_name.title()
        self.last_name = last_name.title()
        self.username = username
        self.email = email
        self.location = location.title()

    def describe_user(self):

        print("\n" + self.first_name + " " + self.last_name)
        print("  Username: " + self.username)
        print("  Email: " + self.email)
        print("  Location: " + self.location)

    def greet_user(self):

        print("\nBienvenido " + self.username + "!!!")

###########################################################################################
###########################################################################################


class Admin(User):


    def __init__(self, first_name, last_name, username, email, location):

        super().__init__(first_name, last_name, username, email, location)
        self.privileges = Privileges()

###########################################################################################
###########################################################################################

class Privileges():

    def __init__(self, privileges=[]):

        self.privileges = privileges

    def show_privileges(self):

        print("\nPrivileges:")
        for privilege in self.privileges:
            print("- " + privilege)



carlos = Admin('carlos', 'Sleiman', 'SleightTheBeast', 'jcsm_14@gmail.com', 'monterrey')
carlos.describe_user()

carlos.privileges.show_privileges()

print("\nAñadiendo privilegios..")
carlos_privileges = [
    'can add user',
    'can delete password',
    'can ban user'
    ]
carlos.privileges.privileges = carlos_privileges
carlos.privileges.show_privileges()

