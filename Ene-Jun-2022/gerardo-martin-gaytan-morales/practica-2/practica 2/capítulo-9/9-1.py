#=============  ejercicio 9-1 ===========
print("========== ejercicio 9-1 ==========")
class Restaurant ():

    def __init__(self,restaurant_name,cuisine_type):
        #"""Initialize name and age attributes."""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
    
    def describe_restaurant(self):
        print("Restaurant name: "+self.restaurant_name.title())
        print("Restaurant name: "+self.cuisine_type.title()+"\n")
    
    def open_restaurant(self):
        print("Restaurant '"+self.restaurant_name.title()+"' is open!!!\n")


#--- instance
restaurant = Restaurant("python","code")
print("------------------------ instances ----------------------")
print("Restaurant name is: "+restaurant.restaurant_name.title())
print("cuisine type is : "+restaurant.cuisine_type.title())

print("------------------------ methods ----------------------\n")
restaurant.describe_restaurant()
restaurant.open_restaurant()


#=============  ejercicio 9-2 ===========
print("========== ejercicio 9-2 ==========")
restaurant1 = Restaurant("lua","code1")
restaurant2 = Restaurant("java","code2")
restaurant3 = Restaurant("ruby","code3")
print("------------------------ methods ----------------------")
restaurant1.describe_restaurant()
restaurant2.describe_restaurant()
restaurant3.describe_restaurant()

#=============  ejercicio 9-3 ===========
print("========== ejercicio 9-3 ==========")

class User():
    def __init__(self,first_name,last_name,phone,years):
        #"""Initialize name and age attributes."""
        self.first_name = first_name
        self.last_name = last_name
        self.phone = phone
        self.years = years

    def describe_user(self):
        print("***** [  Data of user ]  ******")
        print("user name: "+ self.first_name.title() +" "+ self.last_name.title())
        print("phone: "+ self.phone.title())
        print("years: "+self.years.title())
    
    def greet_user(self):
        print("\nHappy Birthday")
        print("Hello "+self.first_name.title() +" "+ self.last_name.title())
        print("reminder of your birthday number: "+self.years.title())

#--- instance

user1 = User("angel","coronado","999869864","67")
user2 = User("oscar","valdes","092573421","66")
user3 = User("pablo","hernandez","9862561683","23")
#--- method
print("----------   method  ----------")
user1.describe_user()
user1.greet_user()
user2.describe_user()
user2.greet_user()
user3.describe_user()
user3.greet_user()


#=============  ejercicio 9-4 ===========
print("\n========== ejercicio 9-4 ==========")
class Restaurant():

    def __init__(self,restaurant_name,cuisine_type):
        #"""Initialize name and age attributes."""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0
    
    def describe_restaurant(self):
        print("Restaurant name: "+self.restaurant_name.title())
        print("Restaurant name: "+self.cuisine_type.title()+"\n")
    
    def open_restaurant(self):
        print("Restaurant '"+self.restaurant_name.title()+"' is open!!!\n")

    def set_number_served(self):
        print("clients: "+str(self.number_served)+"\n")
    
    def increment_number_served(self,miles):
        """Add the given amount to the odometer reading."""
        self.number_served += miles

#--- instance
restaurant = Restaurant("los panchos","mexican")
restaurant.describe_restaurant()
#Setting a Default Value for an Attribute
print("------------------------ Setting a Default Value for an Attribute ----------------------")
restaurant.set_number_served()
#Modifying an Attribute’s Value Directly
print("------------------------ methods modifying ----------------------")
restaurant.number_served= 23
restaurant.set_number_served()
#Incrementing an Attribute’s Value Through a Method
print("-------------- Incrementing an Attribute’s Value Through a Method -----------------")
restaurant.increment_number_served(100)
restaurant.set_number_served()


#=============  ejercicio 9-5 ===========
print("========== ejercicio 9-5 ==========")
class User():
    def __init__(self,first_name,last_name,phone,years):
        #"""Initialize name and age attributes."""
        self.first_name = first_name
        self.last_name = last_name
        self.phone = phone
        self.years = years
        self.login_attempts = 0

    def describe_user(self):
        print("***** [  Data of user ]  ******")
        print("user name: "+ self.first_name.title() +" "+ self.last_name.title())
        print("phone: "+ self.phone.title())
        print("years: "+self.years.title())
        print("login: "+str(self.login_attempts)+"\n")
    
    def greet_user(self):
        print("\nHappy Birthday")
        print("Hello "+self.first_name.title() +" "+ self.last_name.title())
        print("reminder of your birthday number: "+self.years.title())
    
    def incremento_login_attempts(self):
        self.login_attempts += 1

    def reset_login_attempts(self):
        self.login_attempts = 0

#--- instance
user1 = User("angel","coronado","999869864","67")
user1.describe_user()
#------- increment_login_attempts
user1.incremento_login_attempts()
user1.incremento_login_attempts()
user1.incremento_login_attempts()

user1.describe_user()
#-------- reset_ login
user1.reset_login_attempts()
user1.describe_user()


#=============  ejercicio 9-6 ===========
print("========== ejercicio 9-6 ==========")
class IceCreamStand(Restaurant):

    def __init__(self,restaurant_name,cuisine_type):
        """Initialize attributes of the parent class."""
        super().__init__(restaurant_name,cuisine_type)
        self.flavors = ["apple","pineapple","strawberry","lemon"]
    
    def displays_these_flavors(self):
        print("''''''''flavors list''''''''''")
        for i in self.flavors:
            print("flavors: "+i)

ice = IceCreamStand("angel","carlos")
ice.describe_restaurant()
ice.displays_these_flavors()


#=============  ejercicio 9-7 ===========
print("\n========== ejercicio 9-7 ==========")
class Admin(User):
    def __init__(self,first_name,last_name,phone,years):
        """Initialize attributes of the parent class."""
        super().__init__(first_name,last_name,phone,years)
        self.privileges=["can add post", "can delete post", "can ban user"]
    
    def show_privilege(self):
        print("PRIVILEGES")
        for i in self.privileges:
            print(i)

user1 = Admin("angel","coronado","999869864","67")
user1.describe_user()
user1.show_privilege()


#=============  ejercicio 9-8 ===========
print("\n========== ejercicio 9-8 ==========")
class Privileges():
    def __init__(self):
        """Initialize attributes of the parent class."""
        self.privileges=["can add post", "can delete post", "can ban user"]
    
    def show_privilege(self):
        print("PRIVILEGES")
        for i in range(len(self.privileges)):
            print(str(i)+"° "+self.privileges[i])

class Admin1(User):
    def __init__(self,first_name,last_name,phone,years):
        """Initialize attributes of the parent class."""
        super().__init__(first_name,last_name,phone,years)
        #Make a Privileges instance as an attribute in the Admin class
        self.privileges1 = Privileges()

user1 = Admin1("angel","coronado","999869864","67")
user1.privileges1.show_privilege()


#=============  ejercicio 9-9 ===========
print("\n========== ejercicio 9-9 ==========")
class Car():
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

class ElectricCar(Car):
    """Represent aspects of a car, specific to electric vehicles."""
    def __init__(self, make, model, year):
        """Initialize attributes of the parent class.
        Then initialize attributes specific to an electric car.
        """
        super().__init__(make, model, year)
        self.battery = Battery()

class Battery():
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
    def upgrade_battery(self):
        if self.battery_size < 85:
            self.battery_size = 85

my_tesla = ElectricCar('tesla', 'model s', 2016)
print(my_tesla.get_descriptive_name())
my_tesla.battery.describe_battery()
my_tesla.battery.get_range()
print("\n------- upgrade battery --------")
my_tesla.battery.upgrade_battery()
my_tesla.battery.describe_battery()
my_tesla.battery.get_range()


#=============  ejercicio 9-10 ===========
print("\n========== ejercicio 9-10 ==========")
from restaurante import Restaurant1

res = Restaurant1("python","code")
res.describe_restaurant1()


#=============  ejercicio 9-11 ===========
from administrador import Admin2
print("\n========== ejercicio 9-11 ==========")

user1 = Admin2("angel","coronado","999869864","67")
user1.privileges1.show_privilege()


#=============  ejercicio 9-12 ===========
print("\n========== ejercicio 9-12 ==========")
from adminprivileges import Admin2
user1 = Admin2("angel","coronado","999869864","67")
user1.privileges1.show_privilege()


#=============  ejercicio 9-13 ===========
print("\n========== ejercicio 9-13 ==========")
class OrderedDict():
    def __init__(self):
        """Initialize attributes of the parent class."""
        self.favorite_languages = {
            'jen': ['python', 'ruby'],
            'sarah': ['c'],
            'edward': ['ruby', 'go'],
            'phil': ['python', 'haskell'],
            }
    def printt(self):
        for name, languages in self.favorite_languages.items():
            print("\n" + name.title() + "'s favorite languages are:")
            for language in languages:
                print("\t" + language.title())
orde = OrderedDict()
orde.printt()


#=============  ejercicio 9-14 ===========
print("\n========== ejercicio 9-14 ==========")
from random import randint

class Die():
    def __init__(self,cont):
        """Initialize attributes of the parent class."""
        self.sides=6
        self.cont = cont
    
    def roll_die (self):
        for i in range(self.cont):
            x = randint(1, self.sides)
            print(x)
print("dado de 6 lados")
die = Die(10)
die.sides = 6
die.roll_die()
print("dado de 10 lados")
#dado de 20 lados
die1 = Die(10)
die1.sides = 10
die1.roll_die()
print("dado de 20 lados")
#20 lados
die2 = Die(10)
die2.sides = 20
die2.roll_die()


#=============  ejercicio 9-15 ===========
print("\n========== ejercicio 9-15 ==========")
#http://pymotw.com/
#decimal_create.py 
import decimal

fmt = '{0:<25} {1:<25}'

print(fmt.format('Input', 'Output'))
print(fmt.format('-' * 25, '-' * 25))

# Integer
print(fmt.format(5, decimal.Decimal(5)))

# String
print(fmt.format('3.14', decimal.Decimal('3.14')))

# Float
f = 0.1
print(fmt.format(repr(f), decimal.Decimal(str(f))))
print('{:<0.23g} {:<25}'.format(
    f,
    str(decimal.Decimal.from_float(f))[:25])
)

