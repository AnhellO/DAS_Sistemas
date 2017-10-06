from Electrodomestico import Electrodomestico

class Television(Electrodomestico):

    def __init__(self, marca, modelo, color, potencia, frecuencia,
    tamano_pantalla):
        super().__init__(marca, modelo, color, potencia, frecuencia)
        self.tamano_pantalla = tamano_pantalla


    def get_tamano_pantalla(self):
        return self.tamano_pantalla

    def set_tamano_pantalla(self, tamano_pantalla):
        self.tamano_pantalla = tamano_pantalla


    def cambiar_canal(self):
        info = "Se ha cambiado el canal en la televisión {} {}.".format(self.marca,
        self.modelo)
        return info



# mi_tv = Television('A', '1', 'Azul',
# '100', '60', '40')
# print(mi_tv.cambiar_canal())
