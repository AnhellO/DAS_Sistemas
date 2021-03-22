import random as rn


class vehiculo:

    def __init__(self, velocidad_maxima, kilometraje, capacidad):
        self.velocidad_maxima = velocidad_maxima
        self.kilometraje = kilometraje
        self.capacidad = capacidad

    random = rn.randint(0, 50)

    def __str__(self):
        return f'La velocidad maxima es de {self.velocidad_maxima} km/h\n' \
               f'Tiene un kilometraje de {self.kilometraje}\n' \
               f'Con una capacidad de {self.capacidad} pasajeros\n' \
               f'Con un numero random de {self.random}'

    def tarifa(self):
        return float(self.capacidad * 100)