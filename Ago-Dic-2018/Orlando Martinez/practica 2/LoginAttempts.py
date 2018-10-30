class User():

    def __init__(self, first_name, last_name, edad, correo, ciudad):
        self.first_name = first_name
        self.last_name = last_name
        self.edad = edad
        self.correo = correo
        self.ciudad = ciudad
        self.login_attempts = 0

    def describe_user(self):
        print("\n" + self.first_name + " " + self.last_name)
        print("Edad: " + self.edad)
        print("Correo: " + self.correo)
        print("Ciudad: " + self.ciudad)

    def greet_user(self):
        print("\nHola, " + self.first_name + " "  + self.last_name)

    def increment_login_attempts(self):
        self.login_attempts += 1

    def reset_login_attempts(self):
        self.login_attempts = 0

Usuario1 = User('Juan', 'Lopez Rodriguez', '19 años', 'juan_rdz@hotmail.com', 'Saltillo')
Usuario1.describe_user()
Usuario1.greet_user()

print(" 2 Intentos de acceso")
Usuario1.increment_login_attempts()
Usuario1.increment_login_attempts()

print("Intentos de acceso " +str(Usuario1.login_attempts))

print("Resetear intentos de acceso")
Usuario1.reset_login_attempts()
print("Intentos de acceso " +str(Usuario1.login_attempts))
