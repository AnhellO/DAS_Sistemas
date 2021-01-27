"""Ejercicio 1
Crea una clase Page que represente a una página dentro de un sitio web. La clase deberá de contener múltiples atributos
que pertenezcan a una página web, por ejemplo url, folder o path, links o hipervínculos, contenido de texto,
título (<h1>), etiqueta de título (<title>), meta-descripción, formato (HTML, XML, JSON, etc), etcétera
(Recurso: https://es.wikipedia.org/wiki/P%C3%A1gina_web)

Crea una 2da clase Website que represente a un sitio web como un todo/conjunto.
La clase deberá de contener múltiples atributos que describan a un sitio web, por ejemplo dominio, subdominio, páginas
que forman parte del sitio, entre otros (Recurso: https://mx.godaddy.com/blog/que-es-un-sitio-web/)
La clase Website deberá tener un atributo que contenga a la colección de páginas de forman parte del sitio.
Los objetos de esta colección deberán de ser de tipo Page.

Implementa una función buscador, que reciba dos parámetros, uno de tipo Website, y el otro de tipo Page.
La función deberá de llevar a cabo una búsqueda dentro del conjunto de páginas del sitio para determinar si es que
la página existe.
"""


class Page(object):

    def __init__(self, **args):
        self.url = args.get('url')
        self.path = args.get('path')
        self.link = args.get('link')
        self.titulo = args.get('titulo')
        self.descripcion = args.get('descripcion')
        self.formato = args.get('formato')

    # ---------------------------------------------------------------
    def set_url(self, url):
        self.url = url

    def get_url(self):
        return self.url

    # --------------------------
    def set_path(self, path):
        self.path = path

    def get_path(self):
        return self.path

    # --------------------------
    def set_link(self, link):
        self.link = link

    def get_link(self):
        return self.link

    # --------------------------
    def set_titulo(self, titulo):
        self.titulo = titulo

    def get_titulo(self):
        return self.titulo

    # --------------------------
    def set_descripcion(self, descripcion):
        self.descripcion = descripcion

    def get_descripcion(self):
        return self.descripcion

    # --------------------------
    def set_formato(self, formato):
        self.formato = formato

    def get_formato(self):
        return self.formato

    def __str__(self):
        return f'URL: {self.url}\nPath: {self.path} \nLink: {self.link}\nTítulo: {self.titulo}\nDescripción: {self.descripcion}\nFormato: {self.formato}'


# E J E M P L O


"""pagina1 = Page(url='https://es.wikipedia.org/wiki/Wikipedia:Portada', path='Ayuda',
               link='https://es.wikipedia.org/wiki/Ayuda:Contenidos', titulo='Ayuda:Contenidos',
               descripcion='Introducción, Cómo colaborar, Políticas, etc.', formato='html')

print(pagina1)
"""

# -*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-


class Website(Page):

    def __init__(self, dominio, subdominio, coleccion: list):
        self.dominio = dominio
        self.subdominio = subdominio
        self.coleccion = coleccion
# ---------------------------------------------------------------

    def set_dominio(self, dominio):
        self.dominio = dominio

    def get_dominio(self):
        return self.dominio
# ------------------------------------

    def set_subdominio(self, subdominio):
        self.subdominio = subdominio

    def get_subdominio(self):
        return self.subdominio
# ------------------------------------

    def agrega_coleccion(self, Page):
        self.coleccion.append(Page)

    def get_coleccion(self):
        return self.coleccion


# -*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-


    def buscador(self, pagina=''):
        if pagina in self.coleccion:
            print('SI Existe la página\n')
            print(pagina)
        else:
            print('NO Existe la página\n')


pagina1 = Page(url='https://es.wikipedia.org/wiki/Wikipedia:Portada', path='Ayuda',
                link='https://es.wikipedia.org/wiki/Ayuda:Contenidos', titulo='Ayuda:Contenidos',
                descripcion='Introducción, Cómo colaborar, Políticas, etc.', formato='html\n')

pagina2 = Page(url='https://sourcemaking.com/', path='Antipatterns',
                link='https://sourcemaking.com/antipatterns', titulo='AntiPatterns - What is an Antipattern?',
                descripcion='Información sobre antipatrones', formato='html\n')

dominio = '.org'
subdominio = 'es'
coleccion = [pagina1, pagina2]
sw = Website(dominio, subdominio, coleccion)

#Prueba del buscador
print('Veamos si la página que buscas se encuentra...\n')
sw.buscador(pagina1)
