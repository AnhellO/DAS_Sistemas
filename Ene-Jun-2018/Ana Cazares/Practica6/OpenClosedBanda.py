from OpenClosed import *

class banda:
    def __init__(self, **args):
        Banda.__init__(self , **args)

    def play(self):
        print (nombre="Los Rockan' Rollas", logo="/some/path/to/perdition.png")

class impresor:

    """docstring for Impresor"""
    def __init__(self, objeto = None):
        Impresor.__init__(self, objeto=None)

        if objeto:
            self.agregarObjeto(objeto)

    def agregarObjeto(self, objeto):
        Impresor.__init__(self, objeto)

    def getPropiedades(self, objeto):
        Impresor.__init__(self, objeto)

    def imprimeObjeto(self, objeto):
        Impresor.__init__(self, objeto)

    def play(self):
        printer = Impresor()
        printer.agregarObjeto(banda)
        printer.imprimeObjeto(banda)

class conector:

    """docstring for Conector"""
    def __init__(self, **args):
        Conector.__init__(self,**args)

    def setConexion(self, motor='mysql'):
        Conector.__init__(self,**args)

    def crearConexion(self, motor=None):
        Conector.__init__(self,**args)

    def play(self):
        conector = Conector()
        conexion = conector.crearConexion()
        print(conexion)
        conexion = conector.crearConexion('mongo')
        print(conexion)
