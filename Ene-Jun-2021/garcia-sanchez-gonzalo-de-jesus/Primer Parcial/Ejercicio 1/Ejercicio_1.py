#Goncho

"""
Página web
Es un documento que se puede mostrar en un navegador web 
(como Google Chrome,  Mozilla Firefox o Safari de Apple).
En nuestro ejemplo sería el libro de Física.
"""

class PaginaWeb():
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
"""
Sitio web
Es una colección de páginas web que se agrupan y 
normalmente se conectan de varias maneras.
La sección de Ciencias es como un sitio web.
"""
class SitioWeb():
    def __init__(self,dominio,categoria,paginas):
        self.dominio = dominio
        self.categoria = categoria
        self.paginas = paginas

    def __str__(self):
        return f""" 
                    EL DOMINIO: {self.dominio}\n 
                    LA CATEGORIA: {self.categoria}\n
                    LAS PAGINAS: {self.paginas}
                """


def main():
    pagina1 = PaginaWeb(    url = "https://www.callofduty.com/warzone",
                            ruta = "/root",
                            formato = "HTML",
                            contenido = "<body> ¡Warzone Season 2 ya está disponible con nuevas armas, operadores y más!. </body>",
                            titulo = "<title>Call of Duty®: Warzone |  Mejor juego gratuito de Battle Royale</title>",
                            slug = "Call-of Duty®:-Warzone-|-Mejor-juego-gratuito-de-Battle-Royale",
                            meta_tag =["< meta name=description"">","<meta property=og:title"">","<meta http-equiv=content-type content=text/html; charset=UTF-8"">"]
                        )
    
    Sitio1 = SitioWeb(  dominio="callofduty.com",
                        categoria="Juegos",
                        paginas=["/warzone","/blackopscoldwar","/modernwarfare","/mobile"]
                     )

    return print(pagina1,Sitio1)

if __name__ == "__main__":
    main()