import abc

class archivoComponent(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def path(self):
        pass

    def get_Name(self):
        return self.name  # Nombre del archivo

    def get_Type(self):
        return self.type  # Directorio o archivo


class directory(archivoComponent):
    def __init__(self, nombre):
        self.directorios = []
        self.nombre = nombre
        self.tipo = 'Directorio'

    def path(self):
        return f'Nombre: {self.get_Name()}\n Tipo: {self.get_Type()}'
        for i in self.directorios:
            i.path()

    def agregar(self, archive: archivoComponent):
        self.directorios.append(archive)

    def eliminar(self, archive: archivoComponent):
        self.directorios.remove(archive)

    def limpiar(self):
        print("Clearing all the paths")
        self.directorios = []


class Hoja(archivoComponent):
    def __init__(self, nombre, extension):
        self.name = nombre
        self.extension = extension
        self.tipo = 'Archivo'

    def directorio(self):
        return f'Nombre: {self.get_Name()}\n Tipo: {self.get_Type()}'

    def get_Extension(self):
        return self.extension


class SistemaDeArchivos:
    def __init__(self, archive: archivoComponent):
        self.archive = archive

    def printArchive(self):
        self.archive.path()


if __name__ == '__main__':
    #se crean los diferentes archivos que formaran parte del directorio
    root = directory('/')

    etc = directory('/etc')
    var = directory('/var')
    usr = directory('/usr')
    include = directory('/include')
    home = directory('/home')
    users = directory('/users')
    salguer = directory('/salguer')
    documentos = directory('/documentos')

    archivo1 = Hoja('ensayo', 'txt')
    tarea = Hoja('presentacion', 'txt')
    tarea2 = Hoja('DAS', 'txt')

    root.agregar(etc)
    root.agregar(var)
    root.agregar(usr)
    root.agregar(home)

    usr.agregar(include)
    home.agregar(users)

    users.agregar(salguer)
    salguer.agregar(archivo1)

    salguer.agregar(documentos)
    salguer.agregar(tarea)
    salguer.agregar(tarea2)

    root.path()

