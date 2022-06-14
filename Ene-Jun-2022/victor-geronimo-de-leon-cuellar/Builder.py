from abc import ABC, abstractmethod

class PaginaBuilder(ABC):

    def reset(self):
        pass

    def Crear_pagina(self):
        pass

class Pagina:
    def __init__(self):
        self.Titulo = False
        self.Color = False
        self.Nombre = False
        self.crear = []
        

    def __str__(self):
        string = ""
        if self.Titulo:
            string += "Diseño y Arqitectura de Software "
        if self.Color:
            string += "Amarillo "
        if self.Nombre:
            string += "Pagina web "

        return string

class TituloDesc:
    def __str__(self):
        return "Encabezado"

class ColorDesc:
    def __str__(self):
        return "Diseño"

class NombreDesc:
    def __str__(self):
        return "Nombre descriptivo"

class PAgBuilder(PaginaBuilder):
    def __init__(self):
        self.product = Pagina()

    def reset(self):
        self.product = Pagina()

    def get_product(self):
        return self.product

    def crear_pagina(self):
        self.product.__Titulo = True
        self.product.crear.append(TituloDesc())
        self.product.crear.append(ColorDesc())
        self.product.crear.append(NombreDesc())

class AutPagBuilder(PaginaBuilder):
    def __init__(self):
        self.product = Pagina()

    def reset(self):
        self.product = Pagina()

    def get_product(self):
        return self.product


class Director:
    def make_pagina(self, builder):
        builder.crear_pagina()
        return builder.get_product()

    def make_auts_pagina(self, builder):
        builder.crear_pagina()
        return builder.get_product()

director = Director()
builder = PAgBuilder()
print(director.make_pagina(builder))




