

class PaginaWeb():

    # Constructor
    def __init__(self, url, ruta, formato,
                 contenido, titulo, slug, metatags: list):

        self.url = url
        self.ruta = ruta
        self.formato = formato
        self.contenido = contenido
        self.titulo = titulo
        self.slug = slug
        self.metatags = metatags

        
    # Representacion de tipo "string" de la clase "PaginaWeb"
    def __str__(self):

        return f"""URL: {self.url}\nRUTA: {self.ruta}\nFORMATO: {self.formato}\nCONTENIDO: {self.contenido}\nTITULO: {self.titulo}\nSLUG: {self.slug}\nMETA-TAGS: {self.metatags}"""


class SitioWeb():

    def __init__(self, dominio, categoria, paginas: PaginaWeb):

        self.dominio = dominio
        self.categoria = categoria
        self.paginas = paginas

    # Representacion de tipo "string" de la clase "SitioWeb"
    def __str__(self):

        return f"""\nDOMINIO: {self.dominio}\nCATEGORIA: {self.categoria}\nPAGINAS: {self.paginas}"""

def main():

    # Declaramos una variable de tipo "PaginaWeb" para
    # añadirle datos a los atributos de la clase de la pagina web.
    pag1 = PaginaWeb(url="www.georgeUadec.com", ruta="/index",
                     formato="HTML", contenido="<body> ¡¡This is Sparta!! </body> ",
                     titulo="<title> Live long and Prosper </title>", slug="Live-long-and-Prosper",
                     metatags=["<meta name="">", "<meta http-equiv="">", "<meta content="" ", "<meta charset=UTF-8>"])

    # Declaramos otra variable de tipo "PaginaWeb" que iran dentro de nuestro sitio web
    pag2 = PaginaWeb(url="www.georgeUadec/profile.com", ruta="/index/profile",
                     formato="HTML", contenido="<header> ¡¡DAS_Sistemas!! </header> ",
                     titulo="<title> Mi Perfil </title>", slug="Mi-Perfil",
                     metatags=["<meta name="">", "<meta content="" "])

    # Añadimos una variable de tipo "SitioWeb"
    # A de mas de darle formato a los atributos del objeto, tambien
    # Añadimos las paginas que corresponden al sitio web
    sitio1 = SitioWeb(dominio="georgeUadec.com", categoria="Blog",
                      paginas=[str(pag1), str(pag2)])

    # Imprimimos para ver la informacion del sitio web y la pagina
    #print(pag1)
    #print(sitio1)    
    

if __name__ == "__main__":
    # Funcion main que contiene nuestros objetos de clase
    main()
