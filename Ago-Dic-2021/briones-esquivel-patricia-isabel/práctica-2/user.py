# ------- Ejercicio 9,3- Users -------
class User():

    def __init__(self, first_name, last_name, user_id, user_pass):
        self.first_name = first_name
        self.last_name = last_name
        self.user_id = user_id
        self.user_pass = user_pass
        self.login_attempts = 0  # ------- Ejercicio 9,5- Login Attempts -------
 
    def describe_user(self):
        print("\nUser's name: " + self.first_name.title() + " " + self.last_name.title() + ".")
        print("User ID: " + str(self.user_id))
        print("Password: " + self.user_pass)

    def greet_user(self):
        print("Hey, " + self.first_name + ". How are you?")  

    # ------- Ejercicio 9,5- Login Attempts -------
    def read_login_attempts(self):
        print(self.first_name + " login attempts: " + str(self.login_attempts))

    def increment_login_attempts(self):
        self.login_attempts += 1

    def reset_login_attempts(self):
       self.login_attempts = 0

# ------- Ejercicio 9,3- Users -------
user_1 = User('Mario Hugo','Almaguer', 12, 'abc')
user_1.describe_user()
user_1.greet_user()

user_2 = User('Patricia','Ackerman', 1, 'abc')
user_2.describe_user()
user_2.greet_user()

user_3 = User('Marinette','Dupain-Cheng', 3, 'abc')
user_3.describe_user()
user_3.greet_user()

user_4 = User('Cloe','Bourgeois', 5, 'abc')
user_4.describe_user()
user_4.greet_user()

# ------- Ejercicio 9,5- Login Attempts -------
user_4.increment_login_attempts()
user_4.increment_login_attempts()
user_4.increment_login_attempts()
user_4.increment_login_attempts()
user_4.increment_login_attempts()
user_4.read_login_attempts()
user_4.reset_login_attempts()
user_4.read_login_attempts()

# ------- Ejercicio 9,8- Privileges -------
class Privileges():

    def __init__(self, privileges=[]):
        self.privileges = privileges

    def show_privileges(self):
        print("Privileges: ")
        if self.privileges:
            for p in self.privileges:
             print(f"- {p.title()}")
        else:
         print("User do not have privileges")

# ------- Ejercicio 9,7-Admin -------
# En el ejercicio 9,8 se pide mover el método show_privileges
# por lo que está en comentarios.
class Admin (User):
    def __init__(self, first_name, last_name, user_id, user_pass):
        super().__init__(first_name, last_name, user_id, user_pass)
        self.privileges = Privileges()
        #self.privileges = []
    
    #def show_privileges(self):
        #print("Admin has those privileges: ")
        #for p in self.privileges:
            #print(f"- {p.title()}")

my_admin = Admin('Pedro', 'Naranjo', 45, 'Ladybug56')
#my_admin.privileges = ['can add post', 'can delete post', 'can ban user']
my_admin.describe_user()
#my_admin.show_privileges()

# ------- Ejercicio 9,8- Privileges -------
my_admin.privileges.show_privileges()

user_x = Admin('Carlos', 'Muñoz', 456, 'RenaFurtive')
user_x_privileges = ['can add post', 'can delete post', 'can ban user']
user_x.privileges.privileges = user_x_privileges
user_x.describe_user()
user_x.privileges.show_privileges()