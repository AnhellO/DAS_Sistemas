class Page(object):
    def __init__(self, **args):
        self.url = args.get('url')
        self.path = args.get('path')
        self.link = args.get('link')
        self.contenido = args.get('contenido')
        self.titulo = args.get('titulo')
        self.title = args.get('title')
        self.metadesc = args.get('metadesc')
        self.formato = args.get('formato')
    
    def get_contenido(self):
        return self.contenido
    def set_contenido(self, contenido):
        self.contenido = contenido
    
    def diccionarioDatos(self):
        diccionario = {"url": self.url ,"path":self.path, "link":self.link, "contenido": self.contenido, "titulo": self.titulo, "title": self.title, "metadesc": self.metadesc, "formato": self.formato}
        return diccionario

    def __str__(self):
        return f"Url: {self.url}\nPath:{self.path},Link:{self.link}\nContenido: {self.contenido}\nTitulo: {self.titulo}\nTitle: {self.title}\nMetadesc: {self.metadesc}\nFormato: {self.formato}"

class Website(object):
    def __init__(self, **args):
        self.dominio = args.get('dominio')
        self.subdominio = args.get('subdominio')
        self.childs = {}

    def agregarPagina(self, diccionarioDatos: dict):
        self.childs.update(diccionarioDatos)

    def contenido(self):
        content = {"Dominio":self.dominio, "Subdominio" :self.subdominio, "Paginas": self.childs}
        return content

def main():
    #Pagina Agregada al Website
    pagina = Page(
        url="drive.google.com/drive/",
        path="drive.google.com/drive/my-drive",
        contenido="Archivos en la nube",
        titulo="<h1>Drive</h1>",
        title="<title>Mi unidad<title>",
        metadesc="Arechivos subidos a la nube",
        formato="html")
    
    #Pagina No Agregada al Website
    pagina2=Page(
        url="mail.google.com",
        path="mail.google.com/mail/u/0/#inbox", 
        contenido="Plataforma de correo",
        titulo="<h1>Gmail</h1>",
        title="<title>Recibidos</title>",
        metadesc="Correo Electrnico",
        formato="html")
    
    #El Website xd
    web = Website(
        dominio= "google.com",
        subdominio="www"
    )

    #Aqui la Pagina 1 es agregada al Website
    web.agregarPagina(pagina.diccionarioDatos())
    print("-----------------Contenido del sitio web------------------------------------------------------------------------")
    for key in web.contenido():
        print(key+" ==> "+str(web.contenido()[key]))
    print("-----------------Busqueda de una pagina en el sitio web------------------------------------------------------------------------")
    #Algoritmo de busqueda, Busca que todos los atributos de la pagina concuerden con los qu ehay en el website
    def buscador(web: Website, pagina: Page):
        contador = 0
        for key in web.contenido().get("Paginas"):
            if pagina.diccionarioDatos()[key] == web.contenido().get("Paginas")[key]:
                contador+=1
            else:
                print ("La pagina no existe")
                break
        if contador == len(pagina.diccionarioDatos()):
            print("La pagina si existe")
    #Busqueda de la pagina 1 (Si esta agregada)
    print("--------------Busqueda de pagina 1")
    buscador(web, pagina)

    #Busqueda de la pagina 2 (No esta agregada)
    print("--------------Busqueda de pagina 2")
    buscador(web, pagina2)
if __name__ == '__main__':
    main()
    