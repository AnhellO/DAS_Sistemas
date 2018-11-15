class User():

    def __init__(self, first_name, last_name, edad, correo, direccion, telefono):
        self.first_name = first_name
        self.last_name = last_name
        self.edad = edad
        self.correo = correo
        self.direccion = direccion
        self.telefono = telefono
        self.login_attempts = 0

    def describe_user(self):
        print("\n" + self.first_name + " " + self.last_name)
        print("Edad: " + self.edad)
        print("Correo: " + self.correo)
        print("Direccion: " + self.direccion)
        print("Telefono: " + self.telefono)

    def greet_user(self):
        print("\nQue onda! ¿Cómo estás?, " + self.first_name + " "  + self.last_name)

    def increment_login_attempts(self):
        self.login_attempts += 1

    def reset_login_attempts(self):
        self.login_attempts = 0

Usuario1 = User('Alma Daniela', 'Ontiveros Perales', '21 años', 'dany-adop@hotmail.com', 'Jesús R. González #777 Colonia. La Libertad', '8443572026')
Usuario1.describe_user()
Usuario1.greet_user()

print("Existen 3 Intentos de acceso")
Usuario1.increment_login_attempts()
Usuario1.increment_login_attempts()
Usuario1.increment_login_attempts()

print("Intentos de acceso " + str(Usuario1.login_attempts))

print("Favor de resetear los intentos de acceso")
Usuario1.reset_login_attempts()
print("Intentos de acceso " +str(Usuario1.login_attempts))