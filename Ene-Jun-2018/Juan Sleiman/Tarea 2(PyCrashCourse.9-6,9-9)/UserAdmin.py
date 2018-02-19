"""9-3. Users: Make a class called User. Create two attributes called first_name
and last_name, and then create several other attributes that are typically stored
in a user profile. Make a method called describe_user() that prints a summary
of the user’s information. Make another method called greet_user() that prints
a personalized greeting to the user."""
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

"""sleiman = User('juan', 'sleiman', 21, 14151301)
sleiman.describe_user()
sleiman.greet_user()"""

"""9-7. Write a class called Admin that inherits from the User class. Add an attribute, privileges, that stores a list
of strings like "can add post", "can delete post", "can ban user", and so on.
Write a method called show_privileges() that lists the administrator’s set of
privileges. Create an instance of Admin, and call your method."""

class Admin(User):

    def __init__(self,first_name, last_name, age, ID):
        super().__init__(first_name, last_name, age, ID)
        # empty set of privileges.
        self.privileges = Privileges()

    """def show_privileges(self):
        print("\nPrivileges:")
        for p in self.privileges:
            print("* " + p)"""

"""sleiman = Admin('juan', 'sleiman', 21, 1451301)
sleiman.describe_user()
sleiman.privileges = ['can add users', 'can ban  users', 'can do the Harlem Shake']
sleiman.show_privileges()"""

"""9-8. Privileges: Write a separate Privileges class. The class should have one
attribute, privileges, that stores a list of strings as described in Exercise 9-7.
Move the show_privileges() method to this class. Make a Privileges instance
as an attribute in the Admin class. Create a new instance of Admin and use your
method to show its privileges."""

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

sleiman = Admin('juan', 'sleiman', 21, 1451301)
sleiman.describe_user()

sleiman.privileges.show_privileges()

print("\nNow we are adding some privileges: ")
sleiman_privileges = ['can add users', 'can ban  users', 'can do the Harlem Shake']
sleiman.privileges.privileges = sleiman_privileges
sleiman.privileges.show_privileges()
