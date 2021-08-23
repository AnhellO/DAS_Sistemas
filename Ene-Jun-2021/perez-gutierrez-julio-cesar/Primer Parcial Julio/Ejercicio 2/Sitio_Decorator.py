class PaginaWeb:
    def __init__(self, url, ruta, formato, contenido, titulo, slug, meta_tags):
        self.url = url
        self.ruta = ruta
        self.formato = formato
        self.contenido = contenido
        self.titulo = titulo
        self.slug = slug
        self.meta_tags = meta_tags

#mi componente seria un sitioweb
class SitioWebComponent(PaginaWeb):
    def __init__(self, dominio, categoria, paginas : PaginaWeb):
        self.dominio = dominio
        self.categoria = categoria
        self.paginas= paginas
    def buscar(self):
        pass

#mi componente concreto
class SitioWebConcreteComponent(SitioWebComponent):
    def buscar(self):
        return f' '

class Decorator(SitioWebComponent):
    _sitio: SitioWebComponent
    def __init__(self, _sitio:SitioWebComponent):
        self._sitio=_sitio
    def buscar(self):
        return self._sitio.buscar()

#mi decorador concreto el el que decora la funcion del buscador
class ConcreteDecorator(Decorator):
    def buscar(self):
        for pag in sitio.paginas:
            if pag.url == self.url:
                print("existe")
            else:
                print("no existe")

if __name__ == '__main__':
    lista_paginas=[PaginaWeb('url', 'ruta', 'HTML', '<body>', 'Top movies 2020', 'slug', 'meta'),
                    PaginaWeb('url', 'ruta', 'HTML', '<body>', 'Top music 2020', 'slug', 'meta'),
                    PaginaWeb('url', 'ruta', 'HTML', '<body>', 'Top animes 2020', 'slug', 'meta')]
    sitio=SitioWebConcreteComponent('1','2',lista_paginas)
    ConcreteDecorator.buscar(PaginaWeb('url', 'ruta', 'HTML', '<body>', 'Top movies 2020', 'slug', 'meta'))

