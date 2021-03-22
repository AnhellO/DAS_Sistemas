class paginaWeb(object):
    def __init__(self, url: str, ruta: str, formato:str, contenido:str, titulo: str, slug:str, metatags:list):
        self.url = url
        self.ruta = ruta
        self.formato = formato
        self.contenido = contenido
        self.titulo = titulo
        self.slug = slug
        self.metatags=metatags

    def seturl(self,url):
        self.url = url.lower()
    def geturl(self):
        return self.url

    def setruta(self,ruta):
        self.ruta = ruta
    def getruta(self):
        return self.ruta

    def setformato(self,formato):
        self.formato = formato
    def getformato(self):
        return self.formato

    def setcontenido(self,contenido):
        self.contenido = contenido
    def getcontenido(self):
        return self.contenido

    def settitulo(self,titulo):
        self.titulo = titulo
    def gettitulo(self):
        return self.titulo

    def setslug(self):
        self.slug = ((self.titulo).lower()).replace(" ","-")
    def getslug(self):
        return self.slug

    def setmetatags(self,metatags:list):
        self.metatags.append(metatags)
    def getmetatags(self):
        r = ", ".join(self.metatags)
        return r

    def __str__(self):
        mettags = ",".join(self.metatags)
        r=f"url: {self.url}"
        r+=f"\nruta: {self.ruta}"
        r+=f"\nformato: {self.formato}"
        r+=f"\ncontenido: {self.contenido}"
        r+=f"\ntitulo: {self.titulo}"
        r+=f"\nslug: {self.slug}"
        r+=f"\nmeta-tags: {mettags}"
        return r

class SitioWeb(paginaWeb):
    def __init__(self, dominio:str, categoria: str, paginas: list):
        self.dominio=dominio
        self.categoria=categoria
        self.paginas=paginas

    def add_pagina(self, pagina):
        self.paginas.append(pagina)

    def del_pagina(self,pagina):
        try:
            self.paginas.remove()
        except:
            return f"{pagina} se ha eliminado completamente"
        return f"{pagina} no ha podido ser eliminado\n inexistente?"

    def get_dominio(self):
        return self.dominio
    def get_categoria(self):
        return self.categoria
    def get_paginas(self):
        r=""
        for i in self.paginas:
            r+="\n"
            r+=f"{i}"
            r+="#########"
        return r

    def buscador(self,obj):
        for i in self.paginas:
            if obj == i:
                return "Existe."
        return "no se ha encontrado"

    def __str__(self):
        r=f"dominio: {self.dominio}"
        r+=f"\ncategoria: {self.categoria}"
        r+="\npaginas:\n"
        for i in self.paginas:
            r+="############\n"
            r+=f"{i}"
            r+="\n"
        return r 