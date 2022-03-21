class Page():
    def __init__(self,url = None,folder = None,link = None,parrafo = None,titulo = None,formato = None,metaDescripcion = None,body = None,image = None) -> None:
        self.url = url
        self.folder =folder
        self.links = link
        self.parrafo =parrafo
        self.titulo =titulo
        self.formato = formato
        self.metaDescripcion = metaDescripcion
        self.body = body
        self.image = image

    def getUrl(self):
        return f"Dirección Url: {self.url}"
    
    def getFolder(self):
        return f"Folder: {self.folder}"

    def getlink(self):
        return f"link: {self.links}"

    def getParrafo(self):
        return f"<p> {self.parrafo} </p>"
    
    def getTitulo(self):
        return f"<h1> {self.titulo} </h1>"
    
    def getFormato(self):
        return f"Formato: {self.formato}"

    def getMetaDescripcion(self):
        return f"Meta-Descripción: {self.metaDescripcion}"

    def getBody(self):
        return f"<body> {self.getParrafo} </body>"

    def getImage(self):
        return f'<img src="{self.image}"'

class Website():
    def __init__(self,dominio = None,subdominio = None ,paginas = None,extension = None,descripcion = None,host = None,language = None) -> None:
        self.dominio = dominio
        self.subdominio = subdominio
        self.paginas = paginas
        self.extension = extension
        self.descripcion = descripcion
        self.host = host
        self.language = language
        
    def getDominio(self):
        return f"{self.dominio}"

    def getSubdominio(self):
        return f"{self.subdominio}"

    def getPaginas(self):
        return f"{self.paginas}"

    def getExtension(self):
        return f"{self.extension}"

    def getDescripcion(self):
        return f"{self.descripcion}"

    def getHost(self):
        return f"{self.host}"

    def getLanguage(self):
        return f"{self.language}"

def buscador(sitio: Website, pagina:Page):
    if pagina in sitio.paginas:
        return f"El sitio contiene la pagina"
    return f"El sitio no contiene la pagina"
def main():
    paginas = []
    pagina1 = Page("www.pagina1.com", "paginas", "pagina1.com", "hola soy la primer pagina", "Pagina 1", "HTML", "hola", "parrafo1","No hay")
    paginas.append(pagina1)
    pagina2 = Page("www.pagina2.com", "paginas", "pagina2.com", "hola soy la segunda pagina", "Pagina 2", "XML", "como", "parrafo2","osito.jpg")
    paginas.append(pagina2)
    pagina3 = Page("www.pagina3.com", "paginas", "pagina3.com", "hola soy la tercer pagina", "Pagina 3", "JSON", "estas", "parrafo3","gato.png")
    paginas.append(pagina3)
    pagina4 = Page("www.pagina4.com", "paginas", "pagina4.com", "hola soy la cuarta pagina", "Pagina 4", "HTML", "estas", "parrafo4","perro.png")

    sitio = Website("Dominio","subdominio",paginas,"extension","descripicion", "host","español")
    print(buscador(sitio,pagina4)) #-> No contiene la página

    print(buscador(sitio,pagina2)) #-> Contiene la página
if __name__ == "__main__":
    main()