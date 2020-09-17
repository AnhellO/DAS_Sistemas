class Carro(object):
    def __init__(self, name_car, año, kilometraje):
        self.name_car = name_car
        self.año = año
        self.kilometraje = kilometraje

    #Getters and Setters
    def set_name_car(self, name_car):
        self.name_car = name_car

    def set_año(self, año):
        self.año = año

    def set_kilometraje(self, kilometraje):
        self.kilometraje = kilometraje

    def get_name_car(self):
        return self.name_car

    def get_año(self):
        return self.año

    def get_kilometraje(self):
        return self.kilometraje

    def CarIsFlying (self):
        return print('WTF? Your ' + self.name_car + ' is flying!! DD:')

carrito = Carro('Mazda', '2017',1200)
# print(carrito.name_car)
# carrito.CarIsFlying()

class ElecricCar (Carro):
    def __init__(self, name_car, año, kilometraje):
        super().__init__(name_car, año, kilometraje)

my_tesla = ElecricCar('Tesla', '2018', 2000)
print(my_tesla.año)
my_tesla.CarIsFlying()


