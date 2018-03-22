import abc

# Component
class ArchivoComponent(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def imprimeEstructura(self):
        pass

    def getNombre(self):
        return self.nombre

    def getTipo(self):
        return self.tipo

    def setNivel(self, nivel: int):
        self.nivel = nivel

# Composite
class DirectorioComposite(ArchivoComponent):

    def __init__(self, nombre):
        self.nombre = nombre
        self.tipo = 'directorio'
        self.archivos = []

    def imprimeEstructura(self):
        indentacion = "\t" * self.nivel
        print((indentacion + "Nombre: {}\n" + indentacion + "Tipo: {}").format(self.getNombre(), self.getTipo()))

        print(indentacion + "Archivos: \n")
        for archivo in self.archivos:
            archivo.imprimeEstructura()

    def agregaArchivo(self, archivo: ArchivoComponent):
        self.archivos.append(archivo)

# Composite
class ArchivoLeaf(ArchivoComponent):

    def __init__(self, nombre, extension):
        self.nombre = nombre
        self.extension = extension
        self.tipo = 'archivo'

    def imprimeEstructura(self):
        indentacion = "\t" * self.nivel
        print((indentacion + "Nombre: {}\n" + indentacion + "Tipo: {}\n" + indentacion + "Extension: {}\n").format(self.getNombre(), self.getTipo(), self.getExtension()))

    def getExtension(self):
        return self.extension

root = DirectorioComposite('/')
root.setNivel(0)
etc = DirectorioComposite('/etc')
etc.setNivel(1)
var = DirectorioComposite('/var')
var.setNivel(1)
usr = DirectorioComposite('/usr')
usr.setNivel(1)
include = DirectorioComposite('/include')
include.setNivel(2)
home = DirectorioComposite('/home')
home.setNivel(1)
users = DirectorioComposite('/users')
users.setNivel(2)
juanito = DirectorioComposite('/juanito')
juanito.setNivel(3)
archivo1 = ArchivoLeaf('archivo1', 'txt')
archivo1.setNivel(4)
archivo2 = ArchivoLeaf('archivo2', 'html')
archivo2.setNivel(4)
archivo3 = ArchivoLeaf('archivo3', 'css')
archivo3.setNivel(4)

root.agregaArchivo(etc)
root.agregaArchivo(var)
root.agregaArchivo(usr)
root.agregaArchivo(home)

usr.agregaArchivo(include)

home.agregaArchivo(users)
users.agregaArchivo(juanito)
juanito.agregaArchivo(archivo1)
juanito.agregaArchivo(archivo2)
juanito.agregaArchivo(archivo3)

root.imprimeEstructura()

# Client
class SistemaDeArchivos:

    def __init__(self, archivo: ArchivoComponent):
        self.archivo = archivo

    def imprimeArchivo(self):
        self.archivo.imprimeEstructura()

sistema = SistemaDeArchivos(root)
sistema.imprimeArchivo()
