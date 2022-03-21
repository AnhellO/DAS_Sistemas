'''
Clase Page la cúal representa a una página dentro
de un sitio web 
'''

class Page:
    def __init__(self,url=None,folder=None, hipervinculos=None,titulo=None,contenido=None,formato=None,imagen=None,hojaEstilo=None,datosEstilo=None,apps=None) -> None : 
        # Atributos
        self.url = url
        self.folder = folder
        self.hipervinculos = hipervinculos
        self.titulo = titulo
        self.contenido = contenido
        self.formato = formato
        self.imagen = imagen
        self.hojaEstilo = hojaEstilo
        self.datosEstilo = datosEstilo
        self.apps = apps
    
    # Setters
    def setUrl(self,url):
        self.url = url
    
    def setFolder(self,folder):
        self.folder = folder
    
    def setHipervinculos(self,hipervinculos):
        self.hipervinculos = hipervinculos

    def setTitulo(self,titulo):
        self.titulo = titulo

    def setContenido(self,contenido):
        self.contenido = contenido

    def setFormato(self,formato):
        self.formato = formato                

    def setImagen(self,imagen):
        self.imagen = imagen

    def setHojaEstilo(self,hojaEstilo):
        self.hojaEstilo = hojaEstilo

    def setDatosEstilo(self,datosEstilo):
        self.datosEstilo = datosEstilo                        

    def setApps(self,apps):
        self.apps = apps


def main():
    # Objeto de de tipo Page
    pag = Page('www.themeforest.net','mi_folder','<a href="https://themeforest.net/category/wordpress?sort=date">Hipervinculo</a>','<h1>Forest</h1>','<p>Contenido de la página.</p','HTML','theme.png','Texto de hoja de estilo','Datos de estilo','Aplicación 1')

    print(pag.url)
    print(pag.folder)
    print(pag.hipervinculos)
    print(pag.titulo)
    print(pag.contenido)
    print(pag.formato)
    print(pag.imagen)
    print(pag.hojaEstilo)
    print(pag.datosEstilo)
    print(pag.apps)

if __name__ == '__main__':
    main()