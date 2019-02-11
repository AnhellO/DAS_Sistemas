class Restaurante(object):
    def __init__(self, nombre, tipo):
        self.nombre = nombre
        self.tipo = tipo

    def descripcion(self):
        print("El Restaurante se Llama " + self.nombre.title() + " Es de Tipo " + self.tipo.title())

    def abierto(self):
        print(self.nombre.title() + " Esta Abierto")

class IceCreamStand(Restaurante):
    def __init__(self, nombre, tipo):
        super(IceCreamStand, self).__init__(nombre, tipo)
        self.sabores = []

    def obtener_sabores(self, *lista_sabores):
        self.sabores = lista_sabores

    def imprime_sabores(self):
        print("Los Sabores de Helados son: ")
        for sab in self.sabores:
            print("- " + sab)

ics = IceCreamStand('Dairy Queen', 'Helados')
print(ics.descripcion())
ics.obtener_sabores('Chocolate','Vainilla','Oreo','Fresa')
print(ics.imprime_sabores())