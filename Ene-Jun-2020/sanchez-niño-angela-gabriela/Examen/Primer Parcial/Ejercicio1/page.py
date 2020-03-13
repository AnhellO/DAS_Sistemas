#se define la clase page con todos sus atributos y metodos
class page (object):
    def __init__(self,**args):
        self.url = args.get('URL')
        self.carpeta = args.get('CARPETA')
        self.contenido = args.get("CONTENIDO")
        self.titulo = args.get('TITULO')
        self.etiqueta = args.get('ETIQUETA')
        self.formato = args.get('FORMATO')
    
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
    def set_titulo(self, titulo):
        self.titulo = titulo
    def get_titulo(self):
        return self.titulo
    def set_etiqueta(self,etiqueta):
        self.etiqueta = etiqueta
    def get_etiqueta(self):
        return self.etiqueta
    def set_formato(self, formato):
        self.formato = formato
    def get_formato(self):
        return self.formato
    
    def almacenar (self):
        guarda = {'url:':self.url, 'carpeta':self.carpeta, 'titulo': self.carpeta,'etiqueta': self.etiqueta, 'formato':self.formato}
        return guarda
    def __str__(self):
        return f'url:{self.url}\nCarpeta:{self.carpeta}\nContenido:{self.contenido}\nTitulo:{self.titulo}\n Etiqueta de titulo:{self.etiqueta}\n Formato:{self.formato}'
#se define la clase website con sus atributos y metodos
class Website(object):
    def __init__(self,**args):
        self.dominio = args.get('DOMINIO')
        self.subdominio = args.get('SUBDOMINIO') 
        self.coleccion = []

    def set_dominio(self, dominio):
        self.dominio = dominio
    def get_dominio(self):
        return self.dominio

    def set_subdominio(self,subdominio):
        self.subdominio = subdominio

    def get_subdominio(self):
        return self.subdominio
    def colecciones(self, almacenar: dict):
        self.coleccion.append(almacenar)
    def datos(self):
        return f'dominio: {self.dominio}\n Subdominio: {self.subdominio}\n Paginas:{self.coleccion}'
   
    def __str__(self):
        return f'dominio: {self.dominio}\n Subdominio: {self.subdominio}\n Paginas:{self.coleccion}'



def main():
    #Se le da formato a la pagina que estara dentro de nuestro website
   pagina = page(URL ='htijsjkjdf', CARPETA = 'descragads',CONTENIDO ='text',TITULO ='habia una vez', ETIQUETA = '123456', FORMATO = 'HTML' )
   #Se le da formato a la pagina que no se encontrara en el website
   pagina1 = page(URL ='no localizada', CARPETA = 'descragads',CONTENIDO ='text',TITULO ='prueba', ETIQUETA = '45678', FORMATO = 'likm' )
   web = Website (DOMINIO='123456', SUBDOMINIO = '456789')
   #Se incluira la pagina principal al website
   web.colecciones(pagina.almacenar())
   web.datos()
   print(pagina)
   print(web)


#se lleva a cabo las compraciones para poder definir si esta o no la pagina en nuestro website
def buscador(web:Website , pagina:page):
    if pagina.colecciones() in web.contenido():
        print('La pagina SI existe')
        print (web)
    else:
        print (' La pagina NO existe ')
    

#mandas a llamar el metodo main para imprimir
if __name__ == "__main__":
    main()
    












