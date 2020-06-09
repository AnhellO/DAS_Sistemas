import abc


class ArchivoComponent(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def path(self):
        pass

    def get_nombre(self):
        return self.nombre  # Nombre del archivo

    def get_tipo(self):
        return self.tipo  # Directorio o archivo


class Directorio(ArchivoComponent):  # Se declaran los objetos "padres"

    def __init__(self, nombre):
        self.paths = []
        self.nombre = nombre
        self.tipo = 'Directorio'

    def path(self):
        print('{}   --------->    Tipo: {}'.format(self.get_nombre(), self.get_tipo()))
        for i in self.paths:    # Realiza iteraciones a traves de los objetos
            i.path()

    def agrega_path(self, archive: ArchivoComponent):
        self.paths.append(archive)

    def remueve_path(self, archive: ArchivoComponent):
        self.paths.remove(archive)

    def despeja_paths(self):
        print("Despejando todos los paths...")
        self.paths = []


class Hoja(ArchivoComponent):   # Se declaran los objetos "hojas"

    def __init__(self, nombre):
        self.nombre = nombre
        self.tipo = 'Archivo'

    def path(self):
        print('{}    --------->    Tipo: {}'.format(self.get_nombre(), self.get_tipo()))


class SistemaDeArchivos:

    def __init__(self, archive: ArchivoComponent):
        self.archive = archive

    def imprime_archivo(self):
        self.archive.path()

# -*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-

# *** Forma más entendible del árbol que viene a continuación :v

# dir = directorio
# arc = archivo

# (-) raiz
#   (n1 - dir) etc
#   (n1 - dir) var
#   (n1 - dir) user
#   (n1 - dir) include
#   (n1 - dir) home
#   (n1 - dir) users
#   (n1 - dir) daniel
#       (n2 - arc) reporte
#       (n2 - dir) documentos
#           (n3 - arc) tarea
#           (n3 - arc) ejercicio algebra

# -*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-


if __name__ == '__main__':

    raiz = Directorio('/')
# ------------------------------------------ Ramas - Padres - paths
    etc = Directorio('/etc')
    var = Directorio('/var')
    usr = Directorio('/usr')
    include = Directorio('/include')
    home = Directorio('/home')
    users = Directorio('/users')
    daniel = Directorio('/daniel')
    documentos = Directorio('/documentos')
# ------------------------------------------- Hojas - Hijos - archivos
    tarea1 = Hoja('reporte')
    tarea2 = Hoja('tarea')
    tarea3 = Hoja('ejercicio algebra')

# -*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-

    raiz.agrega_path(etc)   # -------- directorio
    raiz.agrega_path(var)   # -------- directorio
    raiz.agrega_path(usr)   # -------- directorio
    raiz.agrega_path(home)  # -------- directorio

    usr.agrega_path(include)    # -------- directorio
    home.agrega_path(users)     # -------- directorio
# -------------------------------------
    users.agrega_path(daniel)       # -------- directorio
    daniel.agrega_path(tarea1)      # -------- archivo
# -------------------------------------
    daniel.agrega_path(documentos)  # -------- directorio
    daniel.agrega_path(tarea2)      # -------- archivo
    daniel.agrega_path(tarea3)      # -------- archivo

    raiz.path()

# ------------------------------------- Imprimimos todooo c:
    sistema = SistemaDeArchivos(etc)
    sistema.imprime_archivo()
