#clase PaginaWeb
class PaginaWeb(object):
    def __init__(self, **args):
        self.url = args.get('url')
        self.ruta = args.get('ruta')
        self.link = args.get('link')
        self.formato = args.get('formato')
        self.contenido = args.get('contenido')
        self.titulo = args.get('titulo')
        self.metaT = args.get('metaT')
        
#getters y setters 
    def set_url(self, url):
        self.url = url
    def get_url(self):
        return self.url
    def set_ruta(self, ruta):
        self.ruta = ruta
    def get_ruta(self):
        return self.ruta
    def set_link(self, link):
        self.link = link
    def set_formato(self, formato):
        self.formato = formato
    def get_formato(self):
        return self.formato
    def set_contenido(self, contenido):
        self.contenido = contenido
    def get_contenido(self):
        return self.contenido
    def set_titulo(self, titulo):
        self.titulo = titulo
    def get_titulo(self):
        return self.titulo
    def set_metaT(self, metaT):
        self.metaT = metaT
    def get_metaT(self):
        return self.metaT


#funcion __str__
    def __str__(self):
        return "URL: {}\nRuta: {}\nLink: {}\nFormato: {}\nContenido: {}\nTitulo: {}\nmetaT: {}".format(self.url, self.ruta, self.link, self.formato, self.contenido, self.titulo, self.metaT)
    

    
    



