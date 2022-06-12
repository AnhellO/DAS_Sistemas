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
    def __init__(self, dominio, categoria, accesibilidad, privacidad, publicidad, distribucion, interactividad, modernidad, buscador_avanzado, paginas : PaginaWeb):
        self.dominio = dominio
        self.categoria = categoria
        self.accesibilidad = accesibilidad
        self.paginas = paginas
        self.privacida = privacidad
        self.publicidad = publicidad
        self.distribucion = distribucion 
        self.interactividad = interactividad
        self.modernidad = modernidad
        self.buscador_avanzado = buscador_avanzado
    def __str__(self):
        return f'{self.dominio}\n{self.categoria}\n{self.accesibilidad}\n{self.paginas}\n{self.privacidad}\n{self.publicidad}\n{self.distribucion}\n{self.interactividad}\n{self.modernidad}\n{self.buscador_avanzado}'


def buscador(sitioweb, pagina):
    if pagina in sitioweb:
        print("existe la pagina")
    else:
        print("no existe")



lista_paginas = []
pag1 = PaginaWeb('url', 'ruta', 'HTML', '<body>', 'Top music 2020', 'slug', 'meta')
pag2 = PaginaWeb('url', 'ruta', 'HTML', '<body>', 'Top music 2021', 'slug', 'meta')
pag3 = PaginaWeb('url', 'ruta', 'HTML', '<body>', 'Top music 2022', 'slug', 'meta')

#coleccion de objetos de la clase pagina web 
lista_paginas.append(pag1)
lista_paginas.append(pag2)
lista_paginas.append(pag3)
#print(lista_paginas)
