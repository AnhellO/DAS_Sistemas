import abc
#Clase componente: implementa un comportamiento comun entre las clases
#y declara una interfaz de manipulacion
class archiveComponent(metaclass = abc.ABCMeta):

    @abc.abstractmethod
    def path(self):
        pass

    def getName(self):
        return self.name

    def getType(self):
        return self.type

#Esta clase define el comportamiento de los objetos hijos y almacena componentes hijos, en este caso
#para los directorios y los archivos de los directorios

class directoryComposite(archiveComponent):

    def __init__(self, nombre):
        self.paths = []
        self.name = nombre
        self.type = 'directory'

    def path(self):
        print(("Name: {} \nType: {}\n").format(self.getName(), self.getType()))
        #print("Archives: \n")
        for i in self.paths:
            i.path()

    def addPath(self, archive: archiveComponent):
        self.paths.append(archive)

    def removePath(self, archive: archiveComponent):
        self.paths.remove(archive)

    def clearPaths(self):
        print("Clearing all the paths")
        self.paths = []

#A continuacion se declaran los objetos "hoja"
# Composite
class archiveLeaf(archiveComponent):

    def __init__(self, nombre, extension):
        self.name = nombre
        self.extension = extension
        self.type = 'archive'

    def path(self):
        print(("Name: {}\n Type: {}\nExtension: {}\n").format(self.getName(), self.getType(), self.getExtension()))

    def getExtension(self):
        return self.extension

# Client
class SistemaDeArchivos:

    def __init__(self, archive: archiveComponent):
        self.archive = archive

    def printArchive(self):
        self.archive.path()

if __name__ == '__main__':
        root = directoryComposite('/')
        etc = directoryComposite('/etc')
        var = directoryComposite('/var')
        usr = directoryComposite('/usr')
        include = directoryComposite('/include')
        home = directoryComposite('/home')
        users = directoryComposite('/users')
        karla = directoryComposite('/karla')
        archivo1 = archiveLeaf('archivo1', 'txt')
        archivo2 = archiveLeaf('archivo2', 'html')
        archivo3 = archiveLeaf('archivo3', 'css')

        root.addPath(etc)
        root.addPath(var)
        root.addPath(usr)
        root.addPath(home)

        usr.addPath(include)

        home.addPath(users)
        users.addPath(karla)
        karla.addPath(archivo1)
        karla.addPath(archivo2)
        karla.addPath(archivo3)

        root.path()

        sistema = SistemaDeArchivos(root)
        sistema.printArchive()
