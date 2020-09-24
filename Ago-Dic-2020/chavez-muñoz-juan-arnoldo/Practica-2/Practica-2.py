class Carro(object):
    def __init__(self, name_car, modelo, kilometraje):
        self.name_car = name_car
        self.modelo = modelo
        self.kilometraje = kilometraje

    #Getters and Setters
    def set_name_car(self, name_car):
        self.name_car = name_car

    def set_modelo(self, modelo):
        self.modelo = modelo

    def set_kilometraje(self, kilometraje):
        self.kilometraje = kilometraje

    def get_name_car(self):
        return self.name_car

    def get_modelo(self):
        return self.modelo

    def get_kilometraje(self):
        return self.kilometraje

    def car_is_flying (self):
        return print('WTF? Your ' + self.name_car + ' is flying!! DD:')

carrito = Carro('Mazda', '2017',1200)
# print(carrito.name_car)
# carrito.CarIsFlying()

class ElecricCar (Carro):
    def __init__(self, name_car, modelo, kilometraje, nuevo):
        super().__init__(name_car, modelo, kilometraje)
        self.es_nuevo = nuevo
        self.value = 50000
    
    def print_value(self):
        print(self.value)

my_tesla = ElecricCar('Tesla', '2018', 2000, True)
print(my_tesla.modelo)
my_tesla.car_is_flying()
my_tesla.print_value()
