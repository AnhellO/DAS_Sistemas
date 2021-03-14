#clase Paginaweb con sus atributos y la funcion __str__
class PaginaWeb:
    def __init__(self, url, ruta, formato, contenido, titulo, slug, meta_tags):
        self.url = url
        self.ruta = ruta
        self.formato = formato
        self.contenido = contenido
        self.titulo = titulo
        self.slug = slug
        self.meta_tags = meta_tags
    def __str__(self):
        return f'{self.url}\n{self.ruta}\n{self.formato}\n{self.contenido}\n{self.titulo}\n{self.slug}\n{self.meta_tags}'

#pagina sitio que hereda de la clase paginaweb
class SitioWeb(PaginaWeb):
    def __init__(self, dominio, categoria, paginas : PaginaWeb):
        self.dominio = dominio
        self.categoria = categoria
        self.paginas= paginas
    def __str__(self):
        return f'{self.dominio}\n{self.categoria}\n{self.paginas}'

#coleccion de objetos de la clase pagina web 
# para luego pasarle esa coleccion a un objeto de sitio web
lista_paginas=[PaginaWeb('url', 'ruta', 'HTML', '<body>', 'Top movies 2020', 'slug', 'meta'),
PaginaWeb('url', 'ruta', 'HTML', '<body>', 'Top music 2020', 'slug', 'meta'),
PaginaWeb('url', 'ruta', 'HTML', '<body>', 'Top animes 2020', 'slug', 'meta')]
sitio=SitioWeb('1','2',lista_paginas)
print(sitio.paginas)

