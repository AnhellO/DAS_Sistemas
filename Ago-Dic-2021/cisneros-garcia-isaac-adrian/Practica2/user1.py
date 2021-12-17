class User():
    
    def __init__(self, first_name, last_name, username, email, location):
        self.first_name = first_name.title()
        self.last_name = last_name.title()
        self.username = username
        self.email = email
        self.location = location.title()
        self.login_attempts = 0

    def describe_user(self):
          
        print(f"\n{self.first_name} {self.last_name}")
        print(f"  Nombre de usuario: {self.username}")
        print(f"  Correo electronico: {self.email}")
        print(f"  Ubicación: {self.location}")

    def greet_user(self):
        print(f"\n¡Bienvenido {self.username}!")

    def increment_login_attempts(self):
        self.login_attempts += 1

    def reset_login_attempts(self):
        self.login_attempts = 0
