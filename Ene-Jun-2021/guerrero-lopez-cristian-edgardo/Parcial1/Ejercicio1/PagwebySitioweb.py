class Page(object):
    def __init__(self, URL: str, RUTA: str, FORMATO:str, CONTENIDO:str, TITULO: str, SLUG:str, METATAGS:list):
        self.URL = URL
        self.RUTA = RUTA
        self.FORMATO=FORMATO
        self.CONTENIDO = CONTENIDO
        self.TITULO = TITULO
        self.SLUG= SLUG
        self.METATAGS=METATAGS
        'Cree unos objetos en la clase ya que el parametro self se refiere al objeto instanciado de esta clase sobre el cual se esta invocando dicho metodo'
    

    
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
    
    def __str__(self):
        r=f"DOMINIO: {self.DOMINIO}"
        r+=f"\nCATEGORIA: {self.CATEGORIA}"
        r+="\nPAGINAS:\n"
        for i in self.PAGINAS:
            r+="############\n"
            r+=f"{i}"
            r+="\n"
        return r
