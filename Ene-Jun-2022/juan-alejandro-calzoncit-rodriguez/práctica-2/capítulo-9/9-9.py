from car import Car

class Battery():

    def __init__(self, battery_size=70):
        self.battery_size = battery_size

    def describe_battery(self):
        print("This car has a " + str(self.battery_size) + "-kWh battery.")        

    def upgrade_battery(self):
        if self.battery_size == 70:
            self.battery_size = 85

    def get_range(self):
        if self.battery_size == 70:
            range = 240
        elif self.battery_size == 85:
            range = 270
        message = "This car can go approximately " + str(range)
        message += " miles on a full charge."
        print(message)        


class ElectricCar(Car):

    def __init__(self, make, model, year):    
        super().__init__(make, model, year)
        self.battery = Battery()

    def fill_gas_tank():
        print("This car doesn't need a gas tank!")        



my_tesla = ElectricCar('tesla', 'model s', 2016)
my_tesla.battery.get_range()
my_tesla.battery.upgrade_battery()
my_tesla.battery.get_range()