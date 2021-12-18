class User():
    def __init__(self,first_name,last_name,username,email,number,age):
        self.first_name = first_name
        self.last_name = last_name
        self.username = username
        self.email = email
        self.number = number
        self.age = age
        self.login_attemps = 0
    
    def describe_user(self):
        print("  NAME:  ", self.first_name)
        print("  LAST NAME:  ", self.last_name)
        print("  USERNAME:  ", self.username)
        print("  EMAIL:  ", self.email)
        print("  NUMBER:  ", self.number)
        print("  AGE:  ", self.age)
    
    def greet_user(self):
        print("Welcome ", self.username)
    
    def increment_login_attemps(self):
        self.login_attemps += 1
    
    def reset_login_attemps(self):
        self.login_attemps = 0


class Admin(User):
    def __init__(self, first_name, last_name, username, email, number, age):
        super().__init__(first_name, last_name, username, email, number, age)
        
        self.privileges = Privileges()
        

class Privileges():
    def __init__(self, privileges = []):
        self.priveleges = privileges
        
    def show_privileges(self):
        print("\nPrivilegios")
        for privilege in self.priveleges:
            print("- ", privilege)
        print("\n")
        
            
user1 = Admin("Anahi", "De la Cruz", "Elvanana", "elva960@hotmail.com", "8441234567", "16")
user1.describe_user()


user1_privilges = [
    'Puede agregar publicaciones',
    'Puede borrar publicaciones',
    'Puede eliminar a un usuario'
]

user1.privileges.priveleges = user1_privilges
user1.privileges.show_privileges()

user2 = Admin("Josh", "Peck", "JoshPeck", "JoshPeck@hotmail.com", "8424569312", "34")
user2.describe_user()

user2_privilges = [
    'Puede agregar publicaciones'
]

user2.privileges.priveleges = user2_privilges
user2.privileges.show_privileges()