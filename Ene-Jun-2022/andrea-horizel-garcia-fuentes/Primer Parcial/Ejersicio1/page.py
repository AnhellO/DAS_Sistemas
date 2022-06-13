
class Page:
    def __init__(self,titulo,texto,cuerpo,URL,imagenes,folder,links,cabezeras,scripts,css):
        self.titulo = titulo
        self.texto = texto
        self.cuerpo = cuerpo
        self.URL = URL
        self.imagenes = imagenes
        self.folder = folder
        self.links = links 
        self.cabezeras = cabezeras
        self.scripts = scripts      
        self.css = css

    #Metodo get y Set
    def getTitulo(self):
        return self.titulo
    
    def setTitulo(self,titulo):
        self.titulo = titulo
        

    def getTexto(self):
        return self.texto
    
    def setTexto(self,texto):
        self.texto = texto

    def getCuerpo(self):
        return self.cuerpo
    
    def setCuerpo(self,cuerpo):
        self.cuerpo = cuerpo
    
    def getURL(self):
        return self.URL
    
    def setURL(self,URL):
        self.URL = URL
    
    def getImagenes(self):
        return self.imagenes 
    
    def setImagenes(self,imagenes):
        self.imagenes = imagenes

    def getFolder(self):
        return self.folder
    
    def setFolder(self,folder):
        self.foler = folder
    
    def getLinks(self):
        return self.links

    def setLinks(self,links):
        self.links = links
    
    def getCabezeras(self):
        return self.cabezera
    
    def setCabezeras(self,cabezeras):
        self.cabezeras = cabezeras
    
    def getScripts(self):
        return self.scripts
    
    def setScripts(self,scripts):
        self.scripts = scripts

    def getCss(self):
        return self.css
    
    def setCss(self,css):
        self.css

    def __str__(self):
        mensaje  = "\n* titulo: " + self.titulo
        mensaje += "\n* texto: " + self.texto
        mensaje += "\n* cuerpo: " + self.cuerpo
        mensaje += "\n* URL: " + self.URL
        mensaje += "\n* imagenes: " + self.imagenes
        mensaje += "\n* folder: " + self.folder
        mensaje += "\n* Links: " + self.links
        mensaje += "\n* cabezeras: " + self.cabezeras
        mensaje += "\n* scripts: " + self.scripts
        mensaje += "\n* css: " + self.css
        return mensaje
