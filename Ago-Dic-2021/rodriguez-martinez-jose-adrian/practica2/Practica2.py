###   PRACTICA 9.1   ###
print('\n\nPractica 9.1')
class Restaurant():
    def __init__(self, name, cuisine):
        self.name = name
        self.cuisine = cuisine
        self.number_served = 0

    def increment_num_served(self, update):
        self.number_served = update
        return f"Number served: {self.number_served}"

    def describe_restaurant(self):
        return f"Restaurant name: {self.name}\nCuisine type: {self.cuisine}"
    
    def open_restaurant(self):
        return f"Restaurant {self.name} is now open"

rest = Restaurant("Pizzeria" ,"Italiana")
print(rest.name)
print(rest.cuisine)
print(rest.describe_restaurant())
print(rest.open_restaurant())


###   PRACTICA 9.2 ###
print('\n\nPractica 9.2')
res1 = Restaurant('Liru Sisa', 'Pizzeria')
res2 = Restaurant('Chicken Only', 'Polleria')
res3 = Restaurant('Carls Jr', 'Hamburguesas')

print(res1.describe_restaurant())
print(res2.describe_restaurant())
print(res3.describe_restaurant())


###   PRACTICA 9.3 ###
print('\n\nPractica 9.3')
class User():
    def __init__(self, first_name, last_name, id, username):
        self.first_name = first_name
        self.last_name = last_name
        self.id = id
        self.username = username
        self.login_attempts = 0
    
    def increment_login_attempts(self):
        self.login_attempts = self.login_attempts + 1

    def reset_login_attempts(self):
        self.login_attempts = 0

    def describe_user(self):
        return  f"ID: {self.id}\nUsername: {self.username}\nName:{self.first_name} {self.last_name}"
    
    def greet_user(self):
        return f"Hello {self.first_name}, Welcome!!!! :)"

u1 = User('Adrian', 'Rodriguez', 1, 'jarmarj')
u2 = User('Sergio', 'Villanueva', 2, 'checobuenhombre')

print(u1.describe_user())
print(u1.greet_user())

print(u2.describe_user())
print(u2.greet_user())


###   PRACTICA 9.4 ###
print('\n\nPractica 9.4')

restaurant = Restaurant('Pizzeria', 'Italiana')
print('Number served: ' + str(restaurant.number_served))
print(restaurant.increment_num_served(10))


###   PRACTICA 9.5 ###
print('\n\nPractica 9.5')
usuario = User('Adrian', 'Rodriguez', 2, 'jarmarj')
usuario.increment_login_attempts()
usuario.increment_login_attempts()
usuario.increment_login_attempts()
usuario.increment_login_attempts()
usuario.increment_login_attempts()
print('Login attempts: ' + str(usuario.login_attempts))

usuario.reset_login_attempts()
print('Login attempts: ' + str(usuario.login_attempts))


###   PRACTICA 9.6 ###
print('\n\nPractica 9.6')
class IceCreamStand(Restaurant):
    def __init__(self, name, cuisine):
        super().__init__(name, cuisine)
        self.flavors = ['Chocolate', 'Vainilla', 'Fresa']
    
    def print_flavors(self):
        for flavor in self.flavors:
            print(flavor)

stand = IceCreamStand('Heladeria', 'Helados')
stand.print_flavors()


###   PRACTICA 9.7 ###
print('\n\nPractica 9.7 está comentada por cambios, ver practica 9.8')
class Admin(User):
    def __init__(self, first_name, last_name, id, username):
        super().__init__(first_name, last_name, id, username)
        self.privileges = Privileges()
    
"""admin = Admin('Jose', 'Martinez', 1, 'jose')
admin.show_privileges()"""


###   PRACTICA 9.8 ###
print('\n\nPractica 9.8')
class Privileges():
    def __init__(self, privileges = ['can add post', 'can delete post', 'can ban user']) -> None:
        self.privileges = privileges

    def show_privileges(self):
        for i in self.privileges:
            print(i)

admin1 = Admin('Pepe', 'Martinez', 4, 'pp')
admin1.privileges.show_privileges()

###   PRACTICA 9.9 ###
print('\n\nPractica 9.9')
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

class ElectricCar(Car):
    def __init__(self, make, model, year):
        super().__init__(make, model, year)
        self.battery = Battery()

    def fill_gas_tank():
        print("This car doesn't need a gas tank!")

class Battery():
    def __init__(self, battery_size=70):
        self.battery_size = battery_size

    def describe_battery(self):
        print("This car has a " + str(self.battery_size) + "-kWh battery.")
    
    def get_range(self):
        if self.battery_size == 70:
            range = 240
            print('Range of the car: ' + str(range))
        elif self.battery_size == 85:
            range = 270
            message = "This car can go approximately " + str(range)
            message += " miles on a full charge."
            print(message)

    def upgrade_battery(self):
        if self.battery_size != 85:
            self.battery_size = 85

electrico = ElectricCar('Tesla', 'S', 2021)
electrico.battery.get_range()
electrico.battery.upgrade_battery()
electrico.battery.get_range()

