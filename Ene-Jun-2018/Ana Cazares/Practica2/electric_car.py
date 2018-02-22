class Car():
    """Un simple intento de representar un auto"""

    def __init__(self, manufacturer, model, year):
        """Inicializar atributos para describir un automóvil."""
        self.manufacturer = manufacturer
        self.model = model
        self.year = year
        self.odometer_reading = 0
        
    def get_descriptive_name(self):
        """Devuelve un nombre descriptivo prolijamente formateado."""
        long_name = str(self.year) + ' ' + self.manufacturer + ' ' + self.model
        return long_name.title()
    
    def read_odometer(self):
        """Imprima una declaración que muestre el millaje del automóvil."""
        print("Este automóvil tiene" + str(self.odometer_reading) + " miles on it.")
        
    def update_odometer(self, mileage):
        """
        Establezca la lectura del odómetro en el valor dado.
        Rechace el cambio si intenta hacer retroceder el odómetro.
        """
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("No puedes hacer retroceder un odómetro!")
    
    def increment_odometer(self, miles):
        """Agregue la cantidad dada a la lectura del odómetro."""
        self.odometer_reading += miles

class Battery():
    """Un simple intento de modelar una batería para un automóvil eléctrico."""

    def __init__(self, battery_size=60):
        """Inicializar los atributos del batteery."""
        self.battery_size = battery_size

    def describe_battery(self):
        """Imprima una declaración que describa el tamaño de la batería."""
        print("Este automóvil tiene una " + str(self.battery_size) + "-kWh battery.")

        
    def get_range(self):
        """Imprime una declaración sobre el alcance que proporciona esta batería"""
        if self.battery_size == 60:
            range = 140
        elif self.battery_size == 85:
            range = 185
            
        message = "Este automóvil puede ir aproximadamente " + str(range)
        message += " millas con una carga completa."
        print(message)

    def upgrade_battery(self):
        """Actualice la batería si es posible."""
        if self.battery_size == 60:
            self.battery_size = 85
            print("Actualizó la batería a 85 kWh.")
        else:
            print("La batería ya está actualizada")
    
        
class ElectricCar(Car):
    """Aspectos de modelos de un automóvil, específicos de vehículos eléctricos."""

    def __init__(self, manufacturer, model, year):
        """
        Inicializar atributos de la clase padre.
        A continuación, inicialice los atributos específicos de un automóvil eléctrico.
        """
        super().__init__(manufacturer, model, year)
        self.battery = Battery()


print("Hacer un automóvil eléctrico y verificar la batería:")
my_tesla = ElectricCar('tesla', 'model s', 2016)
my_tesla.battery.describe_battery()

print("\nActualice la batería y revísela nuevamente:")
my_tesla.battery.upgrade_battery()
my_tesla.battery.describe_battery()

print("\nIntente actualizar la batería por segunda vez.")
my_tesla.battery.upgrade_battery()
my_tesla.battery.describe_battery()
