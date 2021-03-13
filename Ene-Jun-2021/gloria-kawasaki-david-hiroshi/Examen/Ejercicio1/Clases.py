class Page(object):
    def __init__(self, URL: str, RUTA: str, FORMATO:str, CONTENIDO:str, TITULO: str, SLUG:str, METATAGS:list):
        self.URL = URL
        self.RUTA = RUTA
        self.FORMATO=FORMATO
        self.CONTENIDO = CONTENIDO
        self.TITULO = TITULO
        self.SLUG= SLUG
        self.METATAGS=METATAGS

    def set_URL(self,URL):
        self.URL = URL
    def set_RUTA(self,RUTA):
        self.RUTA = RUTA
    def set_FORMATO(self,FORMATO):
        self.FORMATO = FORMATO
    def set_CONTENIDO(self,CONTENIDO):
        self.CONTENIDO = CONTENIDO
    def set_TITULO(self,TITULO):
        self.TITULO = TITULO
    def set_SLUG(self):
        self.SLUG = ((self.TITULO).lower()).replace(" ","-")
    def set_typo(self,METATAGS:list):
        self.METATAGS.append(METATAGS)
    
    def get_URL(self):
        return self.URL
    def get_RUTA(self):
        return self.RUTA
    def get_FORMATO(self):
        return self.FORMATO
    def get_CONTENIDO(self):
        return self.CONTENIDO
    def get_TITULO(self):
        return self.TITULO
    def get_SLUG(self):
        return self.SLUG
    def get_METATAGS(self):
        r = ", ".join(self.METATAGS)
        return r
    
    def __str__(self):
        mettags = ",".join(self.METATAGS)
        r=f"URL: {self.URL}"
        r+=f"\nRUTA: {self.RUTA}"
        r+=f"\nFORMATO: {self.FORMATO}"
        r+=f"\nCONTENIDO: {self.CONTENIDO}"
        r+=f"\nTITULO: {self.TITULO}"
        r+=f"\nSLUG: {self.SLUG}"
        r+=f"\nMETA-TAGS: {mettags}"
        return r

class Website(Page):
    def __init__(self, DOMINIO:str, CATEGORIA: str, PAGINAS: list):
        self.DOMINIO=DOMINIO
        self.CATEGORIA=CATEGORIA
        self.PAGINAS=PAGINAS
    
    def add_PAGINA(self, PAGINA):
        self.PAGINAS.append(PAGINA)
    
    def del_PAGINA(self,PAGINA):
        try:
            self.PAGINAS.remove()
        except:
            return f"{PAGINA} ha sido eliminado"
        return f"{PAGINA} no ha podido ser eliminado\n inexistente?"

    def get_DOMINIO(self):
        return self.DOMINIO
    def get_CATEGORIA(self):
        return self.CATEGORIA
    def get_PAGINAS(self):
        r=""
        for i in self.PAGINAS:
            r+="\n"
            r+=f"{i}"
            r+="#########"
        return r
    def __str__(self):
        r=f"DOMINIO: {self.DOMINIO}"
        r+=f"\nCATEGORIA: {self.CATEGORIA}"
        r+="\nPAGINAS:\n"
        for i in self.PAGINAS:
            r+="############\n"
            r+=f"{i}"
            r+="\n"
        return r