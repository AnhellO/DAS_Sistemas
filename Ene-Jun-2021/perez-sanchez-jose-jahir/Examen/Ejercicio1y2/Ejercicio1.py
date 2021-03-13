#Instale y importe slugify para hacer el sug
from slugify import slugify
#La clase PaginaWeb con sus atributos y su metodo str
class PaginaWeb():
   def __init__(self,url,ruta,formato,contenido,titulo,slug,metatags:list):
       self.url = url
       self.ruta = ruta
       self.formato = formato
       self.contenido = contenido
       self.titulo = titulo
       self.slug = slug
       self.metatags = metatags
    
   def __str__(self):
        return f"Url de la pagina: {self.url}, ruta de la pagina: {self.ruta}, formato de la pagina: {self.formato}, contenido de la pagina: {self.contenido}, titulo de la pagina: {self.titulo}, slug de la pagina: {slugify(self.slug)} y metatags de la pagina: {self.metatags}"
#La clase SitioWeb con sus atributos, metodo str y el decorador con su metodo buscador
#Implemente de esa manera el decorador con el metodo y funciono sin problemas
#recibe las paginas en modo de lista para almacenar las paginas y poder buscarla facil con un if
class SitioWeb(PaginaWeb):
    def __init__(self,dominio, categoria, paginas: list):
        self.dominio = dominio
        self.categoria = categoria
        self.paginas = paginas
    
    def __str__(self):
        return f"Dominio de la pagina: {self.dominio}, categoria de la pagina: {self.categoria} y paginas: {self.paginas}"

    def decorador(func):
        def wrapper(self, pagina):
            print("Busquemos tu pagina web")
            print("............")
            func(self, pagina)
            print("............")
            print("Aqui esta el resultado")
            print(":D")
        return wrapper

    @decorador
    def buscador(self, pagina: PaginaWeb):
        if pagina in self.paginas:
            print("Pagina encontrada")
            print(pagina)
        else:
            print("Pagina no encontrada")

#Todas las pruebas que realize para checar el funcionamiento de la pagina
def main():
    Pag1 = PaginaWeb("www.simon.com","/https","HTML","<p>Esta es la pagina de Simon</p>","<h1>La pagina de simon</h1>","La pagina de simon","<meta name =description content = This is the description. It should be about 155 characters long.>)")
    Pag2 = PaginaWeb("www.pedro.com","/https","XML","<contenido>Esta es la pagina de Pedro</contenido>","La pagina de pedro","La pagina de pedro","No se")
    Pagdummy = PaginaWeb("x","x","x","x","x","x","x")
    print(Pag1,"\n")
    print(Pag2,"\n")

    paginas = [Pag1, Pag2]

    sitio = SitioWeb(".net","informatica",paginas)
    print(sitio)

    sitio.buscador(Pag1)
    sitio.buscador(Pag2)
    sitio.buscador(Pagdummy)


if __name__ == "__main__":
    main()
