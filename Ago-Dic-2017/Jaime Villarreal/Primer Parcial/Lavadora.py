from Electrodomestico import Electrodomestico

class Lavadora(Electrodomestico):

    def __init__(self, marca, modelo, color, potencia, frecuencia,
    cargas_ropa):
        super().__init__(marca, modelo, color, potencia, frecuencia)
        self.cargas_ropa = cargas_ropa


    def get_cargas_ropa(self):
        return self.cargas_ropa

    def set_cargas_ropa(self, cargas_ropa):
        self.cargas_ropa = cargas_ropa


    def lavar(self):
        info = "Haz metido algo a lavar en la {} {} con {} cargas de ropa.".format(self.marca,
        self.modelo, self.cargas_ropa)
        return info



# mi_lav = Lavadora('A', '1', 'Azul',
# '100', '60', '40')
# print(mi_lav.lavar())
