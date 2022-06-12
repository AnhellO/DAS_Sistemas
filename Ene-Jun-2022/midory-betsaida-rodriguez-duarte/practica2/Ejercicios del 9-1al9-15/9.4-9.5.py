#9.4
import Restaurante

Restaurante = Restaurante('carls jr', 'hamburguesa')
Restaurante.describe_restaurante()

print("\nEl numero servido: " + str(Restaurante.number_served))
Restaurante.number_served = 120
print("El numero serdivo: " + str(Restaurante.number_served))

Restaurante.set_number_served(1000)
print("El numero serdivo: " + str(Restaurante.number_served))

Restaurante.increment_number_served(540)
print("El numero serdivo: " + str(Restaurante.number_served))

#9.5
class Usuario():

    def __init__(self, nombre, segundoNom,edad, usuarionomb, correo, localidad):
        
        self.nombre = nombre.title()
        self.segundoNom = segundoNom.title()
        self.edad = edad
        self.usuarionomb = usuarionomb.title()
        self.correo = correo
        self.localidad = localidad.title()
        self.login_attempts = 0

    def desc_usuario(self):
        print("\n" + self.nombre + " " + self.segundoNom)
        print("  usuarionomb: " + self.usuarionomb)
        print("  correo: " + self.correo)
        print("  Localidad: " + self.localidad)

    def greet_usuario(self):
        print("\n bienvenidos, " + self.usuarionomb + "!")

    def increment_login_attempts(self):
        self.login_attempts += 1

    def reset_login_attempts(self):
        self.login_attempts = 0    