#Practicas: Python Crash Course, Capitulo 9 Isaac Cisneros#

#Practica 9.1#
print("\n ------------Practica 9.1 output----------------- \n")

class Restaurant():

    def __init__(self, name, cuisine_type):
        self.name = name.title() #Nombre del Restaurante
        self.cuisine_type = cuisine_type #Lo que se cocina

    def describe_restaurant(self):
        msg = f"{self.name} tiene los mejores {self.cuisine_type}."
        print(f"\n{msg}")

    def open_restaurant(self): #Letreto de abierto
        msg = f"{self.name} está abierto. ¡Adelante!"
        print(f"\n{msg}")

restaurant = Restaurant('El Taco De ojo', 'Tacos')
print(restaurant.name)
print(restaurant.cuisine_type)

restaurant.describe_restaurant()
restaurant.open_restaurant()

#Practica 9.2#
print("\n ------------Practica 9.2 output----------------- \n")

class Restaurant():

    def __init__(self, name, cuisine_type):
        self.name = name.title() #Nombre del Restaurante
        self.cuisine_type = cuisine_type #Lo que se cocina

    def describe_restaurant(self):
        msg = f"{self.name} tiene los mejores {self.cuisine_type}."
        print(f"\n{msg}")

    def open_restaurant(self): #Letreto de abierto
        msg = f"{self.name} está abierto. ¡Adelante!"
        print(f"\n{msg}")

taco_ojo = Restaurant('Taco de ojo', 'Tacos')
taco_ojo.describe_restaurant()

Lonche_DonPancho = Restaurant("Lonches Don Pancho", 'Lonches')
Lonche_DonPancho.describe_restaurant()

Elotes_sc = Restaurant('Elotes sin celos', 'Elotes')
Elotes_sc.describe_restaurant()

#Practica 9.3#
print("\n ------------Practica 9.3 output----------------- \n")

class User():

    def __init__(self, first_name, last_name, username, email, location):
        self.first_name = first_name.title()
        self.last_name = last_name.title()
        self.username = username
        self.email = email
        self.location = location.title()

    def describe_user(self):
      
        print(f"\n{self.first_name} {self.last_name}")
        print(f"  Nombre de usuario: {self.username}")
        print(f"  Correo electronico: {self.email}")
        print(f"  Ubicación: {self.location}")

    def greet_user(self):
        print(f"\n ¡Bienvenido {self.username}!")

juanito = User('Juanito','Crack' ,'Juanito_56_lokote', 'juanito_de_maria@gmail.com', 'Paris')
juanito.describe_user()
juanito.greet_user()

pepo = User('Pepo', 'Baila', 'PepoELBailador69', 'pb69@gmail.com', 'Nuevo Mexico')
pepo.describe_user()
pepo.greet_user()

auron = User('Aurelio', 'Abduzkan', 'AuronPlay', 'auron@gmail.com', 'España')
auron.describe_user()
auron.greet_user()

#Practica 9.4#
print("\n ------------Practica 9.4 output----------------- \n")

class Restaurant():

    def __init__(self, name, cuisine_type):
        self.name = name.title()
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        msg = f"{self.name} tiene los mejores {self.cuisine_type}."
        print(f"\n{msg}")

    def open_restaurant(self):
        msg = f"{self.name} Abierto. ¡Adelante!"
        print(f"\n{msg}")

    def set_number_served(self, number_served):
        self.number_served = number_served #Aquí establecemos la cantidad de clientes atendidos

    def increment_number_served(self, additional_served):
        self.number_served += additional_served #Aquí incrementamos la cantidad de clientes atendidos


restaurant = Restaurant('Tacos de ojo', 'Tacos')
restaurant.describe_restaurant()

print(f"\nNumber served: {restaurant.number_served}")
restaurant.number_served = 80
print(f"Number served: {restaurant.number_served}")

restaurant.set_number_served(100)
print(f"Number served: {restaurant.number_served}")

restaurant.increment_number_served(300)
print(f"Number served: {restaurant.number_served}")

#Practica 9.5#
print("\n ------------Practica 9.5 output----------------- \n")

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

juanito = User('Juanito','Crack' ,'Juanito_56_lokote', 'juanito_de_maria@gmail.com', 'Paris')
juanito.describe_user()
juanito.greet_user()


print("\n Realizar 4 intentos de inicio de sesión...")
juanito.increment_login_attempts()
juanito.increment_login_attempts()
juanito.increment_login_attempts()
juanito.increment_login_attempts()
print(f"  intentos de inicio de sesión: {juanito.login_attempts}")

print("Reseteando los intentos de inicio de sesión...")
juanito.reset_login_attempts()
print(f"  Intentos de inicio de sesión: {juanito.login_attempts}")

#Practica 9.6#
print("\n ------------Practica 9.6 output----------------- \n")

class Restaurant():

    def __init__(self, name, cuisine_type):
        self.name = name.title()
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        msg = f"{self.name} tiene los mejores {self.cuisine_type}."
        print(f"\n{msg}")

    def open_restaurant(self):
        msg = f"{self.name} Abierto. ¡Adelante!"
        print(f"\n{msg}")

    def set_number_served(self, number_served):
        self.number_served = number_served #Aquí establecemos la cantidad de clientes atendidos

    def increment_number_served(self, additional_served):
        self.number_served += additional_served #Aquí incrementamos la cantidad de clientes atendidos


class IceCreamStand(Restaurant):

    def __init__(self, name, cuisine_type='helados'):
        super().__init__(name, cuisine_type)
        self.flavors = []

    def show_flavors(self):
        print("\nTenemos los siguientes sabores disponibles:")
        for flavor in self.flavors:
            print(f"- {flavor.title()}")


c_dc = IceCreamStand('Conos "Doña Concha"')
c_dc.flavors = ['vanilla', 'chocolate', 'galleta','banana','pay de limón']

c_dc.describe_restaurant()
c_dc.show_flavors()

#Practica 9.7#
print("\n ------------Practica 9.7 output----------------- \n")

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

class Admin(User):

    def __init__(self, first_name, last_name, username, email, location):
        super().__init__(first_name, last_name, username, email, location)
        self.privileges = []

    def show_privileges(self):
        print("\n ---Privilegios:--- \n")
        for privilege in self.privileges:
            print(f"- {privilege}")

juanito = Admin('Juanito','Crack' ,'Juanito_56_lokote', 'juanito_de_maria@gmail.com', 'Paris')
juanito.describe_user()

juanito.privileges = ['puede borrar usuarios \n', 'puede comprar comida\n', 'puede casarse\n', 'puede ser lo que quiera ser\n']
juanito.show_privileges()

#Practica 9.8#
print("\n ------------Practica 9.8 output----------------- \n")

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

class Admin(User):

    def __init__(self, first_name, last_name, username, email, location):
        super().__init__(first_name, last_name, username, email, location)
        self.privileges = Privileges()

class Privileges():

    def __init__(self, privileges=[]):
        self.privileges = privileges

    def show_privileges(self):
        print("\n ---Privilegios:--- \n")
        if self.privileges:
            for privilege in self.privileges:
             print(f"- {privilege}")
        else:
         print("- El usurio no tiene privilegios.")

juanito = Admin('Juanito','Crack' ,'Juanito_56_lokote', 'juanito_de_maria@gmail.com', 'Paris')
juanito.describe_user()
juanito.privileges.show_privileges()

print("\n Añadiendo privilegios... \n")
juanito_privileges = ['puede borrar usuarios \n', 'puede comprar comida\n', 'puede casarse\n', 'puede ser lo que quiera ser\n']
juanito.privileges.privileges = juanito_privileges
juanito.privileges.show_privileges()

#Practica 9.9#
print("\n ------------Practica 9.9 output----------------- \n")

class Car():

    def __init__(self, manufacturer, model, year):
        self.manufacturer = manufacturer
        self.model = model
        self.year = year
        self.odometer_reading = 0
        
    def get_descriptive_name(self):
        long_name = f"{self.year} {self.manufacturer} {self.model}"
        return long_name.title()
    
    def read_odometer(self):
        print(f"Este carro tiene {self.odometer_reading} millas en él.")
        
    def update_odometer(self, mileage):

        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("¡No se puede revertir un odómetro!:(")
    
    def increment_odometer(self, miles):
        self.odometer_reading += miles

class Battery():

    def __init__(self, battery_size=75):
        self.battery_size = battery_size

    def describe_battery(self):

        print(f"Este carro tiene {self.battery_size}-kWh de batería.")

    def get_range(self):
        if self.battery_size == 75:
            range = 260
        elif self.battery_size == 100:
            range = 315
            
        message = f"Este coche puede ir aproximadamente a {range}"
        message += " millas con carga completa."
        print(message)

    def upgrade_battery(self):
        if self.battery_size == 75:
            self.battery_size = 100
            print("Agrandar la batería a 100 kWh.")
        else:
            print("la batería se puede agrandar.")
    
        
class ElectricCar(Car):

    def __init__(self, manufacturer, model, year):
        super().__init__(manufacturer, model, year)
        self.battery = Battery()

print("Hacer un coche eléctrico, y comprobar la autonomía:")
my_tesla = ElectricCar('Jaguar', 'roadster', 2019)
my_tesla.battery.get_range()

print("\nActualice la batería y vuelva a comprobar la autonomía:")
my_tesla.battery.upgrade_battery()
my_tesla.battery.get_range()

#Practica 9.10#
print("\n ------------Practica 9.10 output----------------- \n")
print("Se encuentra en un archivo separado, en ésta misma carpeta, ya que así tiene que se realizado")
print('Nombres de los archivos: "my_restaurant.py" y "restaurant.py')

#Practica 9.11#
print("\n ------------Practica 9.11 output----------------- \n")
print("Se encuentra en un archivo separado, en ésta misma carpeta, ya que así tiene que se realizado")
print('Nombres de los archivos: "my_user.py" y "user.py')

#Practica 9.12#
print("\n ------------Practica 9.12 output----------------- \n")
print("Se encuentra en un archivo separado, en ésta misma carpeta, ya que así tiene que se realizado")
print('Nombres de los archivos: "my_user1.py", "admin1.py" y "user1.py')

#Practica 9.13#
print("\n ------------Practica 9.13 output----------------- \n")

from random import randint

class Die():

    def __init__(self, sides=6):
        self.sides = sides

    def roll_die(self):
        return randint(1, self.sides)

d6 = Die()

results = []
for roll_num in range(10):
    result = d6.roll_die()
    results.append(result)
print("10 Tiros, 6 caras:")
print(results)

d10 = Die(sides=10)

results = []
for roll_num in range(10):
    result = d10.roll_die()
    results.append(result)
print("\n10 tiros, 10 caras:")
print(results)

d20 = Die(sides=20)

results = []
for roll_num in range(10):
    result = d20.roll_die()
    results.append(result)
print("\n10 tiros, 20 caras:")
print(results)

#Practica 9.14#
print("\n ------------Practica 9.14 output----------------- \n")

from random import choice

x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 'a', 'b', 'c', 'd', 'e']

b_g = []
print("Veamos cuál es el boleto ganador...")

while len(b_g) < 4:
    n_s = choice(x)

    if n_s not in b_g:
        print(f"  la letra o número es: {n_s}!")
        b_g.append(n_s)
print("El boleto ganador es:", b_g, "¡Felicidades!")
print("No olvides seguir participando en ésta gran lotería, pa' que puedas salir de pobre jajaja saludos")

#Practica 9.15#
print("\n ------------Practica 9.15 output----------------- \n")

from random import choice

def get_winning_ticket(x):
    winning_ticket = []
    while len(winning_ticket) < 4:
        pulled_item = choice(possibilities)

        if pulled_item not in winning_ticket:
            winning_ticket.append(pulled_item)

    return winning_ticket

def check_ticket(played_ticket, winning_ticket):
    for element in played_ticket:
        if element not in winning_ticket:
            return False

    return True

def make_random_ticket(possibilities):
    ticket = []
    while len(ticket) < 4:
        pulled_item = choice(possibilities)

        if pulled_item not in ticket:
            ticket.append(pulled_item)

    return ticket


possibilities = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 'a', 'b', 'c', 'd', 'e']
winning_ticket = get_winning_ticket(possibilities)

plays = 0
won = False

max_tries = 1_000_000

while not won:
    new_ticket = make_random_ticket(possibilities)
    won = check_ticket(new_ticket, winning_ticket)
    plays += 1
    if plays >= max_tries:
        break

if won:
    print("We have a winning ticket!")
    print(f"Your ticket: {new_ticket}")
    print(f"Winning ticket: {winning_ticket}")
    print(f"It only took {plays} tries to win!")
else:
    print(f"Tried {plays} times, without pulling a winner. :(")
    print(f"Your ticket: {new_ticket}")
    print(f"Winning ticket: {winning_ticket}")


print("\n Listo Profe, ya no puedo ni con mi alma \n")