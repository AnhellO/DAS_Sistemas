
class Restourant():
    def __init__(self,restourant_name,cuisine_type):
        self.restourant_name = restourant_name
        self.cuisine_type = cuisine_type
        #? atributo del ejercicio 9.4 
        self.number_serverd = 0

    def describe_restourant(self):
        descripcion =f'{self.restourant_name}, {self.cuisine_type}'
        return descripcion.title()

    def open_restourant(self):
        return (f'Restourant {self.restourant_name.title()} is open ')

    #?add a method of exercise 9.4
    def set_number_served(self,number_serverd):
        self.number_serverd = number_serverd
        return self.number_serverd

    #? metodo que incrementa el numero de clientes atendidos
    def increment_number_serverd(self, increment):
        self.number_serverd += increment    
        return self.number_serverd

my_restourant = Restourant('dominos','fast food')

print('Ejercicio 9.1'.center(100,"="))
print(my_restourant.describe_restourant())
print(my_restourant.open_restourant())
print('='.center(100,"="),'\n')


print('Ejercicio 9.2'.center(100,"="))
my_restourant1 = Restourant('ribs and wings','traditional')
my_restourant2 = Restourant('los compadres','mexican')
my_restourant3 = Restourant('sayulita','fast food')
print(my_restourant1.describe_restourant())
print(my_restourant2.describe_restourant())
print(my_restourant3.describe_restourant())
print('='.center(100,"="),'\n')

class User():
    def __init__(self,first_name,last_name,age,gender,phone_number,marital_status) -> None:
        self.first_name = first_name 
        self.last_name = last_name 
        self.age = age 
        self.gender = gender 
        self.phone_number = phone_number 
        self.marital_status = marital_status 
        #* atributo ejercicio 9.5
        self.login_attempts = 0

    def describe_user(self):
        description = f'Name: {self.first_name}\nLast Name: {self.last_name}\nAge: {self.age}'
        description+= f'\nGender: {self.gender}\nPhone Number: {self.phone_number}\nMarital Status: {self.marital_status}\n'
        return description.title()

    def greet_user(self):
        return f'Hello {self.first_name.title()} have a nice day!!'

    #* metodo 9.5 
    def increment_login_attempts(self):
        self.login_attempts += 1
        return self.login_attempts
    #* metodo 0.5
    def reset_login_attempts(self):
        self.login_attempts = 0
        return self.login_attempts

print('Ejercicio 9.3'.center(100,"="))
user1 = User('edson','amaya',21,'male',84322242422,'single')
user2 = User('rodolfo','aurelio',35,'male',842422423,'married')
print(user1.describe_user())
print(user1.greet_user(),'\n')
print(user2.describe_user())
print(user2.greet_user())
print('='.center(100,"="),'\n')


print('Ejercicio 9.4'.center(100,"="))
 #* crear una nueva instancia de restourante e imprimir customer
my_restourant9 = Restourant('dominos','fast food')
print(f'numero de clientes atendidos: {my_restourant9.number_serverd}')
my_restourant9.number_serverd = 5
print(f'numero de clientes atendidos: {my_restourant9.number_serverd}')
my_restourant9.set_number_served(10)
print(f'numero de clientes atendidos : {my_restourant9.number_serverd} modificado del metodo')
my_restourant9.increment_number_serverd(10)
print(f'numero de clientes atendidos incremento: {my_restourant9.number_serverd}')
print('='.center(100,"="),'\n')

print('Ejercicio 9.5'.center(100,"="))
user3 = User('pepe','cienfuenegos',32,'male',38533232,'single')
user3.increment_login_attempts()
user3.increment_login_attempts()
user3.increment_login_attempts()
print(f'Numero de intentos {user3.login_attempts}')
user3.reset_login_attempts()
print(f'Reseteo de Numero de intentos {user3.login_attempts}')
print('='.center(100,"="),'\n')

class IceCreamStand(Restourant):

    def __init__(self, name, cuisine_type):        
        super().__init__(name, cuisine_type)
        self.flavors = []

    def display_flavors(self):        
        print("\nTenemos los siguientes sabores disponibles:")
        for flavor in self.flavors:
            print(f'--{flavor.title()}--')


ice_cream = IceCreamStand('vaca la norteñita','ice cream')
ice_cream.flavors = ['chocolate','vainilla','pistache','napolitano']


print('Ejercicio 9.6'.center(100,"="))
print(ice_cream.display_flavors())
print('='.center(100,"="),'\n')

class Admin(User):
    def __init__(self,first_name,last_name,age,gender,phone_number,marital_status):
        super().__init__(first_name,last_name,age,gender,phone_number,marital_status)

        self.privileges = Privileges()

    #* metodo ejercicio 9.7
"""    def show_privileges(self):
        print(f'-----The admin {self.first_name}-----')
        for privileges in self.privileges:
            print(f'-{privileges}') """

""" print('Ejercicio 9.7'.center(100,"="))
admin1 = Admin('Edson','amaya',21,'male',83334858343,'single')
print(admin1.describe_user())
admin1_privileges =["can add post","can delete post","can ba user"]
admin1.show_privileges()
print('='.center(100,"="),'\n') """

class Privileges():  
    def __init__(self, privileges=[]):
        self.privileges = privileges

    def show_privileges(self):
        print('-----The admin -----')        
        for privilege in self.privileges:
            print("- " + privilege)


print('Ejercicio 9.7'.center(100,"="))
admin1 = Admin('edson','amaya',21,'male',83334858343,'single')
print(admin1.describe_user())
admin1_privileges =["can add post","can delete post","can ba user"]
admin1.privileges.privileges = admin1_privileges
admin1.privileges.show_privileges()
print('='.center(100,"="),'\n')


print('Ejercicio 9.8'.center(100,"="))
admin2 = Admin('Mario','amlaguer',21,'male',83334858343,'single')
print(admin2.describe_user())

admin2_privileges =["can add post","can delete post","can ba user"]
admin2.privileges.privileges = admin2_privileges
admin2.privileges.show_privileges()
print('='.center(100,"="),'\n')

class Car():
    """A simple attempt to represent a car."""

    def __init__(self, manufacturer, model, year):
        """Initialize attributes to describe a car."""
        self.manufacturer = manufacturer
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        """Return a neatly formatted descriptive name."""
        long_name = str(self.year) + ' ' + self.manufacturer + ' ' + self.model
        return long_name.title()

    def read_odometer(self):
        """Print a statement showing the car's mileage."""
        print("This car has " + str(self.odometer_reading) + " miles on it.")

    def update_odometer(self, mileage):
        """
        Set the odometer reading to the given value.
        Reject the change if it attempts to roll the odometer back.
        """
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")

    def increment_odometer(self, miles):
        """Add the given amount to the odometer reading."""
        self.odometer_reading += miles

class Battery():

    def __init__(self, battery_size=60):        
        self.battery_size = battery_size

    def describe_battery(self):

        print(f'Este carro tiene {self.battery_size}-kWh de bateria.')


    def get_range(self):        
        if self.battery_size == 60:
            range = 140
        elif self.battery_size == 85:
            range = 185

        message = f'El carro puede recorrer {range}'
        message += " millas con carga llena"
        print(message)

    def upgrade_battery(self):        
        if self.battery_size == 60:
            self.battery_size = 85
            print("Bateria recargada a 85-kWh.")
        else:
            print("La bateria ya esta recargada.")


class ElectricCar(Car):
    """Models aspects of a car, specific to electric vehicles."""

    def __init__(self, manufacturer, model, year):
        """
        Initialize attributes of the parent class.
        Then initialize attributes specific to an electric car.
        """
        super().__init__(manufacturer, model, year)
        self.battery = Battery()





print('Ejercicio 9.9'.center(100,"="))


my_tesla = ElectricCar('tesla', 'model s', 2016)
my_tesla.battery.describe_battery()

print("\nRecargando la bateria..")
my_tesla.battery.upgrade_battery()
my_tesla.battery.describe_battery()
my_tesla.battery.get_range()


print("\n")
my_tesla.battery.upgrade_battery()
my_tesla.battery.describe_battery()
print('='.center(100,"="),'\n')






























