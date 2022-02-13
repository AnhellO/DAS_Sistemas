"""9-9. Battery Upgrade:

Use the final version of electric_car.py from this section .
Add a method to the Battery class called upgrade_battery() . This method
should check the battery size and set the capacity to 85 if it isn’t already .
Make an electric car with a default battery size, call get_range() once, and
then call get_range() a second time after upgrading the battery . You should
see an increase in the car’s range."""

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
        print(f"Este coche tiene {self.odometer_reading} millas en él.")
        
    def update_odometer(self, mileage):
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("No se puede hacer retroceder un odómetro")
    
    def increment_odometer(self, miles):
        self.odometer_reading += miles

class Battery():
    def __init__(self, battery_size=75):
        self.battery_size = battery_size

    def describe_battery(self):
        print(f"Este coche tiene una batería de {self.battery_size}-kWh.")

    def get_range(self):
        if self.battery_size == 75:
            range = 260
        elif self.battery_size == 100:
            range = 315
            
        message = f"Este coche puede recorrer {range}"
        message += " millas con la bateria al maximo."
        print(message)

    def upgrade_battery(self):
        if self.battery_size == 75:
            self.battery_size = 100
            print("Se actualizó la batería a 100 kWh.")
        else:
            print("La batería ya ha sido actualizada.")
    
class ElectricCar(Car):
    def __init__(self, manufacturer, model, year):
        super().__init__(manufacturer, model, year)
        self.battery = Battery()

print("Fabrica un coche eléctrico y comprueba la autonomía:")
my_tesla = ElectricCar('Tesla', 'Modelo 3', 2020)
my_tesla.battery.get_range()

print("\nActualice la batería y verifique la autonomia nuevamente:")
my_tesla.battery.upgrade_battery()
my_tesla.battery.get_range()