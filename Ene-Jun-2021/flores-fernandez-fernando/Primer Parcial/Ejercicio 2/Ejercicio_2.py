import abc
#inteface Component creamos la funcion buscador que es la que buscara alguna PaginaWeb en el SitioWeb
class ISitioWebComponent(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def buscador(self):
        pass
    
# Concrete Component
class SitioWebConcreteComponent(ISitioWebComponent):
    def __init__(self, dominio: str,categoria: str, paginas: list):
        self._dominio = dominio
        self._categoria = categoria
        self._paginas = paginas 
    
    
    def __str__(self):
        return f"""
                El dominio del sitio es: {self._dominio}
                La categoria del sitio es: {self._categoria}
                Las paginas del sitio son: {self._paginas}
                """
                
    def buscador(self):
        return f"Pagina no buscada"    

# Base Decorator    
class SitioWebDecorator(ISitioWebComponent, metaclass=abc.ABCMeta):
    def __init__(self,sitio_web: ISitioWebComponent):
        self._sitio_web = sitio_web
        
        @abc.abstractmethod
        def buscador(self):
            pass  
    
# Concrete Decorator: A
class BuscadorConcreteDecorator(SitioWebDecorator):
    # La logica del buscador es recibir un objeto de la clase PaginaWeb luego utiliza la url que es unica de cada pagina 
    # llama a la url de la pagina pedida por atributo y la compara con la url de las paginas que estan dentro del SitioWeb
    # si encuentra que la url de la pagina es igual a la url de las paginas en el sitio regresa un string con los datos de
    # la pagina junto con un mensaje diciendo que existe y si no encuentra la pagina regresa un mensaje de error  
    def buscador(self,pagina : object):
        i = 0
        for pag in self._sitio_web._paginas:
            if(pagina._url == self._sitio_web._paginas[i]._url):
                return f"La pagina: {self._sitio_web._paginas[i]}\nsi Existe"
            i = i+1
        return f"ERROR-HTTP 404 page Not found"
    
#clase PaginaWeb la misma del Ejercicio_1
class PaginaWeb(object):
    def __init__(self,url: str, ruta: str, formato: str,contenido: str,titulo: str,slug: str,metatags: list):
        self._url = url
        self._ruta = ruta
        self._formato = formato
        self._contenido = contenido
        self._titulo = titulo
        self._slug = slug
        self._metatags = metatags
        
    def __str__(self):
        return f"""
                El url de la pagina es: {self._url}
                La ruta del archivo es:{self._ruta}
                El formato del archivo es: {self._formato}
                El contenido de la pagina es: {self._contenido}
                El titulo de la pagina es: {self._titulo}
                El slug de la pagina es: {self._slug}
                Los meta-tags de la pagina son: {self._metatags}
                """

def main():
    #llenamos los objetos de PaginaWeb y SitioWeb
    pagina1 = PaginaWeb("https://www.youtube.com/watch?v=dQw4w9WgXcQ",
                       "C://User/youtube/user",
                       "HTML",
                       "<body> <p> hola soy una pagina de youtube 1 </p></body>",
                       "<h1>Youtube 1</h1>",
                       "youtube-1",
                       ['<meta name = "description" content = "this is the description">',
                        '<meta http-equiv = "refresh" content = "100"'])  
    
    pagina2 = PaginaWeb("https://www.youtube.com/watch?v=r1lEc1w92RE",
                       "C://User/youtube/user",
                       "HTML",
                       "<body> <p> hola soy una pagina de youtube 2 </p></body>",
                       "<h1>Youtube 2</h1>",
                       "youtube-2",
                       ['<meta name = "description" content = "this is the description">',
                        '<meta http-equiv = "refresh" content = "100"'])  
    
    pagina3 = PaginaWeb("https://www.youtube.com/watch?v=8OJf0-r7sZ0",
                       "C://User/youtube/user",
                       "HTML",
                       "<body> <p> hola soy una pagina de youtube 3 </p></body>",
                       "<h1>Youtube 3</h1>",
                       "youtube-3",
                       ['<meta name = "description" content = "this is the description">',
                        '<meta http-equiv = "refresh" content = "100"'])  
    sitio = SitioWebConcreteComponent("www.youtube.com","Entretenimiento",[pagina1,pagina2])
    #Creamos un objeto del decorador y le mandamos nuestro SitioWeb
    buscar = BuscadorConcreteDecorator(sitio)
    #Luego llamamos a la funcion buscador junto con una pagina e introducimos el return de Buscador 
    # a una variable y la imprimimos
    resultado = buscar.buscador(pagina2)
    print(resultado)
    
if __name__ == '__main__':
    main()        