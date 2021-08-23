from Ejercicio_PaginaWeb import PaginaWeb

class SitioWeb:

    #Metodo constructor
    def __init__(self, dominio, categoria, paginas: list(PaginaWeb())):
        self.dominio = dominio
        self.categoria = categoria
        self.paginas = paginas


    #__str__ de la clase que regresa el dominio, categoria, y la lista de paginas
    def __str__(self):
        return 'Dominio: {}\n Categoria: {}\n Paginas: {}\n '.format(self.dominio, self.categoria, *self.paginas)
