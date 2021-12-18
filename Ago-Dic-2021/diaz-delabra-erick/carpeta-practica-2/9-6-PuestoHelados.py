class Heladeria():
    def __init__(self, nombre, tipo):
        self.nombre = nombre.title()
        self.tipo = tipo
        self.numero_servido = 0

    def descripcion(self):
        print("\nLa mejor heladeria es: " + self.nombre)

    def abierto(self):
        print("\n" + self.nombre + " ya abrió!")

    def numero(self, numero_servido):
        self.numero_servido = numero_servido

    def incrementar(self, x):
        self.numero_servido += x

class Heladeria2(Heladeria):
    def __init__(self, nombre, tipo='helado'):
        super().__init__(nombre, tipo)
        self.sabor = []

    def saboress(self):
        print("\nTenemos los siguientes sabores:")
        for sabor in self.sabor:
            print(sabor.title())

n1 = Heladeria2('Helados Erick')
n1.sabor = ['chocolate', 'fresa', 'vainilla', 'platano', 'cereza']
n1.descripcion()
n1.saboress()