# Práctica 2
# -------------------------------------------------------------------------------------------------------
# Objetivo
#   Mejorar en el aprendizaje y conocimiento sobre Python

# Especificaciones
#   Llevar a cabo todos los ejercicios del capítulo 9 del libro de Python Crash Course (del 9-1 al 9-15)

# Deadline
#   Miércoles 15 de Septiembre a las 11:59pm

# TRY IT YOURSELF 9-1. Restaurant Class
class Restaurant():

    def __init__(self, restaurant_name, cuisine_type) -> None:
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.served_number = 0

    def describe_restaurant(self):
        print("Restaurant's Name: {} - Cuisine Type: {} ".format(self.restaurant_name, self.cuisine_type))

    def open_restaurant(self):
        print("The restaurant has opened!")

    def number_served(self):
        print("Curstomers served: {}".format(self.served_number))

    def set_number_served(self, number_served):
        self.served_number = number_served

    def increment_number_served(self, increment):
        self.served_number += increment


# TRY IT YOURSELF 9-1. Restaurant Results
print('# TRY IT YOURSELF 9-1. Restaurant Results')

restaurant = Restaurant("Bistek Restaurant", "Traditional")
restaurant.describe_restaurant()
restaurant.open_restaurant()

# TRY IT YOURSELF 9-2. Restaurant Results
print('\nTRY IT YOURSELF 9-2. Restaurant Results')

restaurant1 = Restaurant("Restaurant 1", "Traditional")
restaurant2 = Restaurant("Restaurant 2", "German")
restaurant3 = Restaurant("Restaurant 3", "Korean")

restaurant1.describe_restaurant()
restaurant2.describe_restaurant()
restaurant3.describe_restaurant()


# TRY IT YOURSELF 9-3. User Class
class User():
    def __init__(self, first_name, last_name) -> None:
        self.first_name = first_name
        self.last_name = last_name
        self.login_attempts = 0

    def describe_user(self):
        print("User's Name: {} - User's Last Name: {} - User's login attempts: {}".format(
            self.first_name, self.last_name, self.login_attempts))

    def greet_user(self):
        print('Hello {}!'.format(self.first_name))

    def increment_login_attempts(self):
        self.login_attempts += 1

    def reset_login_attempts(self):
        self.login_attempts = 0


# TRY IT YOURSELF 9-3. User Results
print('\nTRY IT YOURSELF 9-3. User Results')

user1 = User('Mario', 'Almaguer')
user2 = User('Edson', 'Amaya')
user3 = User('Erick', 'Diaz')

user1.describe_user()
user1.greet_user()
user2.describe_user()
user2.greet_user()
user3.describe_user()
user3.greet_user()

# TRY IT YOURSELF 9-4. Number Served Results
print('\nTRY IT YOURSELF 9-4. Number Served Results')
restaurant4 = Restaurant('Restaurant 9-4', 'Indian')
restaurant4.describe_restaurant()
restaurant4.number_served()
restaurant4.set_number_served(1)
restaurant4.number_served()
restaurant4.increment_number_served(4)
restaurant4.number_served()

# TRY IT YOURSELF 9-5. Login Attempts Results
print('\nTRY IT YOURSELF 9-5. Login Attempts Results')
user4 = User('Humberto', 'Najera')
user4.describe_user()
user4.increment_login_attempts()
user4.increment_login_attempts()
user4.increment_login_attempts()
user4.increment_login_attempts()
user4.describe_user()
user4.reset_login_attempts()
user4.describe_user()

# TRY IT YOURSELF 9-6. Ice Cream Stand Class
class IceCreamStand(Restaurant):

    def __init__(self, restaurant_name, cuisine_type) -> None:
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = ['Vanilla', 'Chocolate', 'Strawberry']

    def display_flavors(self):
        print('Available flavors: {}'.format(self.flavors))


# TRY IT YOURSELF 9-6. Ice Cream Stand Results
print('\nTRY IT YOURSELF 9-6. Ice Cream Stand Results')
stand1 = IceCreamStand('Creamy Ice', 'Ice Creams')
stand1.display_flavors()

# EL ORDEN DE ESTA CLASE ES NECESARIO DE OTRA MANERA NO FUNCIONA
# TRY IT YOURSELF 9-8. Privileges Class
class Privileges():

    def __init__(self):
        self.privileges = ['can add post', 'can delete post', 'can modify post']

    def show_privileges(self):
        print("Admin's Privileges: {}".format(self.privileges))

# TRY IT YOURSELF 9-7. Admin Class
class Admin(User):

    def __init__(self, first_name, last_name) -> None:
        super().__init__(first_name, last_name)
        self.privileges = Privileges()


# TRY IT YOURSELF 9-7. Admin Class Results
print('\nTRY IT YOURSELF 9-7. Admin Class Results')
admin1 = Admin('ADMIN', 'ADMIN')

# Se mueve a la siguiente clase siguiendo el libro.
# admin1.show_privileges()

# TRY IT YOURSELF 9-8. Privileges Results
print('\nTRY IT YOURSELF 9-8. Privileges Results')
admin2 = Admin('ADMIN2', 'ADMIN2')
admin2.privileges.show_privileges()

#TRY IT YOURSELF 9-9. Car, Electric Car, Battery Classes
class Car:
    
    """A simple attempt to represent a car."""
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
    

class Battery:

    """A simple attempt to model a battery for an electric car."""
    def __init__(self, battery_size=70):
        """Initialize the battery's attributes."""
        self.battery_size = battery_size

    def describe_battery(self):
        """Print a statement describing the battery size."""
        
        print("This car has a " + str(self.battery_size) + "-kWh battery.")

    def get_range(self):
        """Print a statement about the range this battery provides."""
        if self.battery_size == 70:
            range = 240
        elif self.battery_size == 85:
            range = 270

        message = "This car can go approximately " + str(range)
        message += " miles on a full charge."
        print(message)

    def update_battery(self):
        if (self.battery_size != 85):
            self.battery_size = 85


class ElectricCar(Car):

    def __init__(self, make, model, year):
        """Initialize attributes of the parent class."""
        super().__init__(make, model, year)
        self.battery = Battery()

    def describe_battery(self):
        """Print a statement describing the battery size."""
        print("This car has a " + str(self.battery_size) + "-kWh battery.")

# TRY IT YOURSELF 9-9. Car, Electric Car, Battery Results
print('\n#TRY IT YOURSELF 9-9. Car, Electric Car, Battery Results')

electricCar1 = ElectricCar('Tesla', 'Model S', '2016')
electricCar1.battery.get_range()
electricCar1.battery.update_battery()
electricCar1.battery.get_range()

# TRY IT YOURSELF 9-10 Imported Restaurant
# SE REALIZO EN EL ARCHIVO tryItYourself_9_10.py
# CLASES REQUERIDAS: modules.py

# TRY IT YOURSELF 9-11 Imported Admin
# SE REALIZO EN EL ARCHIVO tryItYourself_9_11.py
# CLASES REQUERIDAS: modules.py

# TRY IT YOURSELF 9-12 Multiple Modules
# SE REALIZO EN EL ARCHIVO tryItYourself_9_12.py
# CLASES REQUERIDAS: modules.py && user.py

# TRY IT YOURSELF 9-13 OrderedDict Rewrite
print('\nTRY IT YOURSELF 9-13 OrderedDict Rewrite Results')
from collections import OrderedDict

glossary = OrderedDict()

glossary['string'] = 'A series of characters.'
glossary['comment'] = 'A note in a program that the Python interpreter ignores.'
glossary['list'] = 'A collection of items in a particular order.'
glossary['loop'] = 'Work through a collection of items, one at a time.'
glossary['dictionary'] = "A collection of key-value pairs."
glossary['key'] = 'The first item in a key-value pair in a dictionary.'
glossary['value'] = 'An item associated with a key in a dictionary.'
glossary['conditional test'] = 'A comparison between two values.'
glossary['float'] = 'A numerical value with a decimal component.'
glossary['boolean expression'] = 'An expression that evaluates to True or False.'

for word, definition in glossary.items():
    print("\n" + word.title() + ": " + definition)

# TRY IT YOURSELF 9-14 Dice
print('\nTRY IT YOURSELF 9-14 Dice Results')

from random import randint
dice_result = randint(1, 6)
print('\nEl resultado del dado es: {} '.format(dice_result))

class Dice:
    def __init__(self, sides = 6) -> None:
        self.sides = sides

    def roll_dice(self):
        return randint(1, self.sides)

    def roll_ten_times(self):
        for i in range(10):
            print('El resultado del dado en la tirada {} es: {}'.format(i + 1, self.roll_dice()))


# Dado de 10 lados, y lanzarlo 10 veces.
dice_ten = Dice(10)
dice_ten.roll_ten_times()

# Dado de 20 lados, y lanzarlo 10 veces.
dice_twenty = Dice(20)
dice_twenty.roll_ten_times()

