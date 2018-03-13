class User():

    def __init__(self, first_name, last_name, age, ID):
        self.first_name = first_name.title()
        self.last_name = last_name.title()
        self.age = str(age)
        self.ID = str(ID)

    def describe_user(self):
        print("\n" + self.first_name + " " + self.last_name)
        print("Age: " + self.age)
        print("ID: " + self.ID)

    def greet_user(self):
        print("\n¡Welcome " + self.first_name + " " + self.last_name + "!" )



class Admin(User):

    def __init__(self,first_name, last_name, age, ID):
        super().__init__(first_name, last_name, age, ID)
        self.privileges = []
        # empty set of privileges.
        self.privileges = Privileges()

class Privileges():
    def __init__(self, privileges=[]):
        self.privileges = privileges

    def show_privileges(self):
        print("\nPrivileges:")
        if self.privileges:
            for p in self.privileges:
                print("* " + p)
        else:
            print("The user hasn't privileges.")

raulito = Admin('raul', 'alejandro', 29, 19962905)
raulito.describe_user()

raulito.privileges.show_privileges()

print("\nNow we are adding some privileges: ")
raulito_privileges = ['can add users', 'can ban  users', 'can do the Harlem Shake']
raulito.privileges.privileges = raulito_privileges
raulito.privileges.show_privileges()
