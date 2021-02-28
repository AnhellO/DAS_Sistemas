import random, time

tipos = [
    'coche',
    'autobus',
    'trailer',
]

print('tipo de auto...')
time.sleep(2)
#print(random.choice(tipos)) 'Comenté la ejecución para que no provocara confusión con el resultado de main.py'

class vehicle(object):

    def __init__(self, velocidad_maxima, kilometraje, capacidad):
        self.velocidad_maxima = velocidad_maxima
        self.kilometraje = kilometraje
        self.capacidad = capacidad

        def set_velocidad_maxima(self, velocidad_maxima):
            self.velocidad_maxima = velocidad_maxima

        def get_velocidad_maxima(self):
            return self.velocidad_maxima

        def set_capacidad(self, capacidad):
            self.capacidad = capacidad

        def get_capacidad(self):
            return self.capacidad
            
        def set_kilometraje(self, kilometraje):
            self.kilometraje = kilometraje

        def get_kilometraje(self):
            return self.kilometraje

    def __str__(self):
        return "Soy un {} y corro a: {} km/h \n Tengo {}km recorridos\n y llevo hasta: {} pasajeros\n".format(tipos, self.velocidad_maxima, self.kilometraje, self.capacidad).strip()

'''v = vehicle(260, 100000, 5)
print(v)'''