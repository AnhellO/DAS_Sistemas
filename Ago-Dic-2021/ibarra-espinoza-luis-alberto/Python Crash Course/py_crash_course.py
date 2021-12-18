### 9.1: Restaurant ###

# Crear clase
class Restaurant():

    ## Inicializar atributos
    def __init__(self, restaurant_name, cuisine_type) -> None:
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        ### 9.4 ###
        self.number_served = 0

    ## Metodo descripcion
    def describe_restaurant(self):
        print('The Restaurant name is: ' + self.restaurant_name + '\n'
        + 'and the cuisine type are: ' + self.cuisine_type
        )

    ## Metodo abrir restaurant
    def open_restaurant(self):
        print('The restaurant ' + self.restaurant_name + " now it's open!")

    ### 9.4 ###
    def set_number_served(self, num_costumers: int):
        # Set the number of costomers served to the given value.
        self.number_served = num_costumers

    def increment_number_served(self, increment_num: int):
        # Add the given amout to the number served value.
        self.number_served += increment_num

# Instancias
restaurant = Restaurant('La cocina de Luisito', 'Mexicana')

print(restaurant.restaurant_name)
print(restaurant.cuisine_type)

restaurant.describe_restaurant()
restaurant.open_restaurant()

### 9.2: Three Restaurants ###

# Instances
marcelo_restaurant = Restaurant('La Cocinita de Marcelino', 'tawianesa')
phily_restaurant = Restaurant('Aca Phily', 'Hamburgesas y burritas')
jochospepe_restaurant = Restaurant('Joshos Pepe', 'Hot-Dogs')

##Calling Methods
marcelo_restaurant.describe_restaurant()
phily_restaurant.describe_restaurant()
jochospepe_restaurant.describe_restaurant()

### 9.3: Users ###

# Crear clase
class User():
    def __init__(self, first_name: str, last_name: str, age: int, nacionality: str) -> None:
        ## Initialize attributes to describe a user.
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.nacionality = nacionality
        self.login_attempts = 0

    def describe_user(self):
        print(
            'First Name: ' + self.first_name + '\nLast Name: ' + self.last_name + 
            '\nAge: ' + str(self.age) + '\nNacionality: ' + self.nacionality
        )

    def greet_user(self):
        print('Welcome again ' + self. first_name + ' ' + self.last_name + '!')

    ### 9.5 ###
    def increment_login_attempts(self):
        self.login_attempts += 1

    def reset_login_attempts(self):
        self.login_attempts = 0

# Instances
luis = User('Luis', 'Ibarra', 18, 'Mexicana')
frida = User('Frida', 'Rodriguez', 5, 'Mexicana')
leo = User('Leo', 'Messi', 33, 'Argentina')

# Calling Methods
luis.describe_user()
luis.greet_user()
frida.describe_user()
frida.greet_user()
leo.describe_user()
leo.greet_user()

### 9.4: Number Served ###

# New Instance
new_restaurant = Restaurant('Boruca', 'Monclovense')
print('The number of customers served is: ' + str(new_restaurant.number_served))
new_restaurant.number_served = 19
print('The number of customers served is: ' + str(new_restaurant.number_served))

# Add methods
'''
def set_number_served(self, num_costumers):
    # Set the number of costomers served to the given value
    self.number_served = num_costumers
'''

new_restaurant.set_number_served(25)
print('The number of customers served is: ' + str(new_restaurant.number_served))

new_restaurant.increment_number_served(4)
print('The number of customers served is: ' + str(new_restaurant.number_served))

### 9.5: Login Attempts ###

# New instance
lupita = User('Lupita', 'Espinoza', 60, 'Mexicana')
lupita.increment_login_attempts()
lupita.increment_login_attempts()
lupita.increment_login_attempts()
lupita.increment_login_attempts()
print('The number of login attempts is: ' + str(lupita.login_attempts))

lupita.reset_login_attempts()
print('The number of login attempts is: ' + str(lupita.login_attempts))

### 9.6: Ice Cream Stand ###

# create child class
class IceCream(Restaurant):
    
    def __init__(self, restaurant_name, cuisine_type) -> None:
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = []

    def show_flavors(self):
        print('The flavors available are: ')
        for i in self.flavors:
            print('- ' + i)

michoacana = IceCream('La Michoacana', 'Ice Cream')
michoacana.flavors = ['Vainilla', 'Chocolate', 'Fresa', 'Limon']
michoacana.describe_restaurant()
michoacana.show_flavors()

### 9.7: Admin ###

# create child class
class Admin(User):

    def __init__(self, first_name: str, last_name: str, age: int, nacionality: str) -> None:
        super().__init__(first_name, last_name, age, nacionality)
        self.privileges = Privileges()

    '''
    def show_privileges(self):
        print('This administator has the following privileges: ')
        for i in self.privileges:
            print('- ' + i)
    '''

#prefecto = Admin('Jose', 'Serrato', '35', 'Alemana', 0)
#prefecto.show_privileges()

### 9.8: Privileges ###

class Privileges():

    def __init__(self, privileges = []) -> None:
        self.privileges = ['Can add post', 'Can delete post', 'Can ban user']

    def show_privileges(self):
        print('This administator has the following privileges: ')
        for i in self.privileges:
            print('- ' + i)

prefecto = Admin('Jose', 'Serrato', 35, 'Alemana')
prefecto.privileges.show_privileges()

### 9.9: Battery Upgrade ###

class Car():

    def __init__(self, make, model, year) -> None:
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name
    
    def read_odometer(self):
        print('This car has ' + str(self.odometer_reading) + ' miles on it.')

    def update_odometer(self, mileage: int):
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")

    def increment_odometer(self, miles: int):
        self.odometer_reading += miles

class Battery():

    def __init__(self, battery_size = 70) -> None:
        self.battery_size = battery_size

    def describe_battery(self):
        print("This car has a " + str(self.battery_size) + "-kWh battery.")

    def get_range(self):
        if self.battery_size == 70:
            range = 240
        elif self.battery_size == 85:
            range = 270
        
        message = 'This car can go approximately ' + str(range)
        message += ' miles on a full charge.'
        print(message)

    def upgrade_battery(self):
        if self.battery_size == 70:
            self.battery_size = 85
            print('Upgraded the battery to 85 kWh.')
        else:
            print('The battery is already upgraded.')

class ElectricCar(Car):

    def __init__(self, make, model, year) -> None:
        super().__init__(make, model, year)
        self.battery = Battery()
        

my_tesla = ElectricCar('Tesla', 'Model S', '2016')
my_tesla.battery.get_range()
my_tesla.battery.upgrade_battery()
my_tesla.battery.get_range()

### 9.10: Imported Restaurant ###

class Restaurant():

    ## Inicializar atributos
    def __init__(self, restaurant_name, cuisine_type) -> None:
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        ### 9.4 ###
        self.number_served = 0

    ## Metodo descripcion
    def describe_restaurant(self):
        print('The Restaurant name is: ' + self.restaurant_name + '\n'
        + 'and the cuisine type are: ' + self.cuisine_type + '\nnumber of customers served today: '
        + str(self.number_served)
        )

    ## Metodo abrir restaurant
    def open_restaurant(self):
        print('The restaurant ' + self.restaurant_name + " now it's open!")

    ### 9.4 ###
    def set_number_served(self, num_costumers: int):
        # Set the number of costomers served to the given value.
        self.number_served = num_costumers

    def increment_number_served(self, increment_num: int):
        # Add the given amout to the number served value.
        self.number_served += increment_num
'''
from restaurant import Restaurant

mi_cocina = Restaurant('La Cocinita', 'Arabe')

mi_cocina.describe_restaurant()
mi_cocina.set_number_served(15)
mi_cocina.increment_number_served(4)
mi_cocina.describe_restaurant()
mi_cocina.open_restaurant()
'''

### 9.11: Imported Admin

class User():
    def __init__(self, first_name: str, last_name: str, age: int, nacionality: str) -> None:
        ## Initialize attributes to describe a user.
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.nacionality = nacionality
        self.login_attempts = 0

    def describe_user(self):
        print(
            'First Name: ' + self.first_name + '\nLast Name: ' + self.last_name + 
            '\nAge: ' + str(self.age) + '\nNacionality: ' + self.nacionality
        )

    def greet_user(self):
        print('Welcome again ' + self. first_name + ' ' + self.last_name + '!')

    ### 9.5 ###
    def increment_login_attempts(self):
        self.login_attempts += 1

    def reset_login_attempts(self):
        self.login_attempts = 0

class Admin(User):

    def __init__(self, first_name: str, last_name: str, age: int, nacionality: str) -> None:
        super().__init__(first_name, last_name, age, nacionality)
        self.privileges = Privileges()

### 9.8: Privileges ###

class Privileges():

    def __init__(self) -> None:
        self.privileges = ['Can add post', 'Can delete post', 'Can ban user']

    def show_privileges(self):
        print('This administator has the following privileges: ')
        for i in self.privileges:
            print('- ' + i)


#from user import Admin

maestro = Admin('Raul', 'Ovalle', '42', 'Mexicana')

maestro.privileges.show_privileges()


### 9.12: Multiple Modules

class User():
    def __init__(self, first_name: str, last_name: str, age: int, nacionality: str) -> None:
        ## Initialize attributes to describe a user.
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.nacionality = nacionality
        self.login_attempts = 0

    def describe_user(self):
        print(
            'First Name: ' + self.first_name + '\nLast Name: ' + self.last_name + 
            '\nAge: ' + str(self.age) + '\nNacionality: ' + self.nacionality
        )

    def greet_user(self):
        print('Welcome again ' + self. first_name + ' ' + self.last_name + '!')

    ### 9.5 ###
    def increment_login_attempts(self):
        self.login_attempts += 1

    def reset_login_attempts(self):
        self.login_attempts = 0

#from user import  User

class Admin(User):

    def __init__(self, first_name: str, last_name: str, age: int, nacionality: str) -> None:
        super().__init__(first_name, last_name, age, nacionality)
        self.privileges = Privileges()

class Privileges():

    def __init__(self) -> None:
        self.privileges = ['Can add post', 'Can delete post', 'Can ban user']

    def show_privileges(self):
        print('This administator has the following privileges: ')
        for i in self.privileges:
            print('- ' + i)

#from user import User
#from adminPrivileges import Admin

director = Admin('Jesus', 'Rabindranath', 39, 'Mexicana')

director.privileges.show_privileges()

### 9.13: OrderedDict Rewrite ###

from collections import OrderedDict

glosario = OrderedDict()

glosario['String'] = 'Cadena de caracteres'
glosario['int'] = 'Numero entero'
glosario['list'] = 'Coleccion de items en un orden'
glosario['loop'] = 'Trabajar sobre una coleccion de items, uno a la vez'

for i, j in glosario.items():
    print('\n' + i + ': ' + j) 

### 9.14: Dice ###

from random import randint

class Die():
    def __init__(self, sides = 6) -> None:
        self.sides = sides

    def roll_dice(self):
        return randint(1, self.sides)

# dado de 6 lados
d6 = Die()

results = []
for i in range(10):
    result = d6.roll_dice()
    results.append(result)
print(results)

# dado de 10 lados

d10 = Die(sides = 10)

results = []
for i in range(10):
    result = d10.roll_dice()
    results.append(result)
print(results)

# dado de 20 lados

d20 = Die(sides = 20)

results = []
for i in range(10):
    result = d20.roll_dice()
    results.append(result)
print(results)