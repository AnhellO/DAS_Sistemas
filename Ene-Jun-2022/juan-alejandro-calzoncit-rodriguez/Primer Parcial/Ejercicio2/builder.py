import sys , os , abc
sys.path.append(os.path.dirname(os.path.realpath(__file__)) + "/../Ejercicio1")
import page as pg
import webSite as wb


'''
Implementación patrón Builder para construir objetos de tipo Page & WebSite
'''

# Interface Builder
class Builder(abc.ABC):
    @abc.abstractmethod
    def reset(self):
        pass

    def setUrl():
        pass

    def setFolder():
        pass
    
    def setHipervinculos():
        pass

    def setTitulo():
        pass

    def setContenido():
        pass

    def setFormato():
        pass

    def setImagen():
        pass

    def setHojaEstilo():
        pass

    def setDatosEstilo():
        pass

    def setApps():
        pass

    def setDominio():
        pass

    def setSubdominio():
        pass

    def setExtension():
        pass

    def setPaginas():
        pass

    def setDescripcion():
        pass

    def setHosting():
        pass

    def setAdaptadoMoviles():
        pass

    @abc.abstractmethod
    def get_result(self):
        pass

# Builder concreto 
class PageBuiler(Builder):
    def __init__(self) -> None:
        self.__page = pg.Page()
        
    def reset(self):
        self.__page = pg.Page()

    def setUrl(self,url):
        self.__page.setUrl(url)
    
    def setFolder(self,folder):
        self.__page.setFolder(folder)
    
    def setHipervinculos(self,hipervinculos):
        self.__page.setHipervinculos(hipervinculos)

    def setTitulo(self,titulo):
        self.__page.setTitulo(titulo)

    def setContenido(self,contenido):
        self.__page.setContenido(contenido)

    def setFormato(self,formato):
        self.__page.setFormato(formato)

    def setImagen(self,imagen):
        self.__page.setImagen(imagen)

    def setHojaEstilo(self,hojaEstilo):
        self.__page.setHojaEstilo(hojaEstilo)

    def setDatosEstilo(self,datosEstilo):
        self.__page.setDatosEstilo(datosEstilo)

    def setApps(self,apps):
        self.__page.setApps(apps)

    def get_result(self):   # Returna el objeto
        return self.__page

# Builder concreto 
class WebSiteBuiler(Builder):
    def __init__(self) -> None:
        self.__webSite = wb.WebSite()

    def reset(self):
        self.__webSite = wb.WebSite()
    
    def setDominio(self,dominio):
        self.__webSite.setDominio(dominio)

    def setSubdominio(self,subdominio):
        self.__webSite.setSubdominio(subdominio)

    def setExtension(self,extension):
        self.__webSite.setExtension(extension)

    def setPaginas(self,paginas : list):
        self.__webSite.setPaginas(paginas)

    def setDescripcion(self,descripcion):
        self.__webSite.setDescripcion(descripcion)

    def setHosting(self,hosting):
        self.__webSite.setHosting(hosting)

    def setAdaptadoMoviles(self,adaptadoMoviles):
        self.__webSite.setAdaptadoMoviles(adaptadoMoviles)

    def get_result(self):
        return self.__webSite   

# Clase Director
class Director:
    def __init__(self, builder : Builder) -> None:
        self.__builder = builder

    # Función para cambiar builder
    def changeBuilder(self, builder : Builder):
        self.__builder = builder

    # Creación de un tipo de objeto Page
    def makePage(self):
        self.__builder.setUrl('www.themeforest.net')
        self.__builder.setFolder('mi_folder')
        self.__builder.setHipervinculos('<a href="https://themeforest.net/category/wordpress?sort=date">Hipervinculo</a>')
        self.__builder.setTitulo('<h1>Forest</h1>')
        self.__builder.setContenido('<p>Contenido de la página.</p')
        self.__builder.setFormato('HTML')
        self.__builder.setImagen('theme.png')
        self.__builder.setHojaEstilo('Texto de hoja de estilo')
        self.__builder.setDatosEstilo('Datos de estilo')
        self.__builder.setApps('Aplicación 1')
        return self.__builder.get_result()

    def makePage_1(self):
        self.__builder.setUrl('https://www.youtube.com/')
        self.__builder.setFolder('proyecto')        
        self.__builder.setTitulo('<h1>YouTube</h1>')        
        return self.__builder.get_result()

    def makePage_2(self):
        self.__builder.setUrl('https://refactoring.guru/')
        self.__builder.setFolder('datos')
        self.__builder.setHipervinculos('<a href="https://refactoring.guru/es/design-patterns/builder">Hipervinculo</a>')
        self.__builder.setTitulo('<h1>Forest</h1>')
        self.__builder.setFormato('HTML')
        return self.__builder.get_result() 

    # Creación de un tipo de objeto WebSite
    def makeWebSite(self):
        self.changeBuilder(PageBuiler())
        pg = self.makePage()
        pg1 = self.makePage_1()
        pg2 = self.makePage_2() 
        self.changeBuilder(WebSiteBuiler())
        self.__builder.setPaginas([pg,pg1,pg2])
        self.__builder.setDominio('amazon')
        self.__builder.setSubdominio('www')
        self.__builder.setExtension('.com')
        self.__builder.setDescripcion('Shopping')
        self.__builder.setHosting('Hosting El Mariachi')
        self.__builder.setAdaptadoMoviles(True)
        return self.__builder.get_result()

    def makeWebSite_1(self):        
        self.changeBuilder(PageBuiler())
        pg = self.makePage()
        pg1 = self.makePage_1()
        self.changeBuilder(WebSiteBuiler())
        self.__builder.setPaginas([pg,pg1])
        self.__builder.setDominio('cars.com')
        self.__builder.setSubdominio('www')
        return self.__builder.get_result()

    def makeWebSite_2(self):
        self.changeBuilder(PageBuiler())        
        pg1 = self.makePage_1()
        pg2 = self.makePage_2()
        self.changeBuilder(WebSiteBuiler())
        self.__builder.setPaginas([pg1,pg2])
        self.__builder.setDominio('themeforest.com')
        self.__builder.setSubdominio('www')
        self.__builder.setDescripcion('Diferentes temas')                
        return self.__builder.get_result()

# Función main
def main():
    # Objetos de builder concretos
    pageBuilder= PageBuiler()   
    webSiteBuilder = WebSiteBuiler()

    # Objeto de tipo Director se le pasa el builder
    director = Director(pageBuilder)
    page2 = director.makePage_2()   # Objeto que retorna el make_Page2
    print('Página makePage_2() :')
    print(page2.url)
    print(page2.folder)
    print(page2.hipervinculos)
    print(page2.titulo)
    print(page2.formato)

    '''
    https://refactoring.guru/
    datos
    <a href="https://refactoring.guru/es/design-patterns/builder">Hipervinculo</a>
    <h1>Forest</h1>
    HTML
    '''


    director.changeBuilder(webSiteBuilder)  # Se cambia el builder
    wb = director.makeWebSite() # Objeto que retorna makeWebSite
    print('\nWebSite makeWebSite() :')
    print(wb.dominio)
    print(wb.subdominio)
    print(wb.extension)
    print(wb.paginas)
    print(wb.descripcion)
    print(wb.hosting)

    '''
    amazon
    www
    .com
    [<page.Page object at 0x7fab893acbb0>, <page.Page object at 0x7fab893acbb0>, <page.Page object at 0x7fab893acbb0>]
    Shopping
    Hosting El Mariachi
    '''

if __name__ == '__main__':
    main()