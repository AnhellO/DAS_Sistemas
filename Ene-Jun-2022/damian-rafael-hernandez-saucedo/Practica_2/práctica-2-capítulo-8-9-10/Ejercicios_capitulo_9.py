#9.1
class Restaurante():

    def __init__(self, nombreRes, tipoCoci):
        self.nombreRes = nombreRes
        self.tipiCoci = tipoCoci


    def describe_restaurante(self):
        print("El nombre del res es" + self.nombreRes + "tipo es " + self.tipiCoci)

    def abierto():
        print("El restaurante es abierto")



#9.2
res = Restaurante("pol la france", "Comida francesa")# objeto 1
print(res.nombreRes)
res.describe_restaurante()
res.abierto

res1= Restaurante("el buen pastor", "Comida mexicana")# objeto 2
res.describe_restaurante()
res.abierto

res2= Restaurante("la fragata", "Comida de mariscos")#objeto 3
res.describe_restaurante()
res.abierto



#9.3

class Usuario():

    def __init__(self, nombre, segundoNom, edad):
        self.nombre = nombre
        self.segundoNom = segundoNom
        self.edad = edad

    def desc_usuario(self):
        print(self.nombre, self.segundoNom, self.edad)

    def saludo(self):
        print("Hola cuidate del covid es peligroso " + self.nombre)

usu = Usuario("damian", "rafael", 24)
usu.saludo()
usu.desc_usuario()

#9.10

class Restaurante:

    def __init__(self, nombre, cuisine_type):

        self.nombre = nombre.title()
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurante(self):

        mensaje = self.nombre + " sirve deliciosas " + self.cuisine_type + "."
        print("\n" + mensaje)

    def abierto_restaurante(self):

        mensaje = self.nombre + " Disponible yaaaaaa!"
        print("\n" + mensaje)

    def set_number_served(self, number_served):
        self. number_served= number_served

    def increment_number_served(self,number_served ):
        self.number_served += number_served

#9.11
from Restaurante import Restaurante

Monaco = Restaurante('veracruz', 'Mariscos')
Monaco.describe_restaurante()
Monaco.abierto_restaurante()

#9.13
from collections import OrderedDict

dicci = OrderedDict()

dicci['string'] = 'Cadena de caracteres.'
dicci['list'] = 'Estructura de datos.'
dicci['import'] = 'Enlaza los resultados de busqueda.'
dicci['from'] = 'Importa modulos.'
dicci['false'] = 'Son elmentos nulos o vacios.'
dicci['if'] = 'Se utiliza para ejecutar un bloque de codigo.'

for word, definicion in dicci.items():    
    print("\n" + word + " " + definicion)

#9.14
from random import randint


class Dado():
    def __init__(self, sides=6):
        self.sides = sides

    def girar_dado(self):
        return randint(1, self.sides)

dado = Dado()

resultados = []
for girar_num in range(10):
    resultado = dado.girar_dado()
    resultados.append(resultado)
print("dado de 6 caras - 10 tiros")
print(resultados)

dado = Dado(sides=10)

resultados = []
for girar_num in range(10):
    resultado = dado.girar_dado()
    resultados.append(resultado)
print("\ndado de 10 caras - 10 tiros")
print(resultados)

dado = Dado(sides=20)

resultados = []
for girar_num in range(10):
    resultado = dado.girar_dado()
    resultados.append(resultado)
print("\ndado de 20 caras - 10 tiros")
print(resultados) 

#9.4
import Restaurante

Restaurante = Restaurante('macdonals', 'hamburguesa')
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

        #9.6
class Restaurante():

    def __init__(self, nombreRes, tipoCoci):
        self.nombreRes = nombreRes
        self.tipiCoci = tipoCoci


    def describe_restaurante(self):
        print("El nombre del res es" + self.nombreRes + "y su tipo es " + self.tipiCoci)

    def abierto():
        print("El restaurante esta abierto")

    def set_number_served(self, number_served):
        self. number_served= number_served

    def increment_number_served(self,number_served ):
        self.number_served += number_served

class IceCreamStand(Restaurante):

    def __init__(self, nombre, cuisine_type='Helado'):
        super().__init__(nombre, cuisine_type)
        self.flavors = []

    def show_flavors(self):
        print("\nLos helados dispobibles son :")
        for flavor in self.flavors:
            print("- " + flavor.title())


heladochico = IceCreamStand('Helado chico')
heladochico.flavors = [ 'nuez', 'pstache']

heladochico.describe_restaurante()
heladochico.show_flavors()        

restaurante = Restaurante('macdonals', 'hamburguesas')
print(restaurante.nombre)
print(restaurante.cuisine_type)

restaurante.describe_restaurante()
restaurante.abierto_restaurante()
#9.7 

class Admin(Usuario):
    def __init__(self, nombre, segundoNom,edad,usuarionomb, correo, localidad):
        super().__init__(nombre, segundoNom, edad, usuarionomb, correo, localidad)
        self.privileges = Privileges()
#9.8
class Privileges():
    def __init__(self, privileges=[]):
        self.privileges = privileges

    def show_privileges(self):
        print("\nPrivileges:")
        for privilege in self.privileges:
            print("- " + privilege)    

#9.9
class Car():

    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name.title()

    def read_odometer(self):
        print("This car has " + str(self.odometer_reading) + " miles on it.")

    def update_odometer(self, mileage):
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")

    def increment_odometer(self, miles):
        self.odometer_reading += miles


class Battery():

    def __init__(self, battery_size=70):
        self.battery_size = battery_size

    def describe_battery(self):
        print("This car has a " + str(self.battery_size) + "-kWh battery.")

    def get_range(self):
        if self.battery_size == 70:
            range = 240
        elif self.battery_size == 85:
            range = 270

        message = "This car can go approximately " + str(range)
        message += " miles on a full charge."
        print(message)

    def upgrade_battery(self):
        if self.battery_size == 70:
            self.battery_size = 85
            print("Upgrading the battery size")


class ElectricCar(Car):

    def __init__(self, make, model, year):
        super().__init__(make, model, year)
        self.battery = Battery()

my_tesla = ElectricCar('tesla', 'model', 2022)
print(my_tesla.get_descriptive_name())
my_tesla.battery.describe_battery()
my_tesla.battery.get_range()

print("\nBaterry Upgraded")
my_tesla.battery.upgrade_battery()
my_tesla.battery.get_range()