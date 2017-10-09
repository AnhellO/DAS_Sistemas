from Electrodomestico import Electrodomestico

class Refrigerador(Electrodomestico):

    def __init__(self, marca, modelo, color, potencia, frecuencia,
    capacidad):
        super().__init__(marca, modelo, color, potencia, frecuencia)
        self.capacidad = capacidad


    def get_capacidad(self):
        return self.capacidad

    def set_capacidad(self, capacidad):
        self.capacidad = capacidad


    def congelar(self):
        info = "Haz metido algo a congelar en la {} {} con {} de capacidad.".format(self.marca,
        self.modelo, self.capacidad)
        return info



# mi_refri = Refrigerador('A', '1', 'Azul',
# '100', '60', '40')
# print(mi_refri.congelar())
