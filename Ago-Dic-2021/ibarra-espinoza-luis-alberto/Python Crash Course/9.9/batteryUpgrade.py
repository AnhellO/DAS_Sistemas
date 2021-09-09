### 9.9: Battery Upgrade ###

class Car():

    def __init__(self, make, model, year) -> None:
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name
    
    def read_odometer(self):
        print('This car has ' + str(self.odometer_reading) + ' miles on it.')

    def update_odometer(self, mileage: int):
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")

    def increment_odometer(self, miles: int):
        self.odometer_reading += miles

class Battery():

    def __init__(self, battery_size = 70) -> None:
        self.battery_size = battery_size

    def describe_battery(self):
        print("This car has a " + str(self.battery_size) + "-kWh battery.")

    def get_range(self):
        if self.battery_size == 70:
            range = 240
        elif self.battery_size == 85:
            range = 270
        
        message = 'This car can go approximately ' + str(range)
        message += ' miles on a full charge.'
        print(message)

    def upgrade_battery(self):
        if self.battery_size == 70:
            self.battery_size = 85
            print('Upgraded the battery to 85 kWh.')
        else:
            print('The battery is already upgraded.')

class ElectricCar(Car):

    def __init__(self, make, model, year) -> None:
        super().__init__(make, model, year)
        self.battery = Battery()
        

my_tesla = ElectricCar('Tesla', 'Model S', '2016')
my_tesla.battery.get_range()
my_tesla.battery.upgrade_battery()
my_tesla.battery.get_range()