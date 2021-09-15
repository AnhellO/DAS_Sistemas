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
        print(f"Este auto tiene {self.odometer_reading} millas.")
        
    def update_odometer(self, mileage):
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("¡No se puede hacer retroceder un cuentakilómetros!")
    
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
            
        message = f"Este coche puede recorrer aproximadamente  {range}"
        message += " millas con una carga completa."
        print(message)

    def upgrade_battery(self):
        if self.battery_size == 75:
            self.battery_size = 100
            print("Se actualizó la batería a 100 kW")
        else:
            print("La bateria ya esta actualizada.")
    
        
class ElectricCar(Car):

    def __init__(self, manufacturer, model, year):
        super().__init__(manufacturer, model, year)
        self.battery = Battery()


print("Haz un coche eléctrico y comprueba la autonomía.:")
my_tesla = ElectricCar('tesla', 'roadster', 2019)
my_tesla.battery.get_range()

print("\nActualice la batería y verifique el rango nuevamente:")
my_tesla.battery.upgrade_battery()
my_tesla.battery.get_range()