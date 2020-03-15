import abc
#Clase componente: implementa un comportamiento comun entre las clases
#y declara una interfaz de manipulacion
class archivoComponent(metaclass = abc.ABCMeta):

    @abc.abstractmethod
    #estructura --- > imprime estructura
    def path(self):
        pass
    
    def getName(self):
        return self.name #Nombre del archivo

    def getType(self):
        return self.type #Directorio o archivo

#Esta clase define el comportamiento de los objetos hijos y almacena componentes hijos, en este caso
#para los directorios y los archivos de los directorios

class directory(archivoComponent):

    def __init__(self, nombre):
        self.paths = []
        self.name = nombre
        self.type = 'directory'

    def path(self):
        #print(('Name: {} \nType: {}\n').format(self.getName(), self.getType()))
        print(('{}---> {}\n').format(self.getName(), self.getType()))
        for i in self.paths:
            i.path()

    def addPath(self, archive: archivoComponent):
        self.paths.append(archive)

    def removePath(self, archive: archivoComponent):
        self.paths.remove(archive)

    def clearPaths(self):
        print("Clearing all the paths")
        self.paths = []

#A continuacion se declaran los objetos "hoja"
# Composite
class Leaf(archivoComponent):

    def __init__(self, nombre, extension):
        self.name = nombre
        self.extension = extension
        self.type = 'archive'

    def path(self):
        #print(('Name: {}\n Type: {}\n').format(self.getName(), self.getType()))
        print(('{} ---> {}\n').format(self.getName(), self.getType()))
    def getExtension(self):
        return self.extension

# User 
class SistemaDeArchivos:

    def __init__(self, archive: archivoComponent):
        self.archive = archive

    def printArchive(self):
        self.archive.path()
        
        #IMPRIME TODO EL ARBOL
        #print('{}'.format(self.nombre))
        #Itera atraves de los objetos e invoca a la funcion Archivo component imprimiendo los nombres
        #for i in self.estructura:
        #   i.estructura()

if __name__ == '__main__':
        root = directory('/') #NODO RAIZ
        #NODOS PADRES
        etc = directory('/etc')
        var = directory('/var')
        usr = directory('/usr')
        include = directory('/include')
        home = directory('/home')
        users = directory('/users')
        deorela = directory('/deorela')
        pictures = directory('/Pictures')
        #NODOS HOJA QUE NO TIENEN RAMIFICACIONES
        archivo1 = Leaf('archivo1', 'txt')
        picture = Leaf('Picture Profile', 'png')
        picture2 = Leaf('Vacations', 'jpg')
        
        # ÁRBOL A CREAR:
    # (1)root
    #   (2)etc
    #   (2)var
    #   (2)user
    #   (2)include
    #   (2)home
    #   (2)users
    #   (2)deorela
    #       (3)archivo1
    #       (3)Pictures
    #           (4)Picture Profile 
    #           (4)Vacations

        
        root.addPath(etc)
        root.addPath(var)
        root.addPath(usr)
        root.addPath(home)

        usr.addPath(include)
        home.addPath(users)
        #PERSONAL FOLDER
        users.addPath(deorela)
        deorela.addPath(archivo1)
        #PICTURES FOLDER
        deorela.addPath(pictures)
        deorela.addPath(picture)
        deorela.addPath(picture2)

        root.path()
        
        #IMPRIMIMOS TODO EL ARBOL
        sistema = SistemaDeArchivos(etc)
        sistema.printArchive()