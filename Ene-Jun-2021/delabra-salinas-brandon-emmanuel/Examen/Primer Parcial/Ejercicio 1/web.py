
#Se define la clase WebPage, asignandole sus atrubutos
class PaginaWeb(object):
    def __init__(self,**args):
        self.url = args.get('URL')
        self.carpeta = args.get('CARPETA')        
        self.contenido = args.get("CONTENIDO")
        self.formato = args.get('FORMATO')
        self.titulo = args.get('TITULO')
        self.etiqueta = args.get('ETIQUETA')
        self.metatag = args.get('METATAG')
        
#definimos los atributos en diferentes funciones
    def set_url(self, url):
        self.url = url
    def get_url(self):
        return self.url

    def set_carpeta(self, carpeta):
        self.carpeta = carpeta
    def get_carpeta(self):
        return self.carpeta
  
    def set_contenido(self, contenido):
        self.contenido = contenido
    def get_contenido(self):
        return self.contenido

    def set_formato(self, formato):
        self.formato = formato
    def get_formato(self):
        return self.formato

    def set_titulo(self, titulo):
        self.titulo = titulo
    def get_titulo(self):
        return self.titulo

    def set_etiqueta(self,etiqueta):
        self.etiqueta = etiqueta
    def get_etiqueta(self):
        return self.etiqueta

    def set_metatag(self,metatag):
        self.metatag = metatag
    def get_metatag(self):
        return self.metatag
    
#Tomamos todos los atributos y los unimos mediante un diccionario
    def Diccionario(self):
        guarda = {'url:':self.url, 'carpeta':self.carpeta,'contenido':self.contenido, 'formato':self.formato, 'titulo': self.carpeta,'etiqueta': self.etiqueta,'mettag':self.metatag}
        return guarda

    def __str__(self):
        return f'url:{self.url}\ncarpeta:{self.carpeta}\ncontenido:{self.contenido}\nformato:{self.formato}\ntitulo:{self.titulo}\netiqueta de titulo:{self.etiqueta}\n  metatag:{self.metatag}'

#Definimos la clase SitioWeb
class SitioWeb(object):
    def __init__(self,**args):
        self.dominio = args.get('DOMINIO')
        self.categoria = args.get('CATEGORIA') 
        self.coleccion = []

    def set_dominio(self, dominio):
        self.dominio = dominio
    def get_dominio(self):
        return self.dominio

    def set_categoria(self, categoria):
        self.categoria = categoria
    def get_categoria(self):
        return self.categoria

    def paginas(self, Diccionario: dict):
        self.coleccion.append(Diccionario)

    def datos(self):
        return f'dominio: {self.dominio}\n categoria: {self.categoria}\n paginas:{self.coleccion}'
   
    def __str__(self):
        return f'dominio: {self.dominio}\n categoria: {self.categoria}\n paginas:{self.coleccion}'

def main():
    #Se le da formato a la pagina 
    page = PaginaWeb(URL ='drive.google.com/drive/', CARPETA = 'descargas',CONTENIDO ='Almacenamiento en la nube',FORMATO = 'HTML',TITULO ='Drive', ETIQUETA = 'Mi unidad', METATAG ='Archivos a la nube' )
    #Se le da formato a la pagina que no se encontrara en el sitioweb
    page1 = PaginaWeb(URL ='no localizada', CARPETA = 'descargas', CONTENIDO ='text',FORMATO = 'likm',TITULO ='prueba', ETIQUETA = '45678', METATAG ='Correo electronico')
    web = SitioWeb(DOMINIO='.com', CATEGORIA = 'www')
    #Se incluira la pagina principal al sitioweb
    web.paginas(page.Diccionario())
    web.datos()
    print(page)
    print(web)

#mandas a llamar el metodo main para imprimir
if __name__ == "__main__":
    main()
    