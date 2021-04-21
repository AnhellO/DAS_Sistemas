class PaginaWeb(object):
    def __init__(self, url: str, path: str, formato:str, conten:str, title: str, slug:str, mtags:list):
        self.url = url
        self.path = path
        self.formato=formato
        self.conten = conten
        self.title = title
        self.slug = slug
        self.mtags=mtags

    
    def __str__(self):
        mettags = ",".join(self.mtags)
        
        r=f"url: {self.url}"
        r+=f"\npath: {self.path}"
        r+=f"\nformato: {self.formato}"
        r+=f"\nconten: {self.conten}"
        r+=f"\ntitle: {self.title}"
        r+=f"\nslug: {self.slug}"
        r+=f"\nmeta-tags: {mettags}"
        return r

class Website(PaginaWeb):
    def __init__(self, dom:str, cat: str, pags: list):
        self.dom=dom
        self.cat=cat
        self.pags=pags
    
    def add_PAGINA(self, pag):
        self.pags.append(pag)
    
    def __str__(self):
        r=f"dominio: {self.dom}"
        r+=f"\ncategoria: {self.cat}"
        r+="\nPAGINAS:\n"
        for i in self.pags:
            r+="--------------------\n"
            r+=f"{i}"
            r+="\n"
        return r
        
    def buscador(self,obj):
        for i in self.pags:
            if obj == i:
                return "EXISTENTE!"
        return "NO SE ENCONTRO...."
