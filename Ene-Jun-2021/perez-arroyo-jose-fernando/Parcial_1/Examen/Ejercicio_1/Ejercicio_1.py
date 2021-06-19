class PaginaWeb(object):
    def __init__(self, url, contenido, ruta, titulo, desc, formato, slug):
        self.url = url
        self.contenido = contenido
        self.ruta = ruta
        self.titulo = titulo
        self.desc = desc
        self.formato = formato
        self.slug = slug

    def set_url(self, url):
        self.url=url
    def get_url(self):
        return self.url
    def set_slug(self, slug):
        self.slug=slug
    def get_slug(self):
        return self.slug
    def set_folder(self, contenido):
        self.contenido = contenido
    def get_folder(self):
        return self.contenido
    def set_link(self, ruta):
        self.ruta = ruta
    def get_link(self):
        return self.ruta
    def set_titulo(self, titulo):
        self.titulo = titulo
    def get_titulo(self):
        return self.titulo
    def set_desc(self, desc):
        self.desc = desc
    def get_desc(self):
        return self.desc
    def set_formato(self, formato):
        self.formato = formato
    def get_formato(self):
        return self.formato
    
    def __str__(self):
        return f'URL: {self.url}\nFolder: {self.contenido}\nLink: {self.ruta}\nTitulo: {self.titulo}\nDescripción: {self.desc}\nFormato: {self.formato}'


class Website(PaginaWeb):
    def __init__(self, dominio, subdom, paginas: list):
        self.dominio = dominio
        self.subdom = subdom
        self.paginas = paginas
    
    def set_dominio(self, dominio):
        self.dominio = dominio
    def get_dominio(self):
        return self.dominio
    def set_subdom(self, subdom):
        self.subdom = subdom
    def get_subdom(self):
        return self.subdom
 
    def add_paginas(self, Page):
        self.paginas.append(Page)
    def get_paginas(self):
        return self.paginas
    
    def search(self, pagina=''):
        if pagina in self.paginas:
            print('<---------- Pagina Encontrada! ---------->')
            print(pagina)
        else:
            print('<---------- Pagina no Encontrada! ---------->')


            