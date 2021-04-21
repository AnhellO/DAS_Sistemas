#Se crea la clase Sitio web con sus respectivos atributos
class SitioWeb:

    def __init__(self, dominio, categoria,  paginas=[]):
        self.dominio = dominio
        self.categoria = categoria
        self.paginas = paginas

#Metodo al cual le crearemos un decorador de manera nativa
    def buscar(self, paginas):
        pass

    def __str__(self):
        return f'DOMINIO -> {self.dominio}\n' \
               f'CATEGORIA -> {self.categoria}\n' \
               f'PAGINAS -> {self.paginas}'


