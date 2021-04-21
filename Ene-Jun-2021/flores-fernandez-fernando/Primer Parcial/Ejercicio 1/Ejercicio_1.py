
#creamos la clase PaginaWeb contiene los datos de un documento web
class PaginaWeb(object):
    def __init__(self,url: str, ruta: str, formato: str,contenido: str,titulo: str,slug: str,metatags: list):
        self._url = url
        self._ruta = ruta
        self._formato = formato
        self._contenido = contenido
        self._titulo = titulo
        self._slug = slug
        self._metatags = metatags
#modificamos __str__ para regresar de una manera mas estilizada el llamado de los atributos        
    def __str__(self):
        return f"El url de la pagina es: {self._url}\nLa ruta del archivo es:{self._ruta}\nEl formato del archivo es: {self._formato}\nEl contenido de la pagina es: {self._contenido}\nEl titulo de la pagina es: {self._titulo}\nEl slug de la pagina es: {self._slug}\nLos meta-tags de la pagina son: {self._metatags}"
#creamos la clase SitioWeb que va a contener PaginaWeb    
class SitioWeb(object):
    def __init__(self, dominio: str,categoria: str, paginas: list):
        self._dominio = dominio
        self._categoria = categoria
        self._paginas = paginas 
    
#modificamos la funcion __str__ para regresar los atributos    
    def __str__(self):
        return f"El dominio del sitio es: {self._dominio}\nLa categoria del sitio es: {self._categoria}\nLas paginas del sitio son:\n{self._paginas}"

#llamamos a las clases y creamos objetos
def main():
    pagina = PaginaWeb("https://www.youtube.com/watch?v=dQw4w9WgXcQ",
                       "C://User/practica",
                       "HTML",
                       "<body> <p> hola soy una practica </p></body>",
                       "<h1>Practica 1</h1>",
                       "practica-1",
                       ["tags",
                        "tags"])  
    
    sitio = SitioWeb("www.youtube.com",
                     "Entretenimiento",
                     pagina)
    
    print(sitio)
    
    
if __name__ == '__main__':
    main()        