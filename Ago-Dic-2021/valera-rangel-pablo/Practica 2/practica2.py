# 9-1. Restaurant:
from random import randint


class Restaurant():
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        return(f'Name: {self.restaurant_name} cuisine type is: {self.cuisine_type}')

    def open_restaurant(self):
        return(f'The next restaurant is open: {self.restaurant_name}')

# 9.4 Number Served:
    def set_number_served(self, number_served):
        self.number_served = number_served
        return(f'Number served: {self.number_served}')

    def increment_number_served(self, additional_served):
        self.number_served += additional_served


rest = Restaurant('Los Pollos Hermanos', 'IDK its fake')
print(rest.describe_restaurant())
print(rest.open_restaurant())

# 9.2 Three Restaurants
rest1 = Restaurant('Los Jefes', 'Mexican')
print(rest1.describe_restaurant())
print(rest1.open_restaurant())

rest2 = Restaurant('Krusty Krab', 'Sea Food')
print(rest2.describe_restaurant())
print(rest2.open_restaurant())

rest3 = Restaurant('Krusty Burger', 'Fast Food')
print(rest3.describe_restaurant())
print(rest3.open_restaurant())

restaurant = Restaurant('Burger King', 'Fast Food')
restaurant.number_served = 1
print(restaurant.describe_restaurant())
print(restaurant.open_restaurant(), '\n')
print(restaurant.set_number_served(40), '\n')

# 9.3 Users


class Users():
    def __init__(self, first_name, last_name, age, location):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.location = location
        self.login_attempts = 0

    def describe_User(self):
        desc = (
            f'Name: {self.first_name} {self.last_name}\nAge: {self.age}\nCountry: {self.location}')
        return desc

    def greet_user(self):
        return(f'Nice to see you again {self.first_name} {self.last_name}')

# 9.5 Login Attempts
    def increment_login_attempts(self):
        self.login_attempts += 1
        return(f'Attempt Number: {self.login_attempts}')

    def reset_login_attempts(self):
        self.login_attempts = 0
        return(f'Attempts are now: {self.login_attempts}')


user1 = Users('Pablo', 'Valera', 21, 'Saltillo, Coahuila')
print(user1.describe_User())
print(user1.greet_user())

user2 = Users('Isaac', 'Cisneros', 20, 'Parras, Coahuila')
print(user2.describe_User())
print(user2.greet_user())

user3 = Users('Pedro', 'Mendoza', 20, 'Morelia, Michoacan (Michoacan Family)')
print(user3.describe_User())
print(user3.greet_user())

print(user1.increment_login_attempts())
print(user1.increment_login_attempts())
print(user1.increment_login_attempts())
print(user1.reset_login_attempts())


# Ice Cream Stand
class IceCreamStand(Restaurant):
    def __init__(self, restaurant_name, cuisine_type):
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = []

    def display_flavors(self):
        for flavor in self.flavors:
            print(f'Flavor: {flavor}')


iceCream1 = IceCreamStand('Dairy Queen', 'Desserts')
iceCream1.flavors = ['Cherry', 'Chocolate', 'Lemon']
print(iceCream1.describe_restaurant())
iceCream1.display_flavors()

# 9.7 Admin


class Admin(Users):
    def __init__(self, first_name, last_name, age, location):
        super().__init__(first_name, last_name, age, location)
        self.privileges = []

    def show_privileges(self):
        for privilege in self.privileges:
            print(f'This user can: {privilege}')


admin1 = Admin('Antonio', 'Perez', '25', 'Monterrey, Nuevo Leon')
admin1.privileges = ['Edit', 'Delete', 'Ban']
print(admin1.describe_User())
admin1.show_privileges()


#PENDIENTE: ELECTRIC_CAR.py#
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
        print(f"This car has {self.odometer_reading} miles on it.")

    def update_odometer(self, mileage):
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")

    def increment_odometer(self, miles):
        self.odometer_reading += miles


class Battery():

    def __init__(self, battery_size=75):
        self.battery_size = battery_size

    def describe_battery(self):
        print(f"This car has a {self.battery_size}-kWh battery.")

    def get_range(self):
        if self.battery_size == 75:
            range = 260
        elif self.battery_size == 100:
            range = 315

        message = f"This car can go approximately {range}"
        message += " miles on a full charge."
        print(message)

    def upgrade_battery(self):
        if self.battery_size == 75:
            self.battery_size = 100
            print("Upgraded the battery to 100 kWh.")
        else:
            print("The battery is already upgraded.")


class ElectricCar(Car):

    def __init__(self, manufacturer, model, year):
        super().__init__(manufacturer, model, year)
        self.battery = Battery()


ecar = ElectricCar('tesla', 'roadster', 2019)
ecar.battery.get_range()

ecar.battery.upgrade_battery()
ecar.battery.get_range()

# 9.13 Dice


class Dice():
    def __init__(self, sides):
        self.sides = sides

    def roll_die(self):
        return randint(1, self.sides)


sixSides = Dice(6)
sides = []

for number in range(10):
    side = sixSides.roll_die()
    sides.append(side)

print(f'10/6: {sides}')

tenSides = Dice(10)
sides = []

for number in range(10):
    side = tenSides.roll_die()
    sides.append(side)

print(f'10/10: {sides}')

twSides = Dice(20)
sides = []

for number in range(10):
    side = twSides.roll_die()
    sides.append(side)

print(f'10/20: {sides}')
