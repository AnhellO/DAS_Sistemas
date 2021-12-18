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
        self.privileges = []
    
    def show_privileges(self):
        print("\nPrivilegios del usuario", self.username)
        for privilege in self.privileges:
            print("       ", privilege)
            
user1 = Admin("Anahi", "De la Cruz", "Elvanana", "elva960@hotmail.com", "8441234567", "16")
user1.describe_user()

user1.privileges = [
    '- Puede agregar publicaciones',
    '- Puede borrar publicaciones',
    '- Puede eliminar a un usuario'
]

user1.show_privileges()
print(" ")

user2 = Admin("Jesus", "De la Cruz", "Jisus", "Jisus3680@hotmail.com", "8447894561", "22")
user2.describe_user()

user2.privileges = [
    'Puede agregar publicaciones'
]

user2.show_privileges()
