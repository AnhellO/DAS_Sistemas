###############
#Ejercicio 9-1#
###############
# "Clase representando a un restaurante"
# class Restaurante():
    
#     def __init__(self, nombre, tipo_cocina):
#         "Inicia restaurante."
#         self.nombre = nombre.title()
#         self.tipo_cocina = tipo_cocina

#     def descripcion_restaurant(self):
#         "Caracteristica del restaurante"
#         msg = self.nombre + " sirve excelentes " + self.tipo_cocina + "."
#         print("\n" + msg)

#     def restaurant_abierto(self):
#         msg = self.nombre + " Estamos abiertos, pasele"
#         print("\n" + msg)

# restaurante = Restaurante('Tacos El corral', 'Tacos')
# print(restaurante.nombre)
# print(restaurante.tipo_cocina)

# restaurante.descripcion_restaurant()
# restaurante.restaurant_abierto()

###############
#Ejercicio 9-2#
###############
# class Restaurante():
#     "Clase representando a un restaurante"

#     def __init__(self, nombre, tipo_cocina):
#         self.nombre = nombre.title()
#         self.tipo_cocina = tipo_cocina

#     def descripcion_restaurant(self):
#         msg = self.nombre + " Sirve Excelente(s) " + self.tipo_cocina + "."
#         print("\n" + msg)

#     def open_restaurant(self):
#         msg = self.nombre + " Esta Abierto. Pase Usted."
#         print("\n" + msg)

# tacos = Restaurante('Tacos El Corral', 'Tacos')
# tacos.descripcion_restaurant()

# cabaña = Restaurante("La Cabaña", 'Hamburguesas')
# cabaña.descripcion_restaurant()

# Kampai = Restaurante('Kampai', 'Sushi')
# Kampai.descripcion_restaurant()

###############
#Ejercicio 9-3#
###############
#  class Usuario():
#      "Representa un perfil"

#      def __init__(self, nombre, apellido, usuario, email):
#          "Inicia el usuario"
#          self.nombre = nombre.title()
#          self.apellido = apellido.title()
#          self.usuario = usuario
#          self.email = email

#      def descripcion_usuario(self):
#          "Muestra la información del usuario."
#          print("\n" + self.nombre + " " + self.apellido)
#          print("  Usuario: " + self.usuario)
#          print("  Email: " + self.email)

#      def saludo_usuario(self):
#          "Muestra saludo personalizado."
#          print("\nHola, " + self.usuario + "\nBienvenido!")

# david = Usuario('David', 'Viera', 'ElDeibid', 'david@uadec.edu')
# david.descripcion_usuario()
# david.saludo_usuario()

# emilio = Usuario('Emilio', 'Silva', 'foundedline', 'foundedline@gmail.com')
# emilio.descripcion_usuario()
# emilio.saludo_usuario()

###############
#Ejercicio 9-4#
###############
# class Restaurante():
    
#     def __init__(self, nombre, tipo_cocina):
#          "Inicia restaurante."
#          self.nombre = nombre.title()
#          self.tipo_cocina = tipo_cocina
#          self.number_served = 0

#     def descripcion_restaurant(self):
#          "Caracteristica del restaurante"
#          msg = self.nombre + " sirve excelentes " + self.tipo_cocina + "."
#          print("\n" + msg)

#     def restaurant_abierto(self):
#          msg = self.nombre + " Estamos abiertos, pasele"
#          print("\n" + msg)

#     def set_number_served(self, number_served):
#         "Permite establecer el número de clientes que se han atendido."
#         self.number_served = number_served

#     def increment_number_served(self, additional_served):
#         "Permite que incremente el número de clientes atendidos."
#         self.number_served += additional_served

# restaurante = Restaurante('Tacos El corral', 'Tacos')
# restaurante.descripcion_restaurant()

# print("\nClientes Servidos: " + str(restaurante.number_served))
# restaurante.number_served = 200
# print("Clientes Servidos: " + str(restaurante.number_served))

# restaurante.set_number_served(400)
# print("Clientes Servidos: " + str(restaurante.number_served))

# restaurante.increment_number_served(500)
# print("Clientes Servidos: " + str(restaurante.number_served))

###############
#Ejercicio 9-5#
###############
# class Usuario():
#      "Representa un perfil"
#      def __init__(self, nombre, apellido, usuario, email):
#          """Inicia el usuario"""
#          self.nombre = nombre.title()
#          self.apellido = apellido.title()
#          self.usuario = usuario
#          self.email = email
#          self.intentos_acceso = 0

#      def descripcion_usuario(self):
#          "Muestra la información del usuario."
#          print("\n" + self.nombre + " " + self.apellido)
#          print("  Usuario: " + self.usuario)
#          print("  Email: " + self.email)

#      def saludo_usuario(self):
#          "Muestra saludo personalizado."
#          print("\nHola, " + self.usuario + "\nBienvenido!")
     
#      def incremento_intentos_acceso(self):
#          "Incrementa intentos +1"
#          self.intentos_acceso += 1 
    
#      def reset_intentos_acceso(self):
#          "Reinicia intentos a 0"
#          self.intentos_acceso = 0

# david = Usuario('David', 'Viera', 'ElDeibid', 'david@uadec.edu')
# david.descripcion_usuario()
# david.saludo_usuario()

# print("\nHaciendo 5 intentos de acceso...")
# david.incremento_intentos_acceso()
# david.incremento_intentos_acceso()
# david.incremento_intentos_acceso()
# david.incremento_intentos_acceso()
# david.incremento_intentos_acceso()
# print(" Intentos de Acceso:" + str(david.intentos_acceso))

# print("\nReset de intentos de acceso...")
# david.reset_intentos_acceso()
# print(" Intentos de Acceso:" + str(david.intentos_acceso))

###############
#Ejercicio 9-6#
###############
# class Restaurante():
    
#      def __init__(self, nombre, tipo_cocina):
#           "Inicia restaurante."
#           self.nombre = nombre.title()
#           self.tipo_cocina = tipo_cocina
#           self.number_served = 0

#      def descripcion_restaurant(self):
#           "Caracteristica del restaurante"
#           msg = self.nombre + " sirve excelentes " + self.tipo_cocina + "."
#           print("\n" + msg)

#      def restaurant_abierto(self):
#           msg = self.nombre + " Estamos abiertos, pasele"
#           print("\n" + msg)

#      def set_number_served(self, number_served):
#          "Permite establecer el número de clientes que se han atendido."
#          self.number_served = number_served

#      def increment_number_served(self, additional_served):
#          "Permite que incremente el número de clientes atendidos."
#          self.number_served += additional_served

# class Puesto_Helados(Restaurante):
#     "Representa un puesto de helados."

#     def __init__(self, nombre, tipo_cocina='Helados'):
#         """Inicia puesto de helados."""
#         super().__init__(nombre, tipo_cocina)
#         self.sabores = []

#     def muestra_sabores(self):
#         "Muestra Sabores Disponibles."
#         print("\nContamos con los siguientes sabores:")
#         for sabores in self.sabores:
#             print("- " + sabores.title())


# regia = Puesto_Helados('Helados Regia')
# regia.sabores = ['Fresa', 'Vainilla', 'Chocolate']

# regia.descripcion_restaurant()
# regia.muestra_sabores()

###############
#Ejercicio 9-7#
###############
# class Usuario():
#     def __init__(self, nombre, apellido, usuario, email):
#           self.nombre = nombre.title()
#           self.apellido = apellido.title()
#           self.usuario = usuario
#           self.email = email
#           self.intentos_acceso = 0
#     def descripcion_usuario(self):
#           print("\n" + self.nombre + " " + self.apellido)
#           print("  Usuario: " + self.usuario)
#           print("  Email: " + self.email)

#     def saludo_usuario(self):
#           print("\nHola, " + self.usuario + "\nBienvenido!")
     
#     def incremento_intentos_acceso(self):
#           self.intentos_acceso += 1 
    
#     def reset_intentos_acceso(self):
#           self.intentos_acceso = 0

# class Admin(Usuario):
#     """Usuario con privilegios administrador."""

#     def __init__(self, nombre, apellido, usuario, email):
#         """Inicia admin."""
#         super().__init__(nombre, apellido, usuario, email)
#         self.privilegios = []

#     def muestra_privilegios(self):
#         """Muestra privilegios que tiene este usuario."""
#         print("\nPrivilegios de usuario:")
#         for privilegio in self.privilegios:
#             print("- " + privilegio)

# david = Admin('David', 'Viera', 'ElDeibid', 'david@uadec.edu')
# david.descripcion_usuario()

# david.privilegios = [
#     'Puede hacer reset de contraseñas',
#     'Puede suspender cuentas',
#     'Puede ver historial de cuentas'
#     ]
# david.muestra_privilegios()
###############
#Ejercicio 9-8#
###############
# class Usuario():
#     def __init__(self, nombre, apellido, usuario, email):
#           self.nombre = nombre.title()
#           self.apellido = apellido.title()
#           self.usuario = usuario
#           self.email = email
#           self.intentos_acceso = 0
#     def descripcion_usuario(self):
#           print("\n" + self.nombre + " " + self.apellido)
#           print("  Usuario: " + self.usuario)
#           print("  Email: " + self.email)

#     def saludo_usuario(self):
#           print("\nHola, " + self.usuario + "\nBienvenido!")
     
#     def incremento_intentos_acceso(self):
#           self.intentos_acceso += 1 
    
#     def reset_intentos_acceso(self):
#           self.intentos_acceso = 0

# class Admin(Usuario):
#     """Usuario con privilegios administrador."""

#     def __init__(self, nombre, apellido, usuario, email):
#         """Inicia admin."""
#         super().__init__(nombre, apellido, usuario, email)

#         "Inicia un set vacio de privilegios"
#         self.privilegios = Privilegios()

# class Privilegios():
#       "clase para almacenar los privilegios de un administrador"
#       def __init__(self, privilegios=[]):
#         self.privilegios = privilegios

#       def muestra_privilegios(self):
#         print("\nPrivilegios de usuario:")
#         if self.privilegios:
#             for privilegio in self.privilegios:
#                 print("- " + privilegio)
#         else:
#             print("- Este usuario no cuenta con privilegios.")
            
# david = Admin('David', 'Viera', 'ElDeibid', 'david@uadec.edu')
# david.descripcion_usuario()

# david.privilegios.muestra_privilegios()

# print("\nAgregando privilegios...")
# david_privilegios = [
#     'Puede hacer reset de contraseñas',
#     'Puede suspender cuentas',
#     'Puede ver historial de cuentas'
#     ]
# david.privilegios.privilegios = david_privilegios
# david.privilegios.muestra_privilegios()
###############
#Ejercicio 9-9#
###############
# class Auto():
#     "Representa un auto."

#     def __init__(self, manufactura, modelo, año):
#         "Inicializar atributos para describir un coche."
#         self.manufactura = manufactura
#         self.modelo = modelo
#         self.año = año
#         self.odometer_reading = 0
        
#     def nombre_descriptivo(self):
#         "Devuelve un nombre descriptivo con formato ordenado."
#         nombre_largo = str(self.año) + ' ' + self.manufactura + ' ' + self.modelo
#         return nombre_largo.title()
    
#     def lee_odometro(self):
#         "Declaracion que muestra el kilometraje del auto."
#         print("Este auto tiene " + str(self.odometer_reading) + " millas.")
        
#     def actualiza_odometro(self, millage):
#         """
#         Establece la lectura del odómetro en el valor dado.
#         Rechaza el cambio si intenta hacer retroceder el odómetro.
#         """
#         if millage >= self.odometer_reading:
#             self.odometer_reading = millage
#         else:
#             print("No puedes retroceder el odometro!")
    
#     def incremento_odometro(self, millas):
#         "Agrega la cantidad dada a la lectura del odómetro."
#         self.odometer_reading += millas

# class Bateria():

#     def __init__(self, tamaño_bateria=60):
#         """Inicia atributos de bateria."""
#         self.tamaño_bateria = tamaño_bateria

#     def descripcion_bateria(self):
#         """Describe la bateria."""
#         print("Este auto tiene  " + str(self.tamaño_bateria) + "-kWh  de bateria.")

        
#     def obtener_rango(self):
#         """Imprime declaración sobre el alcance que proporciona esta batería."""
#         if self.tamaño_bateria == 60:
#             range = 140
#         elif self.tamaño_bateria == 85:
#             range = 185
            
#         mensaje = "Este coche puede ir aproximadamente" + str(range)
#         mensaje += " millas en una carga completa."
#         print(mensaje)

#     def mejora_bateria(self):
#         """Mejora la bateria si es posible."""
#         if self.tamaño_bateria == 60:
#             self.tamaño_bateria = 85
#             print("Mejorada a 85 kWh.")
#         else:
#             print("La bateria ya esta mejorada.")
    
        
# class AutoElectrico(Auto):
#     "Aspectos del auto."

#     def __init__(self, manufactura, modelo, año):
#         """
#         Inicializa atributos de la clase principal.
#         Despues inicializa los atributos específicos de un coche eléctrico.
#         """
#         super().__init__(manufactura, modelo, año)
#         self.bateria = Bateria()


# print("Hacer un auto eléctrico, y comprobar  bateria:")
# audi = AutoElectrico('Auidi', 'e-tron', 2020)
# audi.bateria.descripcion_bateria()

# print("\nMejora la bateria y revisa de nuevo check:")
# audi.bateria.mejora_bateria()
# audi.bateria.descripcion_bateria()

# print("\nIntenta mejorar la bateria nuevamente y revisa.")
# audi.bateria.mejora_bateria()
# audi.bateria.descripcion_bateria()

################
#Ejercicio 9-10#
################

# class Restaurante():
    
#     def __init__(self, nombre, tipo_cocina):
#          "Inicia restaurante."
#          self.nombre = nombre.title()
#          self.tipo_cocina = tipo_cocina
#          self.cantidad_servidos = 0

#     def descripcion_restaurant(self):
#          "Caracteristica del restaurante"
#          msg = self.nombre + " sirve excelentes " + self.tipo_cocina + "."
#          print("\n" + msg)

#     def restaurant_abierto(self):
#          msg = self.nombre + " Estamos abiertos, pasele"
#          print("\n" + msg)

#     def set_number_served(self, cantidad_servidos):
#         "Permite establecer el número de clientes que se han atendido."
#         self.cantidad_servidos = cantidad_servidos

#     def increment_number_served(self, adicional_servidos):
#         "Permite que incremente el número de clientes atendidos."
#         self.cantidad_servidos += adicional_servidos

################
#Ejercicio 9-11#
################

# class Usuario():
#     def __init__(self, nombre, apellido, usuario, email):
#           self.nombre = nombre.title()
#           self.apellido = apellido.title()
#           self.usuario = usuario
#           self.email = email
#           self.intentos_acceso = 0
#     def descripcion_usuario(self):
#           print("\n" + self.nombre + " " + self.apellido)
#           print("  Usuario: " + self.usuario)
#           print("  Email: " + self.email)

#     def saludo_usuario(self):
#           print("\nHola, " + self.usuario + "\nBienvenido!")
     
#     def incremento_intentos_acceso(self):
#           self.intentos_acceso += 1 
    
#     def reset_intentos_acceso(self):
#           self.intentos_acceso = 0

# class Admin(Usuario):
#     """Usuario con privilegios administrador."""

#     def __init__(self, nombre, apellido, usuario, email):
#         """Inicia admin."""
#         super().__init__(nombre, apellido, usuario, email)

#         "Inicia un set vacio de privilegios"
#         self.privilegios = Privilegios()

# class Privilegios():
#       "clase para almacenar los privilegios de un administrador"
#       def __init__(self, privilegios=[]):
#         self.privilegios = privilegios

#       def muestra_privilegios(self):
#         print("\nPrivilegios de usuario:")
#         if self.privilegios:
#             for privilegio in self.privilegios:
#                 print("- " + privilegio)

################
#Ejercicio 9-12#
################

# class Usuario():
#     def __init__(self, nombre, apellido, usuario, email):
#           self.nombre = nombre.title()
#           self.apellido = apellido.title()
#           self.usuario = usuario
#           self.email = email
#           self.intentos_acceso = 0
#     def descripcion_usuario(self):
#           print("\n" + self.nombre + " " + self.apellido)
#           print("  Usuario: " + self.usuario)
#           print("  Email: " + self.email)

#     def saludo_usuario(self):
#           print("\nHola, " + self.usuario + "\nBienvenido!")
     
#     def incremento_intentos_acceso(self):
#           self.intentos_acceso += 1 
    
#     def reset_intentos_acceso(self):
#           self.intentos_acceso = 0

################
#Ejercicio 9-13#
################

# from collections import OrderedDict

# glossary = OrderedDict()

# glossary['string'] = 'A series of characters.'
# glossary['comment'] = 'A note in a program that the Python interpreter ignores.'
# glossary['list'] = 'A collection of items in a particular order.'
# glossary['loop'] = 'Work through a collection of items, one at a time.'
# glossary['dictionary'] = "A collection of key-value pairs."
# glossary['key'] = 'The first item in a key-value pair in a dictionary.'
# glossary['value'] = 'An item associated with a key in a dictionary.'
# glossary['conditional test'] = 'A comparison between two values.'
# glossary['float'] = 'A numerical value with a decimal component.'
# glossary['boolean expression'] = 'An expression that evaluates to True or False.'

# for word, definition in glossary.items():
#     print("\n" + word.title() + ": " + definition)


################
#Ejercicio 9-14#
################
from random import randint

class Dado():
    "Representa un dado."

    def __init__(self, lados=6):
        "Inicia dado."
        self.lados = lados

    def tira_dado(self):
        "Devuelve un número entre 1 y el número de lados."
        return randint(1, self.lados)

# Dado de 6 lados, con 10 tiros.
d6 = Dado()

resultados = []
for num_tiro in range(10):
    resultado = d6.tira_dado()
    resultados.append(resultado)
print("10 tiros de dado 6 lados:")
print(resultados)

# Dado de 0 lados, con 10 tiros.
d10 = Dado(lados=10)

resultados = []
for num_tiro in range(10):
    resultado = d10.tira_dado()
    resultados.append(resultado)
print("\n10 tiros de dado 10 lados:")
print(resultados)

# Dado de 20 lados, con 10 tiros.
d20 = Dado(lados=20)

resultados = []
for num_tiro in range(10):
    resultado = d20.tira_dado()
    resultados.append(resultado)
print("\n10 tiros de dado 20 lados:")
print(resultados)
