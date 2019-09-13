#Use the final version of electric_car.py from this section.
#Add a method to the Battery class called upgrade_battery(). This method
#should check the battery size and set the capacity to 85 if it isn’t already.
#Make an electric car with a default battery size, call get_range() once, and
#then call get_range() a second time after upgrading the battery. You should
#see an increase in the car’s range.
class Car():

    def __init__(self, manufacturer, model, year):
        """Atributos del carro"""
        self.manufacturer = manufacturer
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        """nombre descriptivo"""
        long_name = str(self.year) + ' ' + self.manufacturer + ' ' + self.model
        return long_name.title()

    def read_odometer(self):
        """kilometraje del carro"""
        print("This car has " + str(self.odometer_reading) + " miles on it.")

    def update_odometer(self, mileage):
        """
        Ajuste la lectura del odómetro al valor dado.
        Rechace el cambio si intenta hacer retroceder el odómetro.
        """
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")

    def increment_odometer(self, miles):
        """Agregar la cantidad dada a la lectura del odómetro"""
        self.odometer_reading += miles

class Battery():
    """Modelando bateria de coche eléctrico"""

    def __init__(self, battery_size=60):
        """Atributos de la bateria"""
        self.battery_size = battery_size

    def describe_battery(self):
        """Tamaño de la bateria"""
        print("Este carro tiene una bateria de " + str(self.battery_size) + " kWh")

    def get_range(self):
        """Rango de bateria"""
        if self.battery_size == 60:
            range = 140
        elif self.battery_size == 85:
            range = 185

        message = "Este carro puede ir aproximadamente " + str(range)
        message += " millas"
        print(message)

    def upgrade_battery(self):
        """Actualizar bateria"""
        if self.battery_size == 60:
            self.battery_size = 85
            print("Se actualizo la batería a 85 kWh.")
        else:
            print("Batería actualizada")


class ElectricCar(Car):
    """Modelos de aspectos de un coche, específicos para vehículos eléctricos."""

    def __init__(self, manufacturer, model, year):
        """
        Inicializar atributos de la clase padre.
        Luego inicialice los atributos específicos de un coche eléctrico.
        """
        super().__init__(manufacturer, model, year)
        self.battery = Battery()


print("Haz un coche eléctrico y checa la batería: ")
my_tesla = ElectricCar('tesla', 'model s', 2016)
my_tesla.battery.describe_battery()

print("\nActualiza la batería y revísela de nuevo:")
my_tesla.battery.upgrade_battery()
my_tesla.battery.describe_battery()

print("\nActualiza la bateria una segunda vez.")
my_tesla.battery.upgrade_battery()
my_tesla.battery.describe_battery()