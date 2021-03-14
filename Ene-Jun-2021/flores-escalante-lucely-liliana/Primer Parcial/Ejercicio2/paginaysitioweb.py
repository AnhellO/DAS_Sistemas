class PaginaWeb(object):
    def __init__(self, url: str, ruta: str, formato:str, contenido:str, titulo: str, slug:str, metatags:list):

        self.contenido=contenido

        self.ruta=ruta

        self.url=url
        
        self.titulo=titulo
        
        self.slug=slug
        
        self.metatags=metatags
        
        self.formato=formato

    
    def __str__(self):
        
        mettags=",".join(self.metatags)

        r=f"url: {self.url}"
        
        r+=f"\nruta: {self.ruta}"
        
        r+=f"\nformato: {self.formato}"
        
        r+=f"\ncontenido: {self.contenido}"
        
        r+=f"\ntitulo: {self.titulo}"
        
        r+=f"\nslug: {self.slug}"
        
        r+=f"\nmeta-tags: {mettags}"
        
        return r

class SitioWeb(PaginaWeb):
    def __init__(self, dominio:str, categoria: str, paginas: list):

        self.paginas=paginas

        self.categoria=categoria
        
        self.dominio=dominio
    
    def agregar_pagina(self, pagina):
        
        self.paginas.append(pagina)
    
    def __str__(self):
        
        r=f"dominio: {self.dominio}"
        
        r+=f"\ncategoria: {self.categoria}"
        
        r+="\npaginas:\n"
        
        for i in self.paginas:
            r+="\n"
            
            r+=f"{i}"
            
            r+="\n"
        
        return r

    def buscador(self,obj):
        for i in self.pags:
            if obj == i:
                return "Existe."
        return "Aquí no esta."
