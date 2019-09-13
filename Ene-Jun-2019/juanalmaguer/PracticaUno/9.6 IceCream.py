class Restaurante(object):
    def __init__(self, nombre, tipo):
        self.nombre = nombre
        self.tipo = tipo

    def description(self):
        print("The name's restaurant is " + self.nombre.title() + " and its type is " + self.tipo.title())

    def open(self):
        print(self.nombre.title() + " is open")

class IceCreamStand(Restaurant):
    def __init__(self, name,tyoe):
        super(IceCreamStand, self).__init__(name,type)
        self.flavors = []

    def get_flavors(self, *lista_sabores):
        self.sabores = lista_sabores

    def print_flavors(self):
        print("There are the flavors")
        for sab in self.sabores:
            print("- " + sab)

ics = IceCreamStand('Helados Sultana', 'IceCream')
print(ics.get_flavors())
ics.get_flavors('Vainilla','Coconut')
print(ics.print_flavors())