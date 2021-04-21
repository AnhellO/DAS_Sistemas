#Goncho

import abc
# Componente
class SitioWebComponent(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def buscador(self):
        pass
    
# Concrete Component
class sitiowebConcreteComponent(SitioWebComponent):
    def __init__(self, dominio,categoria, paginas):
        self.dominio = dominio
        self.categoria = categoria
        self.paginas = paginas 

    def __str__(self):
        return f""" 
                    EL DOMINIO: {self.dominio}\n 
                    LA CATEGORIA: {self.categoria}\n
                    LAS PAGINAS: {self.paginas}\n
                """
    def buscador(self):
        return f"ERROR-HTTP 404 page Not found" 
    
# Decorator
class SitioWebBaseDecorator(SitioWebComponent, metaclass=abc.ABCMeta):
    def __init__(self, SitioWeb: SitioWebComponent):
        self.SitioWeb = SitioWeb

    @abc.abstractmethod
    def buscador(self):
        pass

# Concrete Decorator A Buscador
class BuscadorConcreteDecorator(SitioWebBaseDecorator):
    def buscador(self,pagina : object):
        n = 0
        for pagina in self.SitioWeb.paginas:
            if(pagina.url == self.SitioWeb.paginas[n].url):
                return f"Esta pagina: {self.SitioWeb.paginas[n]}\nsi Existe"
            n = n+1
        return f"ERROR - HTTP 404 PAGE NOT FOUND"


class PaginaWeb(object):
    def __init__(self,url, ruta, formato,contenido, titulo,slug,meta_tag):
        self.url = url
        self.ruta = ruta
        self.formato = formato
        self.contenido = contenido
        self.titulo = titulo
        self.slug = slug
        self.meta_tag = meta_tag

    def __str__(self):
        return f""" 
                    LA PAGINA WEB: {self.url}\n 
                    LA RUTA: {self.ruta}\n
                    EL FORMATO: {self.formato}\n
                    EL CONTENIDO: {self.contenido}\n
                    EL TITULO: {self.titulo}\n
                    SLUG: {self.slug}\n
                    META-TAG: {self.meta_tag} 
                """
def main():
    pagina1 = PaginaWeb(    url = "https://www.callofduty.com/warzone",
                            ruta = "/root",
                            formato = "HTML",
                            contenido = "<body> <p>¡Warzone Season 2 ya está disponible con nuevas armas, operadores y más!. </p> </body>",
                            titulo = "<title>Call of Duty®: Warzone |  Mejor juego gratuito de Battle Royale</title>",
                            slug = "Call-of Duty®:-Warzone-|-Mejor-juego-gratuito-de-Battle-Royale",
                            meta_tag =["< meta name=description"">","<meta property=og:title"">","<meta http-equiv=content-type content=text/html; charset=UTF-8"">"]
                        )
    pagina2 = PaginaWeb(    url = "https://www.callofduty.com/coldwar",
                            ruta = "/root",
                            formato = "HTML",
                            contenido = "<body> <p>¡Cold War Season 2 ya está disponible. </p> </body>",
                            titulo = "<title> Call of Duty®: Cold War</title>",
                            slug = "Call-of Duty®:-Cold-War",
                            meta_tag =["< meta name=description"">","<meta property=og:title"">","<meta http-equiv=content-type content=text/html; charset=UTF-8"">"]
                        )
    sitio = sitiowebConcreteComponent("www.callofduty.com","Juegos",[pagina2,pagina1])
    buscar = BuscadorConcreteDecorator(sitio)
    Res = buscar.buscador(pagina2)
    print(Res)

if __name__ == "__main__":
    main()