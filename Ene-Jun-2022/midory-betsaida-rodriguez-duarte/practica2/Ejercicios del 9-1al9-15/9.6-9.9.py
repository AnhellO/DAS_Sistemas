#9.6
class Restaurante():

    def __init__(self, nombreRes, tipoCoci):
        self.nombreRes = nombreRes
        self.tipiCoci = tipoCoci

    
    def describe_restaurante(self):
        print("El nombre del res es" + self.nombreRes + "y su tipo es " + self.tipiCoci)

    def abierto():
        print("El restaurante es abierto")

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
heladochico.flavors = [ 'nuez', 'napolitano']

heladochico.describe_restaurante()
heladochico.show_flavors()        

restaurante = Restaurante('carls jr', 'hamburguesas')
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
