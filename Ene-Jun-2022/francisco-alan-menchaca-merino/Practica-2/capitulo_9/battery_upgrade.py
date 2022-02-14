class Car():
    """A simple attempt to represent a car.
    9-9. Battery Upgrade: Use the final version of electric_car.py from this section."""

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
    """A simple attempt to model a battery for an electric car."""

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

    # Add a method to the Battery class called upgrade_battery(). This method should
    # check the battery size and set the capacity to 85 if it isn't already.
    def upgrade_battery(self):
        if self.battery_size == 70:
            self.battery_size = 85
            print("Upgrading the battery size to 85-kWh.")
        else:
            print("The battery has already been upgrading")


class ElectricCar(Car):
    """Represent aspects of a car, specific to electric vehicles."""

    def __init__(self, make, model, year):
        super().__init__(make, model, year)
        self.battery = Battery()


# Make an electric car with a default battery size, call get_range() once, and then call
# get_range() a second time after upgrading the battery. You should see an increase
# in the car's range.
my_tesla = ElectricCar('tesla', 'model x', 2022)
print(my_tesla.get_descriptive_name())
my_tesla.battery.describe_battery()
my_tesla.battery.get_range()

print("\nBaterry Upgraded")
my_tesla.battery.upgrade_battery()
my_tesla.battery.get_range()

# 2022 Tesla Model X
# This car has a 70-kWh battery.
# This car can go approximately 240 miles on a full charge.

# Baterry Upgraded
# Upgrading the battery size to 85-kWh.
# This car can go approximately 270 miles on a full charge.
